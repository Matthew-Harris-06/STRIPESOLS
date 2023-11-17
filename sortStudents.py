def sortTheStudents(score, k):

        ans=[]
        dicc={}
        arr=[]

        for i in range(len(score)):
            arr.append(score[i][k])

        for j in range(len(score)):
            dicc[arr[j]]=score[j]

        for kk in sorted(dicc.keys(),reverse=True):
            ans.append(dicc[kk])
        
        return ans
