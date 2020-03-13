


#----------------
# Bytearray Type
#----------------

# Cast bytes to bytearray
mutable_bytes = bytearray(b'\x00\x0F')

# Bytearray allows modification
mutable_bytes[0] = 255
mutable_bytes.append(255)
print(mutable_bytes)

# Cast bytearray back to bytes
immutable_bytes = bytes(mutable_bytes)
print(immutable_bytes)

#---------------
# BytesIO Class
#---------------

binary_stream = io.BytesIO()
# Binary data and strings are different types, so a str
# must be encoded to binary using ascii, utf-8, or other.
binary_stream.write("Hello, world!\n".encode('ascii'))
binary_stream.write("Hello, world!\n".encode('utf-8'))

# Move cursor back to the beginning of the buffer
binary_stream.seek(0)

# Read all data from the buffer
stream_data = binary_stream.read()

# The stream_data is type 'bytes', immutable
print(type(stream_data))
print(stream_data)

# To modify the actual contents of the existing buffer
# use getbuffer() to get an object you can modify.
# Modifying this object updates the underlying BytesIO buffer
mutable_buffer = binary_stream.getbuffer()
print(type(mutable_buffer))  # class 'memoryview'
mutable_buffer[0] = 0xFF

# Re-read the original stream. Contents will be modified
# because we modified the mutable buffer
binary_stream.seek(0)
print(binary_stream.read())

#------------------------
# Writing Bytes to a file
#------------------------


binary_stream = io.BytesIO()
# Binary data and strings are different types, so a str
# must be encoded to binary using ascii, utf-8, or other.
binary_stream.write("Hello, world!\n".encode('ascii'))
binary_stream.write("Hello, world!\n".encode('utf-8'))

# Move cursor back to the beginning of the buffer
binary_stream.seek(0)

# Read all data from the buffer
stream_data = binary_stream.read()

# The stream_data is type 'bytes', immutable
print(type(stream_data))
print(stream_data)

# To modify the actual contents of the existing buffer
# use getbuffer() to get an object you can modify.
# Modifying this object updates the underlying BytesIO buffer
mutable_buffer = binary_stream.getbuffer()
print(type(mutable_buffer))  # class 'memoryview'
mutable_buffer[0] = 0xFF

# Re-read the original stream. Contents will be modified
# because we modified the mutable buffer
binary_stream.seek(0)
print(binary_stream.read())


#---------------------------
# Reading Bytes from a file
#---------------------------

with open("test_file.dat", "rb") as binary_file:
    # Read the whole file at once
    data = binary_file.read()
    print(data)

# Read file line by line

with open("test.txt", "rb") as text_file:
    # One option is to call readline() explicitly
    # single_line = text_file.readline()

    # It is easier to use a for loop to iterate each line
    for line in text_file:
        print(line)


#------------------
# Integer to Bytes
#------------------

i = 16

# Create one byte from the integer 16
single_byte = i.to_bytes(1, byteorder='big', signed=True) 
print(single_byte)

# Create four bytes from the integer
four_bytes = i.to_bytes(4, byteorder='big', signed=True)
print(four_bytes)

# Compare the difference to little endian
print(i.to_bytes(4, byteorder='little', signed=True))

# Create bytes from a list of integers with values from 0-255
bytes_from_list = bytes([255, 254, 253, 252])
print(bytes_from_list)

# Create a byte from a base 2 integer
one_byte = int('11110000', 2)
print(one_byte)

# Print out binary string (e.g. 0b010010)
print(bin(22))

#------------------
# Bytes to integer
#------------------

# Create an int from bytes. Default is unsigned.
some_bytes = b'\x00\xF0'
i = int.from_bytes(some_bytes, byteorder='big')
print(i)

# Create a signed int
i = int.from_bytes(b'\x00\x0F', byteorder='big', signed=True)
print(i)

# Use a list of integers 0-255 as a source of byte values
i = int.from_bytes([255, 0, 0, 0], byteorder='big')
print(i)

#---------------
# Text encoding
#---------------

# Binary to Text
binary_data = b'I am text.'
text = binary_data.decode('utf-8')
print(text)

binary_data = bytes([65, 66, 67])  # ASCII values for A, B, C
text = binary_data.decode('utf-8')
print(text)

# Text to Binary
message = "Hello"  # str
binary_message = message.encode('utf-8')
print(type(binary_message))  # bytes

# Python has many built in encodings for different languages,
# and even the Caeser cipher is built in
import codecs
cipher_text = codecs.encode(message, 'rot_13')
print(cipher_text)

#------------------
# Base 64 Encoding
#------------------

# Encode binary data to a base 64 string
binary_data = b'\x00\xFF\x00\xFF'

# Use the codecs module to encode
import codecs
base64_data = codecs.encode(binary_data, 'base64')
print(base64_data)

# Or use the binascii module
import binascii
base64_data = binascii.b2a_base64(binary_data)
print(base64_data)

# The base64_string is still a bytes type
# It may need to be decoded to an ASCII string
print(base64_data.decode('utf-8'))

# Decoding is done similarly
print(codecs.decode(base64_data, 'base64'))
print(binascii.a2b_base64(base64_data))

#-------------
# Hexadecimal
#-------------


# Starting with a hex string you can unhexlify it to bytes
deadbeef = binascii.unhexlify('DEADBEEF')
print(deadbeef)

# Given raw bytes, get an ASCII string representing the hex values
hex_data = binascii.hexlify(b'\x00\xff')  # Two bytes values 0 and 255

# The resulting value will be an ASCII string but it will be a bytes type
# It may be necessary to decode it to a regular string
text_string = hex_data.decode('utf-8')  # Result is string "00ff"
print(text_string)


#----------------
# Format Strings
#----------------

a_byte = b'\xff'  # 255
i = ord(a_byte)   # Get the integer value of the byte

bin = "{0:b}".format(i) # binary: 11111111
hex = "{0:x}".format(i) # hexadecimal: ff
oct = "{0:o}".format(i) # octal: 377

print(bin)
print(hex)
print(oct)

#--------------------
# Bitwise Operations
#--------------------

# Some bytes to play with
byte1 = int('11110000', 2)  # 240
byte2 = int('00001111', 2)  # 15
byte3 = int('01010101', 2)  # 85

# Ones Complement (Flip the bits)
print(~byte1)

# AND
print(byte1 & byte2)

# OR
print(byte1 | byte2)

# XOR
print(byte1 ^ byte3)

# Shifting right will lose the right-most bit
print(byte2 >> 3)

# Shifting left will add a 0 bit on the right side
print(byte2 << 1)

# See if a single bit is set
bit_mask = int('00000001', 2)  # Bit 1
print(bit_mask & byte1)  # Is bit set in byte1?
print(bit_mask & byte2)  # Is bit set in byte2?

#-------------------------------
# Struckt Packing and Unpacking
#-------------------------------

