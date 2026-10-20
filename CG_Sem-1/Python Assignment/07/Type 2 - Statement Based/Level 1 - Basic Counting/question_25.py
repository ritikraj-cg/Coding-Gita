k=int(input("enter k: "))
n=int(input("enter n: "))
i=1
if k>0 and n > 0:
    while i*k <= n:
        print(f"{k}*{i} = {k*i}")
        i += 1
        
        