from __future__ import print_function
import os

import grpc

import key_value_pb2, key_value_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:8888')
    stub = key_value_pb2_grpc.StorageStub(channel)

    key = 1
    value = "valor 1"
    message = key_value_pb2.PairKeyValue(key = key, value = value)
    response = stub.insert(message)
    print("1. GRPC client received: " + response.reply)

    
    key, value = (1, "valor 1")
    message = key_value_pb2.PairKeyValue(key = key, value = value)
    response = stub.insert(message)
    print("2. GRPC client received: " + response.reply)

    key, value = (2, "valor 2")
    message = key_value_pb2.PairKeyValue(key = key, value = value)
    response = stub.insert(message)
    print("3. GRPC client received: " + response.reply)

    key = 2
    message = key_value_pb2.Key(key = key)
    response = stub.get(message)
    print("4. GRPC client received: " + response.value)

    key = 3
    message = key_value_pb2.Key(key = key)
    response = stub.get(message)
    print("5. GRPC client received: " + response.value)

    channel.close()
    

if __name__ == '__main__':
    run()

