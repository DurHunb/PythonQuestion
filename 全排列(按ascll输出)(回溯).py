class test:
    def __init__(self):
        self.shap=list(map(str,input().replace(' ','')))
        self.res=[]
    def check(self,first=0):
        if len(self.shap)==0:
            return []
        if first==len(self.shap):
            self.res.append(self.shap[:])
        for i in range(first,len(self.shap)):
            self.shap[first],self.shap[i]=self.shap[i],self.shap[first]
            self.check(first+1)
            self.shap[first], self.shap[i] = self.shap[i],self.shap[first]
        return self.res
    def prin(self,shap):
        shap.sort(key= lambda x:x[0])
        for i in shap:
            res=''
            for j in range(len(i)):
                res=res+' '+i[j]
            print(res.strip())


a=test()
shap=a.check()
a.prin(shap)
