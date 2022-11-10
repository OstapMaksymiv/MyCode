
n=int(input("Ile studentow\n"))
t=n
s=0
while n>0:
    k=int(input("Wprowadz punkt\n"))
    s=s+k
    n-=1
print("Szrednie: ",s/t)