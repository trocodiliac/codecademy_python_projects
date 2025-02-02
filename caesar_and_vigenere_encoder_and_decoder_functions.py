# CAESAR DECODER
def caesar_decode(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decoded_msg = ''
    letter_index = 0
    for letter in message:
        letter_index = alphabet.find(letter)
        if letter_index + offset > (len(alphabet) - 1):
            letter_index += offset - len(alphabet)
        elif letter not in alphabet:
            decoded_msg += letter
            continue
        else:
            letter_index += offset
        decoded_msg += alphabet[letter_index]
    return decoded_msg

# CAESAR ENCODER
def caesar_encode(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encoded_msg = ''
    letter_index = 0
    for letter in message:
        letter_index = alphabet.find(letter)
        if letter not in alphabet:
            encoded_msg += letter
        else:
            encoded_msg += alphabet[letter_index - offset]
    return encoded_msg

# VIGENERE DECODER
def vigenere_decipher(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key_phrase = ''
    decoded_msg = ''
    index = 0
    
    # Define key_phrase
    for letter in message:
        if letter == ' ':
            key_phrase += ' '
        elif letter not in alphabet:
            continue
        else:
            key_phrase += key[index]
            index += 1
        if index > len(key) - 1:
            index = 0

    # Reset index and create new variables
    index = 0
    letter_index = 0
    shift = 0

    # Use key_phrase to define decoded_msg
    for letter in message:
        
        if index > len(key_phrase) - 1:
            index = 0
        shift = alphabet.find(key_phrase[index])
        letter_index = alphabet.find(letter)
        
        if letter == ' ':
            decoded_msg += letter
            index += 1
        elif letter not in alphabet:
            decoded_msg += letter
            continue
        else:
            if letter_index + shift > len(alphabet) - 1:
                letter_index = letter_index + shift - len(alphabet)
            else:
                letter_index += shift
            decoded_msg += alphabet[letter_index]
            index += 1
    return decoded_msg

# VIGENERE ENCODER
def vigenere_cipher(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key_phrase = ''
    encoded_msg = ''
    index = 0
    
    # Define key_phrase
    for letter in message:
        if letter == ' ':
            key_phrase += ' '
        elif letter not in alphabet:
            continue
        else:
            key_phrase += key[index]
            index += 1
        if index > len(key) - 1:
            index = 0
            
    # Reset index and create new variables
    index = 0
    letter_index = 0
    shift = 0
    
    # Encode message using key_phrase
    for letter in message:
        
        if index > len(key_phrase) - 1:
            index = 0
        shift = alphabet.find(key_phrase[index])
        letter_index = alphabet.find(letter)
        
        if letter == ' ':
            encoded_msg += letter
            index += 1
        elif letter not in alphabet:
            encoded_msg += letter
            continue
        else:
            if letter_index - shift < 0:
                letter_index = letter_index - shift + len(alphabet)
            else:
                letter_index -= shift
            encoded_msg += alphabet[letter_index]
            index += 1
    return encoded_msg
