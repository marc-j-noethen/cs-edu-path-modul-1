def caesar_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result


message = "Wh wg pshhsf hc qfsohs hvob hc zsof b!"
for shift in range(26):
    print(f"Shift {shift}: {caesar_decrypt(message, shift)}")
