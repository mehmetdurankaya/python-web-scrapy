def not_hesapla(satir):
    satir=satir[:-1]
    liste=satir.split(":")
    ogrenciAdi=liste[0]
    notlar=liste[1].split(",")


    not1=notlar[0]
    not2=notlar[1]
    not3=notlar[2]

    ortalama=(int(not1)+int(not2)+int(not3))/3

    if ortalama>90 and ortalama<=100:
        harf="AA"
    elif ortalama>=85 and ortalama<=89:
        harf="BA"
    elif ortalama>=65:
        harf="BB"
    elif ortalama>=55:
        harf="CB"
    elif ortalama>=45:
        harf="CC"
    elif ortalama>=40:
        harf="DC"
    else:
        harf="FF"
    return ogrenciAdi+ " : "+ harf + "\n"

def ortalamalari_Oku():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))       
 
def not_gir():
    ad=input("Öğrenci Adı: ")
    soyad=input("Öğrenci Soyadı: ")
    not1=input("not 1: ")
    not2=input("not 2: ")
    not3=input("not 3: ")
    
    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
        file.write(ad+" "+soyad+": "+not1+", "+not2+", "+not3+"\n")
def notlari_kaydet():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        liste=[]
        for i in file:
            liste.append(not_hesapla(i))
        with open("sonuclar.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)



while True:
    islem=input(" 1- Notları Oku\n 2- Not Gir \n 3- Notları Kaydet\n 4- Çıkış\n ")
    if islem=="1":
        ortalamalari_Oku()
        
    elif islem=="2":
        not_gir()
        

    elif islem=="3":
        notlari_kaydet()
           
    else:
        break