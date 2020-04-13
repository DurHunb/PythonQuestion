class test:
    def __init__(self):
        self.shap=list(map(int,input().split(' ')))
        print('shap',self.shap)
    def check(self):
        n=len(self.shap)
        res=0
        dix=dict()
        for i in range(n):
            if self.shap[i] in dix:
                dix[self.shap[i]]+=1
            else:
                dix[self.shap[i]]=1
        shap1=list(set(self.shap))
        print('shap1',shap1)
        print('dix',dix)
        for i in range(len(shap1)):
            a=dix[shap1[i]]%(shap1[i]+1)
            b=dix[shap1[i]]//(shap1[i]+1)
            if a:
                res=res+b*(shap1[i]+1)+shap1[i]+1
            else:
                res+=b*(shap1[i]+1)
        print(res)
a=test()
a.check()