import string
from pathlib import Path
from typing import Dict
import random

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


def map_to_numbers(text: str, table: Dict) -> str:
    output = ''

    for char in text:
        output += str(table.get(char))
        output += ' '

    return output


def map_to_chars(numbers: str, table: Dict) -> str:
    res = ''

    numbers_array = numbers.split(' ')

    for num in numbers_array:
        res += table.get(int(num))

    return res


def swap_table(table: Dict[str, int]) -> Dict[int, str]:
    return {value: key for key, value in table.items()}


def generate_table() -> Dict[str, int]:
    chars = list(string.ascii_uppercase + ' ')
    numbers = [i for i in range(0, len(chars))]
    random.shuffle(numbers)

    return dict(zip(chars, numbers))


def handle_io(input_file: str, output_file: str) -> None:
    shift = int(input('Enter shift\n'))
    direction = input('Enter direction left or right\n')

    text = Path(input_file).read_text()
    text = text.upper()

    # caesar
    processed: str = caesar_encrypt(text, shift, direction)

    table = generate_table()

    processed = map_to_numbers(processed, table)
    processed = 'processed ' + processed.upper()

    processed += f"\nshift {shift}"
    processed += f"\ndirection {direction}"
    processed += f"\ntable " + ','.join([f"{key}:{value}" for key, value in table.items()])

    Path(output_file).write_text(processed)

    print(generate_table())
