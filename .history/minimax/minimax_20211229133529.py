
def minimax( state, turn : int):  
        
        if(isFinal(state)): 
            return utility(turn)
        
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


           
              
 
      

            





