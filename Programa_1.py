# Documentación: https://docs.python.org/es/3/library/platform.html

# Programa que imprime la versión del sistema operativo, el tipo de sistema operativo y la ip actual de mi computadora
# hostname y el procesador que estamos utilizando  

import platform
import sys
import subprocess

sistemaop = sys.platform
sistema = platform.system()
version = platform.win32_ver()
name = platform.node()
procesador = platform.processor()

print("Estamos en {}".format(sistema), " en version: {}".format(version))
print ("Tipo SO: {}".format(sistemaop))
if sistema == 'Windows':
    local = subprocess.getoutput("""for /f "tokens=2 delims=[]" %a in ('ping -n 1 -4 "%computername%"') do @echo %a""")
else:
    local = subprocess.getoutput("ifconfig | grep 'inet ' | grep -Fv 127.0.0.1 | awk '{print $2}'")
print(local)
print("Hostname: {}".format(name))
print("Procesador: {}".format(procesador))