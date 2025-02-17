def caesar_cipher(text, k):
    kq = ""
    for i in text:
        if i.isalpha():
            change = ord('A') if i.isupper() else ord('a')
            kq += chr((ord(i) - change + k) % 26 + change)
        else:
            kq += i  
    return kq

plaintext = "Tran Van Tuan"
k = 18
ciphertext = caesar_cipher(plaintext, k)
print("Ciphertext:", ciphertext)
