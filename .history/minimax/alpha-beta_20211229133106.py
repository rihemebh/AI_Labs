 import copy


def getChildren(self, state : list): 
        result = []
        child = state
        for element in state: 
            if element>2:
                child.pop(child.index(element))
                for i in range(int(element/2)): 
                    if(element % 2 != 0 or (element % 2 == 0 and i+1 != element/2)):
                        child.append(i+1)
                        child.append(element-i-1)
                        result.append(copy.deepcopy(child))
                        child.pop()
                        child.pop() 
        return result



def isFinal(self,state: list): 
        b = True
        for i in state:
            if i > 2:
                b= False
                continue
        return b

def utility(turn):
        if(turn == 1 ):
            return -1
        return 1


def alphabeta(state, turn : int, alpha , beta ):  
        
        if(isFinal(state)): 
            return utility(turn)
        
        if(turn == 1):
            score = -99999
            for s in getChildren(state): 
                score = max(score, alphabeta(s , 0, alpha , beta))
                if (score >= beta): 
                    alpha = min(alpha,score)
            return score
        else: 
            score = 99999
            for s in getChildren(state):
                score = min(score, alphabeta(s , 1, alpha , beta))
            
            return score