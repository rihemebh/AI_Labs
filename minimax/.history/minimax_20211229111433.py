from abc import get_cache_token
from typing import List
import copy

class Game : 
    state = ([],0)
    tuples = []
    def __init__(self, state):
        self.state = state
        
  
    def getChildren(self, state : List): 
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

    def utility(self,turn):
        if(turn == 1 ):
            return -1
        return 1


    def minimax(self, state, turn : int):  
        
        if(self.isFinal(state)): 
            return self.utility(turn)
        
        if(turn == 1):
            score = -99999
            for s in self.getChildren(state):
                print(s)
                score = max(score, self.minimax(s , 0))
            print(score)
            return score
        else: 
            score = 99999
            for s in self.getChildren(state):
                print(s)
                score = min(score, self.minimax(s , 1))
            print(score)
            return score


           
              
 
      

            





