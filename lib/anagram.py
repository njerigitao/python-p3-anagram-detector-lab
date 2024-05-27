class Anagram:
    def _init_(self,word):
      self.word = word.lower()
      pass

    def match(self, possible_anagrams):
           matches = []
           for anagram in possible_anagrams:
               if self.is_anagram(anagram.lower()):
                   matches.append(anagram)
                   return matches
               
               def is_anagram(self, other_word):
                   if len(self.word) != len(other_word) or self.word == other_word:
                       return False
                   return sorted(self.word) == sorted(other_word)