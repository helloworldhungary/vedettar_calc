aktualis = float(input("Aktuális benzin ár? "))
tank = float(input("Mennyiért szeretnél védett áron tankolni? "))

liter = tank / 595
normal = liter * aktualis

print(round(liter, 2),"liter üzemanyag.")
print("Védett ár:",round(tank),"Ft")
print("Normál ár:",round(normal),"Ft")