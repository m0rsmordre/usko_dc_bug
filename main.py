import socket
import struct
import binascii
import time
import string

def cevir(p):
    return bytes.fromhex(p)

def chr_paket(chr_id):
    
    chr_id_hex = chr_id.encode("utf-8").hex()
    uzunluk = len(chr_id)
    return "aa55" + str(hex(uzunluk+3))[2:].zfill(2)+"0051" +str(hex(uzunluk))[2:].zfill(2)+"00"+chr_id_hex +"55aa"

HOST =  f"server_ip" #ROSETTA1 ROSETTA2'nin ipsi farklı

AGENT = 15001 #game 
GATEWAY = 15100 #launcher


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, AGENT))

acc_id = "account_id"

s.sendall(cevir(chr_paket(acc_id)))
s.close()  
