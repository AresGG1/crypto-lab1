from pathlib import Path

INPUT_FILE = 'enc_out.txt'


def analyze(text: str):
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


def get_shift(char: str):
    most_common_char = 'e'

    shift = ord(char) - ord(most_common_char)

    direction = 'right' if shift >= 0 else 'left'

    print('Shift: ', abs(shift), direction)


def main():
    input_text = Path(INPUT_FILE).read_text()
    res = analyze(input_text)

    get_shift(res[0][0])


if __name__ == '__main__':
    main()
