kitapListesi = list()
yazarListesi = list()
menu = """
1) Kitap ekle
2) Kitap çıkar
3) Eklenen kitapları göster
Q) Çıkış
"""
def kitapEkle(liste,kitapAdi,yazarListe,yazar):
    
    liste += [kitapAdi]
    yazarListe += [yazar]
    
    print("Kitap ekleme işlemi başarıyal tamamlanmıştır\t")
    input("Ana menüye dönmek için Enter'a basınız\t")
def kitapCikar():
    
    pass
def kitapGoster(liste,yListe,b=0):
    for a in liste:
        print("Kitap ismi\t",5*">",a,"\tYazar adı:",yListe[b])
        b+=1

    input()
    input("Ana menüye dönmek için Enter'a basınız")
def cikis():
    quit()
while True:
    print(menu)
    secim = input("Lütfen seçim yapınız\t")
    if secim=="1":
        print("Kitap adını giriniz\t")
        kitapAdi=input(5*">\t")
        print("Yazar adını giriniz\t")
        yazarAdi=input(5*">\t")
        kitapEkle(kitapListesi,kitapAdi,yazarListesi,yazarAdi)
    elif secim=="2":
        kitapCikar()
    elif secim=="3":
        kitapGoster(kitapListesi,yazarListesi,b=0)
    elif secim=="Q" or secim=="q":
        cikis()
    else:
        print("Yanlış giriş yaptınız\t")
        input()
        print("Ana menüye yönlendiriliyorsunuz!!\t")
