"""This python3 script will recognize hex, binary, and base64 strings and convert them to ascii."""
#Written by Christopher Rider

#Note: base64 strings without padding ('=') that contain only [A-Fa-f0-9] will be recognized as hex. 

import codecs
import base64
import re
import binascii

# Get the input
import sys
input = sys.argv[1]
#Remove any whitespace
input = input.replace(' ','')

#FUNCTIONS
#CHECK & CONVERT: binary
def check_binary(binary):
    """This function checks if it's binary."""
    #Cleaning input up
    if binary[:2] == '0b':
        binary = binary[2:]
    x = len(binary)
    #Checking if binary
    if bool(re.search('[0-1]{' + str(x) + '}', binary)):
        return True

def convert_binary(binary):
    """This function converts a binary string to ascii."""
    if binary[:2] != '0b':
        binary = '0b'+ binary
    binary = int(binary, 2)
    output = binary.to_bytes((binary.bit_length() + 7) // 8, 'big').decode()
    return output

#CHECK & CONVERT: hex
def check_hex(hex):
    """This function checks if it is hex."""
    if hex[:2] == '0x':
        hex = hex[2:]
    x = len(hex)
    if bool(re.search('[a-fA-F0-9]{' + str(x) + '}', hex)):
        return True

def convert_hex(hex):
    """This function converts hex to ascii"""
    if hex[:2] == '0x':
        hex = hex[2:]
    output = bytes.fromhex(hex).decode('utf-8')
    return output

#CHECK & CONVERT: base64
def check_base64(b64):
    """This function checks if it's base64."""
    #Removes the trailing = or ==
    b64 = re.sub("={,2}$", '', b64, 2)
    #Checks if it's base64
    if bool(re.search('[a-zA-Z0-9]{' + str(len(b64)) + '}', b64)):
        return True

def convert_base64(b64):
    """This function converts base64 to ascii"""
    #Doing the conversion
    output = base64.b64decode(b64).decode('utf-8')
    #Returning the output, converting to remove the b' prefix
    return output



# CHECKING THE ENCODING
if check_binary(input):
    output_binary = convert_binary(input)
    print("Binary to ascii:\n" + output_binary)
elif check_hex(input):
    output_hex = convert_hex(input)
    print("Hex to ascii:\n" + output_hex)
elif check_base64(input):
    output_b64 = convert_base64(input)
    print("Base64 to ascii:\n" + output_b64)
else:
    print("I'm not sure what encoding this is.")
