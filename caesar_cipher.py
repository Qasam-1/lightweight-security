# Caesar cipher to encrypt stuff, a bit old not every secure

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

if __name__ == "__main__":
    msg = input("Enter a message: ")
    shift = int(input("Enter shift (number): "))

    encrypted = caesar_encrypt(msg, shift)
    print("Encrypted:", encrypted)

    decrypted = caesar_decrypt(encrypted, shift)
    print("Decrypted:", decrypted)
