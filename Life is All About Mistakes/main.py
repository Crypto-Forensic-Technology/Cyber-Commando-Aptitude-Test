def decrypt_message(message, key):
    decrypted_text = "" 
    for char in message:
        decrypted_text += chr(ord(char) - key)
    return decrypted_text

encrypted_flag = "Wboef!Nbubsbn"
key = 1  

print("The flag is: decrypt_message(, key))")
