# Vigenère Cipher
This Python script implements the Vigenère cipher, a method of encryption that uses a repeating keyword to obscure plaintext. This implementation supports both uppercase and lowercase letters, as well as special characters.

# Functions:

```vigenere(query, key, decrypt=False): Encrypts or decrypts a given text using the Vigenère cipher.```

query: The input text to be encrypted or decrypted.
key: The keyword used for encryption.
decrypt: A boolean flag indicating whether to decrypt (True) or encrypt (False).

# Sample Usage: 

```
encrypted_text = vigenere("Hello, World!", "secret")
print(encrypted_text)  # Output: Rotq, Ebiqv!

decrypted_text = vigenere(encrypted_text, "secret", decrypt=True)
print(decrypted_text)  # Output: Hello, World!
```
