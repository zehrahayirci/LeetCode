class Solution:
   
    
    #MAP={2:["a","b","c"],3:["d","e","f"],4["g","h","i"],5:["j","k","l"],6:["m","n","o"],7:["p","q","r","s"],8:["t","u","v"],9:["w","x","y","z"]}
        
    def letterCombinations(self, digits: str) -> List[str]:
        MAP={2:["a","b","c"],3:["d","e","f"],4:["g","h","i"],5:["j","k","l"],6:["m","n","o"],7:["p","q","r","s"],8:["t","u","v"],9:["w","x","y","z"]}
        
        s =[]
        a = []
        if digits == "":
            return a
        for digit in digits:
            s.append(MAP[int(digit)])
        #print(s)
        #print(list(itertools.product(*s)))
        for tup in list(itertools.product(*s)):
            st =  ''.join(tup)
            a.append(st)
        return a