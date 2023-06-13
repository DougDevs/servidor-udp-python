# servidor.py
import socket
import math

# Função para verificar se um número é primo
def is_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Configurar o endereço IP e a porta do servidor
IP = '127.0.0.1'
PORTA = 12345

# Criar o socket UDP
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Vincular o socket ao endereço IP e porta
servidor_socket.bind((IP, PORTA))

print("Servidor pronto para receber conexões...")

while True:
    # Receber os dados do cliente e o endereço do cliente
    dados, endereco_cliente = servidor_socket.recvfrom(1024)
    numero = int(dados.decode())

    # Realizar as operações matemáticas
    numero_invertido = int(str(numero)[::-1])
    soma_digitos = sum(map(int, str(numero)))
    resultado_primo = is_primo(numero)
    raiz_quadrada = math.sqrt(numero) if numero >= 0 else None

    # Preparar o resultado para envio
    resultado = f"Número invertido: {numero_invertido}\nSoma dos dígitos: {soma_digitos}\nÉ primo: {resultado_primo}\nRaiz quadrada: {raiz_quadrada}"

    # Enviar o resultado de volta para o cliente
    servidor_socket.sendto(resultado.encode(), endereco_cliente)
