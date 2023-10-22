def morse(text):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
        '.': '.-.-.-', ',': '--..--', ':': '---...', "'": '.----.', '!': '-.-.--', '?': '..--..', ' ': ' '
    }
    
    text = text.upper()  # Convert the input text to uppercase for case-insensitivity
    morse_code = ''
    
    for char in text:
        if char in morse_code_dict:
            morse_code = morse_code + morse_code_dict[char] + ' '
    
    return morse_code

input_text = input("Enter a string: ")
morse_translation = morse(input_text)
print("Morse Code Translation:", morse_translation)
