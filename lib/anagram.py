# your code goes here!
# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # lowercase to avoid case mismatch

    def match(self, words):
        matches = []
        for candidate in words:
            if candidate.lower() != self.word:  # avoid identical match
                if sorted(candidate.lower()) == sorted(self.word):
                    matches.append(candidate)
        return matches
