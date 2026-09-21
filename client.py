from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)

# Lista de requisições, incluindo chamadas a múltiplas funcionalidades na mesma requisição
requests = [
    "UPPER hello, world",             # Uma funcionalidade: Maiúsculas
    "REVERSE hello, world",           # Uma funcionalidade: Inverter
    "UPPER,REVERSE hello, world",     # Múltiplas funcionalidades: Maiúsculas e Inverter
    "VOWELS,UPPER sistemas distribuidos", # Múltiplas funcionalidades: Vogais e Maiúsculas
    "INVALID hello"                   # Comando inválido
]

for req in requests:
    print(f"Enviando: {req}")
    s.send(str.encode(req))             # envia a requisição
    data = s.recv(1024)                 # recebe a resposta
    print(f"Resposta do servidor: {bytes.decode(data)}\n")

s.close()               # close the connection
