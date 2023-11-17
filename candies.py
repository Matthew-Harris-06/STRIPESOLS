def kidsWithCandies(candies, extraCandies):
        
        max = 0
        for int in candies:
            if(int > max):
                max = int
        answer = []
        for candy in candies:
           
            if(candy + extraCandies >= max):
                
                answer.append(True)
            else:
                answer.append(False)
        
        return answer
print(kidsWithCandies([2,5,3,2,1], 7))
