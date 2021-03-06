import parser
import binascii
from socket_connect import send_to_socket
from ISO8583.ISO8583 import ISO8583

iso = ISO8583()
iso.setMTI('0800')
iso.setBit(3, 990000)  # PROCCESING CODE
iso.setBit(11, 123612)  # STAN
iso.setBit(12, 173645)  # TIME
iso.setBit(13, 1515)  # DATE
total = 26
byteTrama = bytearray(7)

j = int((total - (total % 256)) / 256)
k = total - (256 * j)
byteTrama[0] = int(j)
byteTrama[1] = int(k)
byteTrama = byteTrama.hex().encode()
# encodeo en bytes lo que se va enviar
iso_to_send = binascii.unhexlify(byteTrama) + binascii.unhexlify(iso.getRawIso())
# enviando al socket
response_socket = send_to_socket(iso_to_send)
# print(response_socket)
fp = parser.FullCargaParser(1)
# seteando el ISO en el parset
fp.setByteArrayISO(response_socket)
# leer cada respuesta segun su ISO
# print(fp.getValueFromISO(3))
print(fp.getRawIso())
