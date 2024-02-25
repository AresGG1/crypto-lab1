from pathlib import Path

LETTERS_IN_ALPHABET = 26
UPPERCASE_STARTS_FROM = 65
LOWERCASE_STARTS_FROM = 97


def caesar_encrypt(text: str, shift: int, direction: str) -> str:
    encrypted_text = ""

    # Reverse shift in case left direction
    shift = shift if direction == 'right' else shift * -1
    for char in text:

        if not char.isalpha():
            encrypted_text += char
            continue

        start_from = UPPERCASE_STARTS_FROM if char.isupper() else LOWERCASE_STARTS_FROM

        encrypted_text += make_shift(shift, start_from, char)

    return encrypted_text


def make_shift(shift_value: int, start_from: int, char: str) -> str:
    return chr((ord(char) - start_from + shift_value) % LETTERS_IN_ALPHABET + start_from)


def caesar_decrypt(encrypted_text: str, shift: int, direction: str) -> str:
    if direction == 'right':
        reverse_direction = 'left'
    elif direction == 'left':
        reverse_direction = 'right'

    decrypted_text = caesar_encrypt(encrypted_text, shift, reverse_direction)
    return decrypted_text


def handle_io(input_file: str, output_file: str, action: callable) -> None:
    shift = int(input('Enter shift\n'))
    direction = input('Enter direction left or right\n')

    text = Path(input_file).read_text()
    decrypted = action(text, shift, direction)

    Path(output_file).write_text(decrypted)
