yuan = int(input("Qué cantidad de yuan tienes:"))
yen = int(input("Qué cantidad de yen tienes:"))
won = int(input("Qué cantidad de won tienes:"))

USDtoYuan = yuan*0.14734
USDtoYen = yen*0.00778
USDtoWon = won*0.00081

USD = USDtoYuan+USDtoYen+USDtoWon

print(USD)