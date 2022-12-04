import random

x = 1
y = 100


guess = int(input("1 ile 100 arasında sayı yaz! : "))


for i in range(10,0,-1):
    cpurandom = random.randint(x,y)
    if cpurandom == guess:
        print("Tuttuğun sayı : " , cpurandom, " kazandım").__format__.__module__
        break
    elif cpurandom != guess:
        print("Tuttuğun sayı : ",cpurandom,"||",">>>", i, "<<<", " hakkın kaldı")
        
    kucukbuyuk = input("Yazdığın sayı küçük mü büyük mü? (k?,b?) : ") 
    if kucukbuyuk == "k":
        y = cpurandom
        cpurandom > y
        continue
    if kucukbuyuk == "b":
        x = cpurandom    
        cpurandom < x
    continue
