lower,upper=map(int,raw_input().split())
count=0
for n in range(lower,upper+1):
    if n>1:
        for i in range(2,n):
            if(n%i)==0:
                break
        else:
            count=count+1
print count            
