class Solution:#动态规划
    def trap(self, height) :
        n=len(height)
        if n<2: return 0
        maxleft=[0]*n
        maxright=[0]*n
        maxleft[0]=height[0]
        maxright[n-1]=height[n-1]
        for i in range(1,n):
            maxleft[i]=max(maxleft[i-1],height[i])
        for i in range(n-2,-1,-1):
            maxright[i]=max(maxright[i+1],height[i])
        res=0
        for i in range(n):
            if height[i]<min(maxleft[i],maxright[i]):
                res+=min(maxleft[i],maxright[i])-height[i]
        return res