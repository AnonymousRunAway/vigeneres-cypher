def vigenere(query: str, key: str, decrypt: bool = False) -> str:
    """Encrypts or decrypts a text using the Vigenère cipher, handling uppercase and special characters.

    Args:
        query (str): The input text to be encrypted or decrypted.
        key (str): The keyword used for encryption.
        decrypt (bool, optional): If True, decrypts the text. Defaults to False (encrypt).

    Returns:
        str: The encrypted or decrypted text.
    """

    result = []
    key_index = 0

    for char in query:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shift = ord(key[key_index % len(key)].lower()) - ord('a')
            shifted_char = chr(((ord(char) - ord('a') + (shift * (-1 if decrypt else 1))) % 26) + ord('a'))
            result.append(shifted_char.upper() if is_upper else shifted_char)
            key_index += 1
        else:
            result.append(char)  # Preserve non-alphabetic characters

    return ''.join(result)