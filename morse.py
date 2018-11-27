# morse.py
# pylint: disable=missing-docstring


class Morse:
    ALPHABET = {
        ".-": "A",
        "-...": "B",
        "-.-.": "C",
        "-..": "D",
        ".": "E",
        "..-.": "F",
        "--.": "G",
        "....": "H",
        "..": "I",
        ".---": "J",
        "-.-": "K",
        ".-..": "L",
        "--": "M",
        "-.": "N",
        "---": "O",
        ".--.": "P",
        "--.-": "Q",
        ".-.": "R",
        "...": "S",
        "-": "T",
        "..-": "U",
        "...-": "V",
        ".--": "W",
        "-..-": "X",
        "-.--": "Y",
        "--..": "Z",
        "/": " "
    }

    def decode(self, message):
        return_string = ""
        letter_list = message.split(" ")
        try:
            for letter in letter_list:
                print(letter)
                return_string += self.ALPHABET[letter]
        except KeyError:
            return ""
        return return_string


# if __name__ == "__main__":
#     print(Morse().decode(".-"))
