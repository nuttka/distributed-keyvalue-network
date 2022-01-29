import sys
import grpc

import key_value_pb2, key_value_pb2_grpc


class KeyValueClient(): # classe responsável por mandar e receber mensagens para o servidor de par

    def __init__(self, host):
        self.host = host
        self.channel = grpc.insecure_channel(self.host) # cria o canal inseguro para o servidor recebido
        self.stub = key_value_pb2_grpc.StorageStub(self.channel) # criação do stub

    def insert(self, key, value):
        message = key_value_pb2.PairKeyValue(key = key, value = value) # mensagem com tipo definido no .proto, o qual contém a chave e o valor
        response = self.stub.insert(message) # envio da mensagem para o servidor e obtenção da resposta
        print(str(response.reply))
        return response.reply

    def get(self, key):
        message = key_value_pb2.Key(key = key) # mensagem com tipo definido no .proto, o qual contém a chave
        response = self.stub.get(message) # envio da mensagem para o servidor e obtenção do valor da chave, caso exista
        print(str(response.value))
        return response.value

    def activate(self, host):
        message = key_value_pb2.ServerHost(host = host) # mensagem definida no .proto, o qual possui o endereço do servidor central
        response = self.stub.activate(message) # envio da mensagem para o servidor de par
        print(str(response.number_of_keys))
        return response.number_of_keys # respota com o numero de chaves que o servidor de par enviou para o central

      
    def finish(self):
        message = key_value_pb2.FinishParams() # tipo definido no .proto para finalização do servidor de par
        response = self.stub.finish(message) # obtem a mensagem do servidor de par
        print(str(response.reply))
        return response.reply



def run(host):
    keyValueClient = KeyValueClient(host)   # instancio a classe

    while True: # obtenho o input e para cada um deles chamo a função da classe KeyValueClient responsável
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
        
        # else:
            # print("Entrada inválida ...")
            # break
        
    keyValueClient.channel.close()




if __name__ == '__main__':
    host = sys.argv[1]     # obtenho o host pelo arg
    run(host)

