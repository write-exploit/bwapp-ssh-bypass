import paramiko
from termcolor import colored
import os

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect("192.168.1.39",username="bee",password="bug")

while True:
    print(colored("enter command :\n","blue"))
    command = input()
    if command == 'clear':
        if os.name == 'nt':
            os.system("cls")
            continue
        else:
            os.system("clear")
            continue
    stdin, stdout, stderr = ssh.exec_command(command)
    print(stdout.read().decode('ascii')) 
