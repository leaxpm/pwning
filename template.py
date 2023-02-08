#! /usr/bin/python3
from pwn import *

#Connection host
host = '127.0.0.1'
puerto = 9003

#Settings Linux 
nombre_binario = './'
binario = context.binary = ELF(nombre_binario)

#DEBUG OPTION
context.log_level = "debug"

if(args['REMOTO']):
    p = remote(host, puerto)
else:
    p = process(nombre_binario)

if(args['GDB']):
    comandos_gdb = ""
    comandos_gdb += "continue\n"
    gdb.attach(p, comandos_gdb)
