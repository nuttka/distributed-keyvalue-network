import sys
import grpc

import central_management_pb2, central_management_pb2_grpc, key_value_pb2, key_value_pb2_grpc


class CentralClient(): # classe responsável por mandar e receber mensagens para o servidor central

    def __init__(self, host):
        self.host = host
        self.channel = grpc.insecure_channel(self.host) # cria o canal inseguro para o servidor de central recebido
        self.stub = central_management_pb2_grpc.CentralManagementStub(self.channel) # criação do stub

    def findServer(self, key): # realiza uma chamada no servidor central buscando obter o servidor no qual está uma chave
        message = central_management_pb2.Key(key = key) # mensagem que contém a chave requerida no tipo definido no .proto
        response = self.stub.find(message) # envia para o servidor central a chave

        if not response.server: # caso o servidor central envie uma string vazia, não faz nada visto que a chave nao foi encontrada
            pass
        else: # caso o servidor central retorne o servidor de par que possui a chave, enviamos uma mensagem ao servidor a fim de obter o valor da chave
            key_value_client = KeyValueClient(response.server) # instanciaçaõ da classe que faz tal comunicação, passando o endereço do servidor
            value = key_value_client.get(key) # chamada do método que chama o servidor de par e obtenção do valor da chave
            print(response.server + ':' + str(value))
            return value

      
    def finish(self):
        message = central_management_pb2.FinishParams() # tipo definido no .proto para finalização do servidor central
        response = self.stub.finish(message) # obtem a mensagem do servidor central
        print(str(response.number_of_keys))
        return response.number_of_keys # resposta do servidor com o numero de chaves



class KeyValueClient(): # classe responsável por mandar e receber mensagens para o servidor de par

    def __init__(self, host):
        self.host = host
        self.channel = grpc.insecure_channel(self.host) # cria o canal inseguro para o servidorde par recebido
        self.stub = key_value_pb2_grpc.StorageStub(self.channel) # cria o stub

    def get(self, key):
        message = key_value_pb2.Key(key = key) # tipo de mensagem definido no .proto para envio da chave
        response = self.stub.get(message) # envio da mensagem para o servidor par e recebimento da resposta
        return response.value # resposta do servidor com o valor da chave





def run(host):
    centralClient = CentralClient(host)

    while True: # obtenho o input e para cada um deles chamo a função da classe CentralClient responsável
        input_value = input().split(',')
        if input_value[0] == 'C':
            centralClient.findServer(int(input_value[1]))
        
        elif input_value[0] == 'T':
            centralClient.finish()
            break
        
        # else:
            # print("Entrada inválida ...")
            # break
        
    centralClient.channel.close()




if __name__ == '__main__':
    host = sys.argv[1] # recebe o servidor por arg
    run(host)

