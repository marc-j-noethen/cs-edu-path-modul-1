def shift_character(character, shift):
    if not character.isalpha():
        return character
    base = ord("A") if character.isupper() else ord("a")
    return chr((ord(character) - base - shift) % 26 + base)


def caesar_decrypt(text, shift):
    return "".join(shift_character(character, shift) for character in text)


if __name__ == "__main__":
    cipher_text = "Wh wg pshhsf hc qfsohs hvob hc zsof b!"
    print("# Shift-Key 14")
    print(caesar_decrypt(cipher_text, 14))
