txt = str(input('text: ')).encode('utf-8')


def to_bytes(txt):
    byte_arr = bytearray(txt, 'utf-8')
    result = []
    for i in byte_arr:
        binary = bin(i)
        result.append(binary[2:])
    result = ''.join(result)
    return result


def extender(bits):
    bits_divided = []
    if len(bits) < 128:
        while len(bits) < 128:
            bits += '0'
        for i in range(0, 128, 32):   
            part = bits[ i : i+32];  
            bits_divided.append(part);
        return bits_divided
    else:
        raise 'len is more than 128'


txt_bits = to_bytes(txt)
bits_ext = extender(txt_bits)

test_string = ''.join(bits_ext)
print(txt)
print(txt_bits)
print(bits_ext)

print(test_string)
#print([ord(i) for i in "text"])
#test_string = '1101100110000110110110011000001011011000101001111101100010101000'
#print ('%x' % int(test_string, 2)).decode('hex').decode('utf-8')