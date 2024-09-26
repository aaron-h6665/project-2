"""
Author: Aaron Huang
Last Modified: 9/21/2024
Description:
    Implementation of a one-time pad to encrypt and decrypt text files where 
    users may specify an alphanumeric passkey that is either elongated or 
    truncated to match the length of 
    the text file's message length. Encrypted files are written 
    in base64 and may be named to the users liking.
"""

import base64

def select():
    """
    Returns a string that tells the program whether to encrypt or decrypt from user input.

    The input must either be "encrypt" or "decrypt".
    """
    while True:
        method = input("Do you want to encrypt or decrypt? ")
        if method.strip().title() == "Encrypt" or method.strip().title() == "Decrypt":
            return method
        print("Please type Encrypt or Decrypt.")

def get_password():
    """
    Returns a string that is an alphanumeric password obtained from user input.

    The password must consist of only alphanumeric characters and must not be empty.
    """
    while True:
        password = input("Enter an alphanumeric password: ")
        # Check if the password only contains alphanumeric characters and is not empty
        if password.isalnum() and len(password) > 0:
            return password
        print("Invalid password. Please enter a password containing only 0-9, a-z, A-Z.")

def get_filename():
    """
    Returns the filename from user input.
    """
    filename = input("What is the name of the file you want to encrypt/decrypt? ")
    return filename

# get desired user-file output name
def write_encrypted(encrypted_message):
    """
    Obtains what the user wants to name the encrypted file.

    Arguments: the base64 encrypted string

    Writes the base64 encrypted string into a txt file with that name.
    """
    filename = input("What do you want to name the encrypted file: ")
    with open(f'{filename}', 'wb') as file:
        file.write(encrypted_message)

# get desired user-file output name
def write_decrypted(decrypted_message):
    """
    Obtains what the user wants to name the decrypted file.

    Arguments: The decrypted string

    Returns: The name of file decrypted message is written in

    Writes the decrypted string into a txt file with that name.
    """
    filename = input("What do you want to name the decrypted file: ")
    with open(f'{filename}', 'w', encoding = 'utf-8') as file:
        file.write(decrypted_message)
        return filename

# reads the file message
def get_message():
    """
    Obtains the file name and opens that file if that file exists 
    (otherwise an exception will be raised)

    Returns the text found in that file.
    """
    while True:
        try:
            filename = get_filename()

            #to be able to read all unicode characters
            with open(f'{filename}', 'r', encoding='utf-8') as file:
                message = file.read()

            return message
        #in case they misstyped/file does not exist
        except FileNotFoundError:
            print("File not found. Please enter a valid filename.")

# encoding text to utf8
def text_to_binary(text):
    """
    Arguments: the message/text we want to encode

    Returns the UTF-8 encoded text
    """
    return text.encode("utf-8")

# decoding utf8 to text
def binary_to_text(text):
    """
    Arguments: the UTF-8 encoded message/text we want to decode

    Returns the decoded text
    """
    return text.decode("utf-8")

# encryption and decryption mechanism
def one_time_pad(message, password):
    """
    Arguments: the user inputed alphanumeric password and message from user specified file

    Encodes the password into UTF-8. Extends or truncates the password to be the same
    length as the message. XOR's the two together.

    Returns that XOR'ed (encrypted) message.

    Tests to see if the length of the key (enlongated/truncated password) is the 
    length of the message. Tests to see if key as been altered.
    """
    #convert the alphanumeric password into binary
    password = text_to_binary(password)

    #make the password the same length as the binary message
    while len(password) < len(message):
        password = password * 2

    if len(password) > len(message):
        key = password[0: len(message)]
    # test code to see if the key length is the same as the message
    print("The length of the extended/truncated password (key) is the same as the message: " + str(len(key) == len(message)))
    if len(key) >= len(password):
        print("The extended/truncated password (key) as not been altered: " + str(password == key[0: len(password)]))
    elif len(key) < len(password):
        print("The extended/truncated password (key) as not been altered: " + str(password[0: len(key)] == key))

    #XOR each byte one by one, using the zip function which makes lists
    encrypted_message = bytes(byte_a ^ byte_b for byte_a, byte_b in zip(message, key))

    return encrypted_message

def encrypt(message, password):
    """
    Arguments: the user inputed alphanumeric password and message from user specified file

    Encodes message and obtains the return (encrypted message) from the one-time-pad.
    Converts that encrypted message into base64 and writes that message into a file.
    """
    binary_message = text_to_binary(message)
    encrypted_message = one_time_pad(binary_message, password)

    #convert the encrypted message to base64
    encrypted_message_base64 = base64.b64encode(encrypted_message)

    #save the file as a binary file so that we don't run into any problems
    write_encrypted(encrypted_message_base64)

def decrypt(password):
    """
    Arguments: the user inputed alphanumeric password

    Gets file to decrypt from user. Decodes the message from that file to binary.
    Decrypts the decoded message using the one-imte-pad. Decodes the decrypted message 
    into plaintext. Writes a file with the plaintext. Raises exception if file not found.
    """
    filename = get_filename()
    while True:
        try:
            with open(f'{filename}', 'rb') as file:
                encrypted_message_base64 = file.read()
                encrypted_message = base64.b64decode(encrypted_message_base64)
                decrypt_message_binary = one_time_pad(encrypted_message, password)
                decrypted_message = binary_to_text(decrypt_message_binary)
                filename = write_decrypted(decrypted_message)
                return filename

        except FileNotFoundError:
            print("File not found. Please enter a valid filename.")


if __name__ == "__main__":
    # user I/O they can choose encrypt or decrypt
    choice = select()
    # If you want to encrypt a file
    if choice.title() == "Encrypt":
        message = get_message()
        password = get_password()
        encrypt(message, password)

    else:
        # If you want to decrypt a file
        password = get_password()
        decrypted_filename = decrypt(password)
        original_filename = "test.txt"

        # testing if content matches original file
        with open(f"{decrypted_filename}", 'r', encoding='utf-8') as decrypted_file, open(f'{original_filename}', 'r', encoding='utf-8') as original_file:
            decrypted_content = decrypted_file.read()
            original_content = original_file.read()
            print("Does the decrypted file contain the same content as the original file: " + str(decrypted_content == original_content))


"""
# old: used back when I was writing raw binary to strings
temp_byte_list = []
    temp_chr_list = binary_message_formatted.split(' ')
    temp_chr_list.pop()
    for chr in temp_chr_list:
        byte = chr.split(':')
        temp_byte_list.append(byte)

    binary_key = binary_key_formatted.replace(":", "")
    binary_key = binary_key.replace(" ", "")
    binary_message = binary_message_formatted.replace(":", "")
    binary_message = binary_message.replace(" ", "") 
"""

"""
    old: long attempt to decrypt message when working with strings
    print(decrypted_message_binary)
    print(temp_byte_list)

    i = 0 
    for chr in temp_byte_list:
        for _ in range(len(chr) - 1):
            decrypted_message_binary = decrypted_message_binary[0: 9*i+8] + ":" + decrypted_message_binary[9*i+8:]
            i += 1
        decrypted_message_binary = decrypted_message_binary[0: 9*i+8] + " " + decrypted_message_binary[9*i+8: ]
        i += 1
    
    print(decrypted_message_binary)
    
    new_list = []

    for chr in list_chrs:
        chrs = []
        temp = chr.split(":")
        for bit in temp:
            f = int(bit, 2)
            chrs.append(f)
        chrs = bytes(chrs)
        new_list.append(chrs)
"""

"""
 Old key extension algorithm:
    encrypted_message = int(binary_message, 2) ^ int(binary_key, 2)
    encrypted_message = bin(encrypted_message)[2:].zfill(len(binary_key))
"""

"""
old attempt to decrypt the message:
    i, j = 0, 0
    for chr in temp_byte_list:
        for byte in range(len(chr) - 1):
            encrypted_message = encrypted_message[0: 9*i+8] + ":" + encrypted_message[9*i+8:]
            i += 1
        encrypted_message = encrypted_message[0: 9*i+8] + " " + encrypted_message[9*i+8: ]
        i += 1
"""

"""
old encoding: used back when I was writing raw binary to strings
    for chr in text:
        chr = chr.encode("utf-8")
        binary_format = ':'.join(f'{byte:08b}' for byte in chr)
        #list_chrs.append(binary_format)
        binary_string += binary_format
        binary_string += " "
        #print(binary_format, end = '')
    return binary_string
    """
