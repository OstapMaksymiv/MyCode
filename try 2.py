x=int(input("Wprowadz wartosc studentuw:\n"))
t=x
s=0
while x>0:
    k=int(input("wprowadz ocene"))
    s=s+k
    x-=1
print("srednie aref",s/t)