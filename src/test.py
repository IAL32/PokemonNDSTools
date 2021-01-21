#!/usr/bin/env python

import io
import codecs
import os
import binascii


def play():

    # Immutable array
    empty_bytes = bytes(4)
    print("Empty bytes:", empty_bytes)

    # Mutable array
    mutable_bytes = bytearray(b'\x00\x0F')
    mutable_bytes[0] = 255
    mutable_bytes.append(128)
    print("Mutable butes:", mutable_bytes)

    # We can even cast these bytes
    immutable_bytes = bytes(mutable_bytes)
    print("Immutable bytes", immutable_bytes)

    # Let's talk about binary streams
    binary_stream = io.BytesIO()
    binary_stream.write("Hello world!\n".encode('ascii'))
    binary_stream.write("Hello world!\n".encode('utf-8'))

    # Moving cursor back to beginning of buffer
    binary_stream.seek(0)

    # We can read all the data from the stream
    stream_data = binary_stream.read()

    print("Type of stream data:", type(stream_data))
    print("Stream data:", stream_data)

    # But maybe we would like to modify the stream data...
    # We have to get the buffer!
    mutable_buffer = binary_stream.getbuffer()
    mutable_buffer[0] = 0xAA

    # Now, let's re-read the original stream.
    binary_stream.seek(0)
    print("Modified stream contents:", binary_stream.read())

    # Now let's get to writing bytes to a file
    with open("test.txt", "wb") as binary_file:
        # We can write text...
        binary_file.write("Write text by encoding\n".encode("utf-8"))
        num_bytes_written = binary_file.write(b'\xDE\xAD\xBE\xEF')
        print("Wrote %d bytes" % num_bytes_written)

    # Now let's read that data
    with open("test.txt", "rb") as binary_file:
        data = binary_file.read()
        print(data)

    # We might want to see the data size
    file_length_in_bytes = os.path.getsize("test.txt")
    print(file_length_in_bytes)

    # For specific applications, we might want to seek to a specific position of the file
    with open("test.txt", "rb") as binary_file:
        # we can try to go the beginning of the file
        binary_file.seek(0, 0)
        # and then read a couple bytes
        couple_bytes = binary_file.read(2)
        print(couple_bytes)

    # Some Int-Byte transformation

    my_int = 0x14
    # The single byte will be written in BigEndian, and it will be with sign
    single_byte = my_int.to_bytes(1, byteorder="big", signed=True)
    print("Single byte:", single_byte)

    # Or we can write 4 bytes for the same integer
    four_bytes = my_int.to_bytes(4, byteorder="big", signed=True)
    print("Four Bytes", four_bytes)

    # What about little endian?
    print("Four bytes little endian", my_int.to_bytes(
        4, byteorder="little", signed=True))

    # We can create bytes also from a list of integers
    bytes_from_list = bytes([255, 128, 16, 16])
    print("Bytes from list:", bytes_from_list)

    # Sometimes its useful to just use bits
    one_byte = int("11110000", 2)
    print("One byte from binary:", one_byte)

    # We can also print the binary string
    print(bin(22))

    # The opposite, Bytes-Integer transformations

    some_bytes = b'\x00\xFF'
    my_int = int.from_bytes(some_bytes, byteorder="big")
    print("Bytes to integer:", my_int)

    # The int can also be signed
    my_int = int.from_bytes(b'\x00\x0F', byteorder="big", signed=True)
    print("Signed integer:", my_int)

    # We can also use a list of integers as a source of byte values
    my_int = int.from_bytes([255, 0, 0, 0], byteorder="big")
    print("From int list:", my_int)

    # Going back to text-encoding

    binary_data = b'TExtttt'
    text = binary_data.decode('utf-8')
    print("Binary data to text:", text)

    # We can also get text from bytes
    binary_data = bytes([65, 66, 67])  # A, B, C
    text = binary_data.decode("utf-8")
    print("ASCII to text:", text)

    # We saw before how to conver text to binary
    message = "Helloooo"
    binary_message = message.encode('utf-8')
    print(binary_message)

    # Using other encodings? no problem.
    cipher_text = codecs.encode('的一是不', 'utf-8')
    print(cipher_text)

    # Hexadecimals? Alright
    some_hex = binascii.unhexlify('00FF')
    print("Hex to bytes:", some_hex)

    # From bytes, we can transform to hex data
    hex_data = binascii.hexlify(b'\x00\xFF')
    print("Hex data:", hex_data)

    # And now let's transform it to string
    text_string = hex_data.decode('utf-8')
    print('TExt from hex', text_string)

    # BITWISE OPERATIONS WOOOHOO

    byte1 = int('11110000', 2)  # 240
    byte2 = int('00001111', 2)  # 15
    byte3 = int('01010101', 2)  # 85

    print("Bitflip of {0:b}: {1:b} {2:b}".format(byte1, ~byte1, -byte1))

    # AND
    print("AND:", byte1 & byte2)

    # OR
    print("OR:", byte1 | byte2)

    # XOR
    print("XOR:", byte1 ^ byte3)

    # Shifting right will lose the right-most bit
    print("right byte shift:", byte2 >> 3)

    # Shifting left will add a 0 bit on the right side
    print("left byte shift:", byte2 << 1)

    # See if a single bit is set
    bit_mask = int('00000001', 2)  # Bit 1
    print("is bit set in byte1?", bit_mask & byte1)  # Is bit set in byte1?
    print("is bit set in byte2?", bit_mask & byte2)  # Is bit set in byte2?


if __name__ == "__main__":
    play()
