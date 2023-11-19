def foxsol(distance):
    distance = distance
    steps = 0
    for x in range(5,0,-1):
        
        steps += distance // x
        distance -= (distance // x)* x
        
    return steps   
                
                
            
