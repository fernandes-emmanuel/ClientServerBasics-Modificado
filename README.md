# Processador de Texto Remoto (Cliente/Servidor)

Este projeto implementa um servidor de processamento de texto remoto com base no exemplo básico de Cliente-Servidor (Fig. 2.3). 

A aplicação permite que o cliente envie um texto (payload) e instrua o servidor a executar uma ou mais operações sobre ele. O servidor processa os dados solicitados e retorna a string processada.

## Funcionalidades Disponíveis

O servidor suporta quatro (4) operações básicas de manipulação de texto:
- `UPPER`: Converte todo o texto para letras maiúsculas.
- `LOWER`: Converte todo o texto para letras minúsculas.
- `REVERSE`: Inverte a ordem dos caracteres do texto.
- `VOWELS`: Filtra e retorna apenas as vogais presentes no texto (ignorando consoantes e espaços).

## Encadeamento de Operações

Uma das principais funcionalidades do sistema é a capacidade de **encadear múltiplas operações em uma única requisição**. O cliente pode enviar uma lista de comandos separados por vírgula. O servidor aplicará as transformações sequencialmente.

**Exemplo de formato de requisição:**
`COMANDO1,COMANDO2 texto_a_processar`

Exemplos práticos suportados pelo cliente:
- `UPPER hello, world` -> `HELLO, WORLD`
- `REVERSE python is fun` -> `nuf si nohtyp`
- `UPPER,REVERSE testes de rede` -> `EDER ED SETSET`
- `VOWELS,UPPER sistemas distribuidos` -> `IEAIIUIO`

## Como Executar

1. Certifique-se de que o endereço de IP e porta estão corretamente configurados no arquivo `constCS.py`. Para rodar na mesma máquina, `HOST` está configurado como `'127.0.0.1'`.
2. Em um terminal, inicie o servidor: `python server.py`
3. Em outro terminal, inicie o cliente para rodar os casos de teste pré-definidos: `python client.py`
