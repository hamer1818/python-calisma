def sag(adet):
    for a in range(int(adet)):
        print("/",end="")
def sol(adet):
    for a in range(int(adet)):
        print("\\",end="")
def bosluk(adet):
    for a in range(int(adet)):
        print(" ",end="")
def atla(adet):
    for a in range(int(adet)):
        print()
def ust(cap):
    baslangic = cap/2-1
    for a in range(int(cap/2)):
        bosluk(baslangic-a)
        sag(1)
        bosluk(a*2)
        sol(1)
        atla(1)
def alt(cap):
    baslangic = cap-2
    for a in range(int(cap/2)):
        bosluk(a)
        sol(1)
        bosluk(baslangic-2*a)
        sag(1)
        atla(1)

def paralel(deger):
    ust(deger)
    alt(deger)
buyukluk = int(input("yarıçap gir:\t"))
if buyukluk%2==0 and buyukluk>=0:
    while buyukluk!=1:
        buyukluk = int(input("yarıçap gir:\t"))
        print()
        paralel(buyukluk)
else:
    print("lütfen tek sayı veya negatif sayı(sıfır dahil) girmeyiniz!!!")