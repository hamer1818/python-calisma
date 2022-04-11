
eMail = str
while eMail != "kapat":
    print("programı kapatmak için kapat yaz")  #program düzgün çalışırsa kendi kapanıyor ama bir hata aldığında tekrar eposta istiyor
    eMail = str(input("e-mail adresi gir: "))
    etMail = eMail.find("@")
    noktaMail = eMail.find(".")
    boslukMail = eMail.find(" ")
    turkKarakterMail1 = eMail.find("ğ")
    turkKarakterMail2 =  eMail.find("ü")
    turkKarakterMail3 =  eMail.find("Ü")
    turkKarakterMail4 =  eMail.find("Ğ")
    turkKarakterMail5 = eMail.find("İ")
    turkKarakterMail6 =  eMail.find("Ş")
    turkKarakterMail7 =  eMail.find("ş")
    turkKarakterMail8 =  eMail.find("Ö")
    turkKarakterMail9 =  eMail.find("ö")
    turkKarakterMail10 =  eMail.find("Ç")
    turkKarakterMail11 =  eMail.find("ç")
    turkKarakterMail12 = eMail.find("ı")

    if etMail == -1:
        print("Lütfen \"@\" işareti ekleyiniz")
    elif noktaMail == -1:
        print("Lütfen Nokta ekleyiniz")
    elif boslukMail != -1:
        print("Lütfen Boşluk bırakmadan yazınız")
    elif turkKarakterMail1 != -1 or turkKarakterMail2 != -1 or turkKarakterMail3 != -1 or turkKarakterMail4 != -1 or turkKarakterMail5 != -1 or turkKarakterMail6 != -1 or turkKarakterMail7 != -1 or turkKarakterMail8 != -1 or turkKarakterMail9 != -1 or turkKarakterMail10 != -1 or turkKarakterMail11 != -1 or turkKarakterMail12 != -1:
        print("Lütfen Türkçe karakter kullanmayınız")
    else:
        break
print(f"İşlem  tamamlandı hata bulunamadı!!\nGirilen e-posta: {eMail}")

#Hamza ORTATEPE 90210000172