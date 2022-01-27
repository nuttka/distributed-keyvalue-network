# from __future__ import print_function

import grpc

import key_value_pb2, key_value_pb2_grpc


class KeyValueClient():

    def __init__(self):
        self.host = 'localhost:50051'
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

      
    def finish(self):
        message = key_value_pb2.finishParams()
        response = self.stub.finish(message)
        print(str(response.reply))
        return response.reply



def run():
    keyValueClient = KeyValueClient()

    while True:
        input_value = input().split(',')
        if input_value[0] == 'I':
            keyValueClient.insert(int(input_value[1]), input_value[2])
            
        elif input_value[0] == 'C':
            keyValueClient.get(int(input_value[1]))
            
        elif input_value[0] == 'A':
            pass
        
        elif input_value[0] == 'T':
            keyValueClient.finish()
            break
        
        else:
            print("Entrada inválida ...")
            break
        
    keyValueClient.channel.close()




if __name__ == '__main__':
    run()
