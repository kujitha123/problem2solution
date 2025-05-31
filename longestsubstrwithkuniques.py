##brute force solution###
def longestKSubstr(string,k):
        n=len(string)
        if(n==1):
            return 1
        maxLen=0
        dup=sorted(string)
        if(dup[0]==dup[n-1]):
            return -1
        if(len(set(dup))<k):
            return -1
        for i in range(0,n):
            s=set()
            for j in range(i,n):
                s.add(string[j])
                if(len(s)>k):
                    break
                maxLen=max(maxLen,j-i+1)
        return maxLen
string="aabacbebebe"
k=int(input())
print(longestKSubstr(string,k))

##optimal code(sliding window concept)##
def longestKSubstr(string,k):
        n=len(string)
        if(n==1):
            return 1
        dup=sorted(string)
        if(dup[0]==dup[n-1]):
            return -1
        if(len(set(dup))<k):
            return -1
        maxLen=0
        left=0
        right=0
        d={}
        while(right<n):
            if(string[right] in d):
                d[string[right]]+=1
            else:
                d[string[right]]=1
            if(len(d)>k):
                while(len(d)>k):
                    d[string[left]]-=1
                    if(d[string[left]]==0):
                        del d[string[left]]
                    left+=1
            maxLen=max(maxLen,right-left+1)
            right+=1
        return maxLen
string="aab"
k=int(input())
print(longestKSubstr(string,k))