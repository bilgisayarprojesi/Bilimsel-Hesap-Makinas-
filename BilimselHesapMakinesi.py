import math

print("**********************************************\n"
      "BİLİMSEL HESAP MAKİNESİ PROGRAMI \n"
      "İŞLEMLER\n"
      "1.  İşlem = Toplama(x,y)\n"
      "2.  İşlem = Çıkarma(x,y) \n"
      "3.  İşlem = Çarpma(x,y) \n"
      "4.  İşlem = Bölme(x,y) \n"
      "5.  İşlem = Üssünü Alma(x,y) \n"
      "6.  İşlem = tan(x) \n"
      "7.  İşlem = Sin(x)\n"
      "8.  İşlem = Cos(x) \n"
      "9.  İşlem = Faktoriyel(x) \n"
      "10. İşlem = Log(x) \n"
      "11. İşlem = Karekök(x) \n"
      "12. İşlem = ln(x) \n"
      "13. İşlem = 1/(x) \n"
      "14. İşlem = Deg(x)\n"
      "15. İşlem = Rad(x)\n"
      "**********************************************\n ")
ts = 0
cs = 0
c2 = 0
b = 0
u = 0
t = 0
s = 0
c = 0
f = 0
l = 0
k = 0
ln = 0
b2 = 0
d = 0
r = 0
while True:

    islem = input("Hangi İşlemi Yapmak İstediğiniiz Seçiniz:")
    if islem == "1":
        ts += 1
        x = int(input("Toplama İşlemi İçin Birinci Sayıyı Giriniz:"))
        y = int(input("Toplama İşlemi İçin İkinci Sayıyı Giriniz:"))
        print("Sonucunuz:", x + y)
        if (ts >= 2):
            print(str(ts), " .kez Toplama işlemi yaptınız")

    elif islem == "2":
        cs += 1
        x = int(input("Çıkarma İşlemi İçin Birinci Sayıyı Giriniz:"))
        y = int(input("Çıkarma İşlemi İçin İkinci Sayıyı Giriniz:"))
        print("Sonucunuz:", x - y)
        if (cs >= 2):
            print(str(cs), " .kez Çıkarma işlemi yaptınız")
    elif islem == "3":
        c2 += 1
        x = int(input("Çarpma İşlemi İçin Birinci Sayıyı Giriniz:"))
        y = int(input("Çarpma İşlemi İçin İkinci Sayıyı Giriniz:"))
        print("Sonucunuz:", x * y)
        if (c2 >= 2):
            print(str(c2), " .kez Çarpma işlemi yaptınız")
    elif islem == "4":
        b += 1
        x = int(input("Bölme İşlemi İçin Birinci Sayıyı Giriniz:"))
        y = int(input("Bölme İşlemi İçin İkinci Sayıyı Giriniz:"))

        print("Sonucunuz:", x / y)
        if (b >= 2):
            print(str(b), " .kez Bölme işlemi yaptınız")
    elif islem == "5":
        u += 1
        x = int(input("Üs Alma İşlemi İçin Birinci Sayıyı Giriniz:"))
        y = int(input("Üs Alma İşlemi İçin İkinci Sayıyı Giriniz:"))

        print("Sonucunuz:", x ** y)
        if (ts >= 2):
            print(str(u), " .kez Üs işlemi yaptınız")
    elif islem == "6":
        t += 1
        x = int(input("Sayıyı Giriniz:"))
        print("Sonucunuz:", math.tan(x))
        if (t >= 2):
            print(str(t), " .kez Tanjant işlemi yaptınız")
    elif islem == "7":
        s += 1
        x = int(input("Sayıyı Giriniz:"))
        print("Sonucunuz:", math.sin(x))
        if (s >= 2):
            print(str(s), " .kez Sinüs işlemi yaptınız")
    elif islem == "8":
        c += 1
        x = int(input("Sayıyı Giriniz:"))
        print("Sonucunuz:", math.cos(x))

        if (c >= 2):
            print(str(c), " .kez Cosinüs işlemi yaptınız")
    elif islem == "9":
        f += 1
        x = int(input("Sayıyı Giriniz:"))
        print("Sonucunuz:", math.factorial(x))

        if (f >= 2):
            print(str(f), " .kez Faktöriyel işlemi yaptınız")
    elif islem == "10":
        l += 1
        x = int(input("Sayıyı Giriniz:"))
        print("Sonucunuz:", math.log10(x))

        if (l >= 2):
            print(str(l), " .kez Logaritma işlemi yaptınız")
    elif islem == "11":
        k += 1
        x = int(input("Sayıyı Giriniz:"))
        print("Sonucunuz:", math.sqrt(x))

        if (k >= 2):
            print(str(k), " .kez karekök işlemi yaptınız")
    elif islem == "12":
        ln += 1
        x = int(input("Sayıyı Giriniz:"))
        print("Sonucunuz:", math.log(x))

        if (ln >= 2):
            print(str(ln), " .kez ln işlemi yaptınız")
    elif islem == "13":
        b2 += 1
        x = int(input("Sayıyı Giriniz:"))
        print("Sonucunuz:", x ** -1)

        if (b2 >= 2):
            print(str(b2), " .kez 1/x işlemi yaptınız")
    elif islem == "14":
        d += 1
        x = int(input("Sayıyı Giriniz:"))
        print("Sonucunuz:", math.degrees(x))

        if (d >= 2):
            print(str(d), " .kez derece işlemi yaptınız")
    elif islem == "15":
        r += 1
        x = int(input("Sayıyı Giriniz:"))
        print("Sonucunuz:", math.radians(x))

        if (r >= 2):
            print(str(r), " .kez Radiant işlemi yaptınız")
    elif islem == "Çıkış":
        break
    else:
        print(" \n Geçersiz İşlem Tekrar Deneyin.")

