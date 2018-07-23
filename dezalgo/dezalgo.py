import unicodedata

class Dezalgo:
    def __init__(self, text=None):
        self.text = text
        self.__call__()
        self.worked = True

    def __call__(self):
        assert self.text is not None, "We need Zalgo Text!!!"
        self.plain = ""
        self.unicode = ""
        for character in self.text:
            if unicodedata.combining(character) == 0:
                self.plain += character
            else:
                self.unicode += character
        return self.plain
