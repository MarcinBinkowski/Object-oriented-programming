CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.'
        }

CODE_REVERT = dict((v, k) for k, v in CODE.items())


def decode(morse_code):
    decoded_text = ""
    words = split_text(morse_code)
    for word in words:
        letter_list = filter(None, split_word(word))
        for letter in letter_list:
            decoded_text += decode_letter(letter)
        decoded_text += " "
    return decoded_text[:len(decoded_text)-1]


def split_text(morse_code):
    return morse_code.split("  ")


def split_word(word):
    return word.split(" ")


def decode_letter(letter):
    return CODE_REVERT[letter]


def encode(text):
    morse_code = ""
    for letter in text.upper():
        if letter != " ":
            morse_code += CODE[letter]
            morse_code += " "
        if letter == " ":
            morse_code += " "
    return morse_code[:len(morse_code)-1]
