class LetterIter:
    def __init__(self, start = 'a', end = 'e'):
        self.cur_letter = start
        self.start = start
        self.end = end
    def __next__(self):
        if self.cur_letter == self.end:
            self.cur_letter = self.start
        letter = self.cur_letter
        self.cur_letter = chr(ord(self.cur_letter) + 1)
        return letter

class Letters:
    def __init__(self, start = 'a', end = 'e'):
        self.cur_letter = start
        self.start = start
        self.end = end
    def __iter__(self):
        return LetterIter(self.start, self.end)

class LettersWithYield:
    def __init__(self, start = 'a', end = 'e'):
        self.start = start
        self.end = end
    def __iter__(self):
        cur_letter = self.start
        while cur_letter < self.end:
            yield cur_letter
            cur_letter = chr(ord(cur_letter) + 1)
