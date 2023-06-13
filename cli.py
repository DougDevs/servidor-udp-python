# cliente.py
import socket

# Configurar o endereço IP e a porta do servidor
IP = '127.0.0.1'
PORTA = 12345

# Criar o socket UDP
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Solicitar ao usuário para digitar um número
numero = input("Digite um número inteiro: ")

# Enviar o número para o servidor
cliente_socket.sendto(numero.encode(), (IP, PORTA))

# Receber a resposta do servidor
resposta, endereco_servidor = cliente_socket.recvfrom(1024)

# Exibir a resposta do servidor
print("Resultado:\n" + resposta.decode())

# Fechar o socket do cliente
cliente_socket.close()
