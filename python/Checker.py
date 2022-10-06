#  Word Class

class Checker:
    def __init__(self, word):
        self.word = word

    def getWord(self):
        return self.word

    def setWord(self, word):
        self.word = word

    def getWordLength(self):
        return len(self.word)
    
    def getWordLetters(self):
        return list(self.word)
    
    def getWordLettersSet(self):
        return set(self.word)
    
    def getWordLettersSetLength(self):
        return len(set(self.word))
    
    # Get all accents from word
    def getWordAccents(self):
        accents = []
        for letter in self.word:
            if letter in 'àâäéèêëîïôöùûüç':
                accents.append(letter)
        return accents

    # Verify if word contains accents
    def hasAccents(self):
        return len(self.getWordAccents()) > 0