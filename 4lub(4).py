imiona=(list(["Kasia", "Tomek", "Jan", "Ola", "Jerzy", "Marek", "Piotr",
"Zuzia", "Bartek", "Jacek"]))
imiona[-7]='Ostap'
imiona.insert(4,"Lia")
imiona.remove("Marek")
print(imiona)
print( )
x=str(input("Dodal Imie1:\n"))
z=str(input("Dodal Imie2:\n"))
c=str(input("Dodal Imie3:\n"))
imiona.insert(1,x)
imiona.insert(2,z)
imiona.insert(3,c)
imiona=(list(["Kasia", "Tomek", "Jan", "Ola", "Jerzy", "Marek", "Piotr",
"Zuzia", "Bartek", "Jacek"]))
print(imiona)