import sys
import grpc

import central_management_pb2, central_management_pb2_grpc, key_value_pb2, key_value_pb2_grpc


class CentralClient():

    def __init__(self, host):
        self.host = host
        self.channel = grpc.insecure_channel(self.host)
        self.stub = central_management_pb2_grpc.CentralManagementStub(self.channel)

    def findServer(self, key):
        message = central_management_pb2.Key(key = key)
        response = self.stub.find(message)

        if not response.server:
            pass
        else:
            key_value_client = KeyValueClient(response.server)
            value = key_value_client.get(key)
            print(response.server + ':' + str(value))
            return value

      
    def finish(self):
        message = central_management_pb2.FinishParams()
        response = self.stub.finish(message)
        print(str(response.number_of_keys))
        return response.number_of_keys



class KeyValueClient():

    def __init__(self, host):
        self.host = host
        self.channel = grpc.insecure_channel(self.host)
        self.stub = key_value_pb2_grpc.StorageStub(self.channel)

    def get(self, key):
        message = key_value_pb2.Key(key = key)
        response = self.stub.get(message)
        return response.value





def run(host):
    centralClient = CentralClient(host)

    while True:
        input_value = input().split(',')
        if input_value[0] == 'C':
            centralClient.findServer(int(input_value[1]))
        
        elif input_value[0] == 'T':
            centralClient.finish()
            break
        
        else:
            # print("Entrada inválida ...")
            break
        
    centralClient.channel.close()




if __name__ == '__main__':
    host = sys.argv[1]
    run(host)

