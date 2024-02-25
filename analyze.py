from pathlib import Path
from common_functions import caesar_decrypt

INPUT_FILE = 'enc_out.txt'
CHARS_SORTED = 'etaoinshrdlcumwfgypbvkjxqz'


def analyze(text: str) -> list:
    frequencies = {}
    total_characters = 0

    # Count the frequency of each character
    for char in text:
        if char.isalpha():
            char = char.lower()
            frequencies[char] = frequencies.get(char, 0) + 1
            total_characters += 1

    # Calculate the percentage frequency
    percentage_frequencies = {char: count / total_characters * 100 for char, count in frequencies.items()}

    # Sort the results
    sorted_frequencies = sorted(percentage_frequencies.items(), key=lambda x: x[1], reverse=True)

    print(sorted_frequencies)

    return sorted_frequencies


def get_shift(char: str, text: str) -> None:
    for common_char in CHARS_SORTED:
        shift = ord(char) - ord(common_char)
        direction = 'right' if shift >= 0 else 'left'

        print('Shift: ', abs(shift), direction)

        print('Decoded phrase: ', caesar_decrypt(text, shift, direction))

        ans = input('Is this correct ? (y/n): ')

        if ans.lower() == 'y':
            print('Finished')
            return


def main() -> None:
    input_text = Path(INPUT_FILE).read_text()
    res = analyze(input_text)

    get_shift(res[0][0], input_text)


if __name__ == '__main__':
    main()
