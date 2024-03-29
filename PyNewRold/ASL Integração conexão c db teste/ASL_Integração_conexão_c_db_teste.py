import mysql.connector
import subprocess
import psutil
import time

###
host = 'localhost'
port = 3306  
user = 'skillo'
password = 'skilloeocara'
###
CGood = 0
CBad = 0 
###
Pid = []
NCaminhos = 3
Caminhos = [
    r"C:\Users\luiz.molina\Downloads\Stremio+4.4.165.exe",
    r"C:\Users\luiz.molina\Downloads\Stremio+4.4.165.exe",
    r"C:\Users\luiz.molina\Downloads\Stremio+4.4.165.exe"
]

def checar(host, port, user, password):
    try:
        conn = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password
        )
        conn.close()
        return True
    except mysql.connector.Error as e:
        return False

def iniciar_programas():
    for i in range(NCaminhos):
        processo = subprocess.Popen([Caminhos[i]])
        Pid.append(processo.pid)
        time.sleep(3.0)

def fechar_programas():
    for i in range(NCaminhos):
        processo = psutil.Process(Pid[i])
        processo.terminate()
        time.sleep(3.0)

def Main():  
    global CGood, CBad
    if checar(host, port, user, password):
        CGood += 1 
    else:
        CBad += 1
        fechar_programas()
        iniciar_programas()


iniciar_programas()
while True:
    Main()
    time.sleep(10.0)
