# -*- coding: utf-8 -*-
import timeit

P_ROUND = [
    0x243F6A88, 0x85A308D3, 0x13198A2E, 0x03707344,
    0xA4093822, 0x299F31D0, 0x082EFA98, 0xEC4E6C89,
    0x452821E6, 0x38D01377, 0xBE5466CF, 0x34E90C6C,
    0xC0AC29B7, 0xC97C50DD, 0x3F84D5B5, 0xB5470917,
    0x9216D5D9, 0x8979FB1B
    ]

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
    if len(bits) < 256:
        while len(bits) < 256:
            bits += '0'
        for i in range(0, 256, 64):   
            part = bits[i:i+64]
            bits_divided.append(part)
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

#len(num1) == len(num2)
def bit_xor(num1, num2):
    xored = ''
    res = list(zip(num1, num2))
    for i, j in res:
        res = int(i) ^ int(j)
        xored += str(res)
    return xored



txt_bits = get_bits(txt)
bits_ext = extender(txt_bits)
txt_decoded = decoder(bits_ext)


n = 5
# calculate total execution time
result = timeit.timeit(stmt='txt_decoded', globals=globals(), number=n)


print('source:', txt)
print('bytes:', list(bytearray(txt, 'utf-8')))
print('bits:', txt_bits)
print('extended bits:', bits_ext)
print('decode:', txt_decoded)
print(f"Execution time is {result / n} seconds")
