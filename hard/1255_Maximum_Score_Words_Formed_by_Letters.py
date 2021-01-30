class Solution(object):
    def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """
        self.history = {}
        wordscores=[]
        for item in words:
            cur_score=0
            for l in item:
                cur_score+=score[ord(l)-97]
            wordscores.append(cur_score)
        print(wordscores)
        return self.recursiveWord(words, letters, wordscores)
        
    def recursiveWord(self,words,letters,wordscores):
        inp = ('_'.join(words), '_'.join(letters))
        if inp in self.history:
            return self.history[inp]
        if len(words)==0 or len(letters)==0:
            self.history[inp] = 0
            return 0
        if(self.isAfford(words[0],letters)):
            temp1 = self.recursiveWord(words[1:],letters,wordscores[1:])
            #Delete the letters
            new_letters = [l for l in letters]
            for l in words[0]:
                new_letters.remove(l)
            temp2 = self.recursiveWord(words[1:],new_letters,wordscores[1:])
            self.history[inp] = max(temp1,temp2+wordscores[0])
            return self.history[inp]
            
        else:
            self.history[inp] = self.recursiveWord(words[1:],letters,wordscores[1:])
            return self.history[inp]
        
    def isAfford(self,word,letters):
        new_letters = [l for l in letters]
        for l in word:
            if l not in new_letters:
                return False
            else:
                new_letters.remove(l)
        return True
            
        
        
        