def encryption(text, shift):
    encrypted_word = ""
    for i in range(len(text)):
        if (text[i].isupper()):
            encrypted_word += chr((ord(text[i]) + shift - 65) % 26 + 65)
        else:
            encrypted_word += chr((ord(text[i]) + shift - 97) % 26 + 97)
    return encrypted_word

text = "ATTACKATONCE"
shift = 4
print("Text: " + text)
print("Shift: " + str(shift))
print("Cipher: " + encryption(text, shift))

def decryption(text, shift):
    decrypted_word = ""
    for i in range(len(text)):
        if (text[i].isupper()):
            decrypted_word += chr((ord(text[i]) - shift + 65) % 26 + 65)
        else:
            decrypted_word += chr((ord(text[i]) - shift + 97) % 26 + 97)
    return decrypted_word

text = "EXXEGOEXSRGI"
shift = 4
print("Text: " + text)
print("Shift: " + str(shift))
print("Cipher: " + decryption(text, shift))