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

for num in range(a+1,b):
    if num > 1:
        for i in range(2, num):
            if num % i == 1:
                break

        else:
            print(num)
