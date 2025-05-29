#sieve of erotosthenes:- i and n//i are factors
#n=36
#1*36=36
#2*18=36
#3*12=36
#4*9=36
#6*6=36
#code:
def countPrimes(n):
        prime=[1]*n
        for i in range(2,int(n**0.5)+1):
            if(prime[i]==1):
                for j in range(i*i,n,i):
                    prime[j]=0
        count=0
        for i in range(2,n):
            if(prime[i]==1):
                count+=1
        return count
n=int(input())
print(countPrimes(n))
#aronomus functions in python are lamda functions like add=lamda x,y:x+y