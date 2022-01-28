import sys
import grpc

import key_value_pb2, key_value_pb2_grpc

# >>> import sys
# >>> print(sys.argv)
# ['example.py', 'one', 'two', 'three']


class KeyValueClient():

    def __init__(self, host):
        self.host = host
        self.channel = grpc.insecure_channel(self.host)
        self.stub = key_value_pb2_grpc.StorageStub(self.channel)

    def insert(self, key, value):
        message = key_value_pb2.PairKeyValue(key = key, value = value)
        response = self.stub.insert(message)
        print(str(response.reply))
        return response.reply

    def get(self, key):
        message = key_value_pb2.Key(key = key)
        response = self.stub.get(message)
        print(str(response.value))
        return response.value

    def activate(self, host):
        message = key_value_pb2.ServerHost(host = host)
        response = self.stub.activate(message)
        print(str(response.number_of_keys))
        return response.number_of_keys

      
    def finish(self):
        message = key_value_pb2.FinishParams()
        response = self.stub.finish(message)
        print(str(response.reply))
        return response.reply



def run(host):
    keyValueClient = KeyValueClient(host)

    while True:
        input_value = input().split(',')
        if input_value[0] == 'I':
            keyValueClient.insert(int(input_value[1]), input_value[2])
            
        elif input_value[0] == 'C':
            keyValueClient.get(int(input_value[1]))
            
        elif input_value[0] == 'A':
            keyValueClient.activate(input_value[1])
        
        elif input_value[0] == 'T':
            keyValueClient.finish()
            break
        
        else:
            print("Entrada inválida ...")
            break
        
    keyValueClient.channel.close()




if __name__ == '__main__':
    host = sys.argv[1]
    run(host)

