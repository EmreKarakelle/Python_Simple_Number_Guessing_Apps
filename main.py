import random

rastgelesayi = random.randint(1,101)

for i in range(6,0,-1):
    sayin = int(input("{{{{""1 ile 100 arası sayı gir""}}}}"))
    if sayin <0:
        print("{{{{""Pozitif tam sayı gir!""}}}}")
        break
    if sayin >100:
        print("{{{{""100'den küçük sayı gir!""}}}}")
        break
    if sayin == 0:
        print("sıfır girme birader")
    if sayin == rastgelesayi:
        print("{{{{""heleşükür bildin""}}}}")
        break
    if sayin < rastgelesayi:
        print("{{{{""Biraz büyük sayı gir!", i, "hakkın kaldı""}}}}")
    if sayin > rastgelesayi:
        print("{{{{""Biraz küçük sayı gir", i, "hakkın kaldı""}}}}")
else:
    print("maalesef bulamadın!")