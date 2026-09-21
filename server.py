from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))  #-
s.listen(1)           #-
print("Servidor aguardando conexões...")
(conn, addr) = s.accept()  # returns new socket and addr. client 
print(f"Conectado por {addr}")

while True:                # forever
  data = conn.recv(1024)   # receive data from client
  if not data: break       # stop if client stopped
  
  msg = bytes.decode(data)
  print(f"Recebido: {msg}")
  
  # O formato da mensagem esperada eh: "CMD1,CMD2 payload"
  parts = msg.split(' ', 1)
  if len(parts) < 2:
      response = "Erro: Formato invalido. Use 'CMD payload'"
  else:
      cmds_str, payload = parts[0], parts[1]
      cmds = cmds_str.split(',')
      
      # Processamento da requisicao (podendo encadear multiplas funcionalidades)
      response = payload
      for cmd in cmds:
          if cmd == 'UPPER':
              response = response.upper()
          elif cmd == 'LOWER':
              response = response.lower()
          elif cmd == 'REVERSE':
              response = response[::-1]
          elif cmd == 'VOWELS':
              # Mantem apenas as vogais
              response = ''.join([c for c in response if c.lower() in 'aeiou'])
          else:
              response = f"Erro: Comando desconhecido '{cmd}'"
              break # Para o processamento em caso de erro
              
  conn.send(str.encode(response)) # retorna os dados processados

conn.close()               # close the connection
