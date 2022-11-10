try:
  a=int(input("Podaj argument 1:"))
except:
    print("Podana wartosc nie jest liczba")
    exit()
try:
    b=int(input("Podaj argument 2:"))
except:
    print("Podana wartosc nie jest liczba")
    exit()

for x in range(a+1,b):
     print(x)
