class test:
    def __init__(self):
        self.shap=list(map(str,input()))
    def check(self):
        if len(self.shap)==0:
            print(0)
        else:
            max_lenth=0
            res=[]
            for i in range(len(self.shap)):
                while self.shap[i] in res:
                    res.pop(0)
                res.append(self.shap[i])
                max_lenth=max(max_lenth,len(res))
            print(max_lenth)


a=test()
a.check()