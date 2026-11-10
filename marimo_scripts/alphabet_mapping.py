import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium", auto_download=["html"])

@app.cell
def _():
    import string
    # 1. Generate the encoding dictionary!
    def generate_alphabet_dicts():
        # Lowercase alphabet (a-z) -> digits [11,36]
        int_to_letter = {}
        letter_to_int = {}

        encode = 11
        for letter in string.ascii_lowercase:
            int_to_letter[encode] = letter
            letter_to_int[letter] = encode
            encode += 1

        letter_to_int[' '] = encode
        int_to_letter[encode] = ' '

        return letter_to_int, int_to_letter

    letter_to_int, int_to_letter = generate_alphabet_dicts()
    print(letter_to_int)
    print(int_to_letter)
    return