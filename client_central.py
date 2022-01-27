# from __future__ import print_function

import grpc

import central_management_pb2, central_management_pb2_grpc


class CentralClient():

    def __init__(self):
        self.host = 'localhost:8080'
        self.channel = grpc.insecure_channel(self.host)
        self.stub = central_management_pb2_grpc.CentralManagementStub(self.channel)

    def findServer(self, key):
        message = central_management_pb2.Key(key = key)
        response = self.stub.find(message)
        print(str(response.value))
        return response.value

      
    def finish(self):
        message = central_management_pb2.finishParams()
        response = self.stub.finish(message)
        print(str(response.reply))
        return response.reply



def run():
    centralClient = CentralClient()

    while True:
        input_value = input().split(',')
        if input_value[0] == 'C':
            centralClient.findServer(input_value[1])
        
        elif input_value[0] == 'T':
            centralClient.finish()
            break
        
        else:
            print("Entrada inválida ...")
            break
        
    centralClient.channel.close()




if __name__ == '__main__':
    run()

