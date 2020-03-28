import socket

print("Enter a URL Below:")
x = input()


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((x, 80))
cmd = 'GET data.pr4e.org HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
print('If it says "HTTP/1.1 200 OK" at the top, That means the connections are OK.')
