class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen_state = dict()
        forward = False
        while n > 0:
            if not forward:
                state = tuple(cells)
                if state in seen_state:
                    n = n % (seen_state[state]-n)
                    forward = True 
                else:
                    seen_state[state] = n
            
            if n > 0:
                n -=1
                new = [0]
                for i in range(1,7):
                    new.append(int(cells[i-1] == cells[i+1]))
                new.append(0)
                cells = new 
                
            
        return cells
        