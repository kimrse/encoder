# -*- coding: utf-8 -*-
txt = str(input('text: '))

def get_bits(txt):
    byte_arr = bytearray(txt, 'utf-8')
    bits = []
    for byte in byte_arr:
        bit = format(byte, '08b')
        bits.append(bit)
    return bits


def extender(bits):
    bits_divided = []
    bits = ''.join(bits)
    if len(bits) < 128:
        while len(bits) < 128:
            bits += '0'
        for i in range(0, 128, 32):   
            part = bits[i:i+32];  
            bits_divided.append(part);
        return bits_divided
    else:
        raise 'len is more than 128'


def decoder(bits_arr):
    bits_divided = []
    bytes_arr = []
    bits_arr = ''.join(bits_arr)
    for i in range(0, 128, 8):
        part = str(bits_arr[i:i+8])
        if part != '0'*8:
            bits_divided.append(part)
    for i in bits_divided:
        byte = int(i, 2)
        bytes_arr.append(int(byte))
    decoded_txt = bytes(bytes_arr).decode('utf-8')
    return decoded_txt


txt_bits = get_bits(txt)
bits_ext = extender(txt_bits)
txt_decoded = decoder(bits_ext)


print('source:', txt)
print('bytes:', list(bytearray(txt, 'utf-8')))
print('bits:', txt_bits)
print('extended bits:', bits_ext)
print('decode:', txt_decoded)