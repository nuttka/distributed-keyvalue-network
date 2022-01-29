from concurrent import futures
import threading
import socket
import sys

import grpc

import key_value_pb2, key_value_pb2_grpc, central_management_pb2, central_management_pb2_grpc



class CentralClient():

    def __init__(self, host):
        self.host = host
        self.channel = grpc.insecure_channel(self.host)  # cria o canal inseguro para o servidor recebido
        self.stub = central_management_pb2_grpc.CentralManagementStub(self.channel) # criação do stub

    def sendKeys(self, server, arr):
        message = central_management_pb2.ServerKeys(server_id = server, arr = arr) # mensagem com o tipo definido no arquivo .proto
        response = self.stub.register(message) # envio da mensagem para o servidor
        return response.number_of_keys # retorna o valor recebido do servidor central
        


class KeyValueService(key_value_pb2_grpc.StorageServicer): # classe que dita serviços que o cliente pode convocar

    def __init__(self, stop_event, host):
        self.host = host
        self.key_value_list = dict() # dicionário para relação chave valor
        self.stop_event = stop_event # thread responável pelo termino do servidor

    def insert(self, request, context):
        key = request.key
        value = request.value
        
        if key not in self.key_value_list:   # se a chave nao existir no dicionario, ela é criada e atribuido o valor, retornando 0
            reply = 0
            self.key_value_list[key] = value
        else:    # caso contrário, nada acontece e retorna -1
            reply = -1

        return key_value_pb2.InsertReply(reply = reply) # retorno do tipo corretamente definido no .proto

    
    def get(self, request, context):
        key = request.key

        if key in self.key_value_list: # se a chave existir, seu valor é retornado
            value = self.key_value_list[key]
        else:  # caso contrário, retona uma string vazia
            value = ""

        return key_value_pb2.Value(value = value) # retorno do tipo corretamente definido no .proto


    def activate(self, request, context):
        
        if len(sys.argv) < 3:
            return key_value_pb2.NumberKeys(number_of_keys = 0) # retorno do tipo corretamente definido no .proto
        
        host = request.host
        central_client = CentralClient(host) # instancia a classe responsável por realizar chamadas no servidor central
        keys_arr = []

        for key in self.key_value_list:
            keys_arr.append(key)

        number_of_keys = central_client.sendKeys(self.host, keys_arr) # envia para o método sendKeys da classe as chaves que o servidor corrente possui
        return key_value_pb2.NumberKeys(number_of_keys = number_of_keys) # retorna o resultado obtido da classe sendKeys, sendo ele o numero de chaves

    
    def finish(self, request, context):
        self.stop_event.set() # disparo da thread
        return key_value_pb2.Finish(reply = 0) # retorno do tipo corretamente definido no .proto



def serve(port):
    host = socket.getfqdn() + ':' + port # nome do dominio + porta

    stop_event = threading.Event() # evento criado para a finalização do servidor, o qual a thread fica em wait até ser disparada 
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    key_value_pb2_grpc.add_StorageServicer_to_server(KeyValueService(stop_event = stop_event, host = host), server)
    server.add_insecure_port(host)
    server.start()
    
    stop_event.wait() # thread em espera para finalização do servidor
    server.stop(5) # finalização do servidor

if __name__ == '__main__':
    port = sys.argv[1] # recebe a porta como arg
    serve(port)