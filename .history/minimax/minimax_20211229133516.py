
def minimax(self, state, turn : int):  
        
        if(self.isFinal(state)): 
            return self.utility(turn)
        
        if(turn == 1):
            score = -99999
            for s in self.getChildren(state): 
                score = max(score, self.minimax(s , 0))
            return score
        else: 
            score = 99999
            for s in self.getChildren(state):
                score = min(score, self.minimax(s , 1))
            
            return score


           
              
 
      

            





