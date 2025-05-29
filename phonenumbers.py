def generate(ind,curr,ans,digits,combos):
    if(ind==len(digits)):
        ans.append(curr)
        return
    i=int(digits[ind])
    for j in combos[i]:
        generate(ind+1,curr+j,ans,digits,combos)
def letterCombinations(digits: str):
    if(len(digits)==0):
        return []
    ind=0
    curr=""
    ans=[]
    combos=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    generate(ind,curr,ans,digits,combos)
    return ans
digits=input()
print(letterCombinations(digits))
