#  Dosya Açmak ve oluşturmak için open() fonksiyonu kullanılır.
#  Kullanımı: open(dosya_adi,dosya_erişim_modu)
#  dosya_erişim_modu => dosyayı hangi amaçla açtığımızı belirtir
#  "w" : (Write) yazma modu. Dosyayı konumda oluşturur.
#       ** Dosyayı konumda oluşturur. 
#       ** Eski dosya varsa içeriği siler ve uzerine yeniden ekleme yapar.
# file=open("newfile.txt","w",encoding="utf-8")
# file.write("Mehmet Duran Kaya")
# file.close()

#  "a" : (Append) ekleme modu. Dosya konumda yoksa oluşturur.

# file=open("newfile.txt","a",encoding="utf-8")
# file.write("\nNizamettin Kaya\n")
# file.close()



#  "x" : (Create) oluşturma. Dosya zaten varsa hata verir.

# file=open("newfile2.txt","x",encoding="utf-8")


#  "r" : (Read) okuma modu. Varsayılan moddur. Dosya konumda yoksa hata verir.

# try:
#     file=open("newfile.txt","r",encoding="utf-8")
#     print(file)
# except FileNotFoundError:
#     print("dosya okunamadı")
# finally:
#     print("dosya kapandı")
#     file.close()

# file=open("newfile.txt","r",encoding="utf-8")
# #for döngüsü
# # for i in file:
# #     print(i, end="")

# #read() fonksiyonu
# content=file.read()

# print("içerik 1")
# print(content)

# content2=file.read()
# print("içerik 2")
# print(content2)

# file.close()
# ******* readline() *******************
# print(file.readline(),end="")
# file.close()
# file=open("newfile.txt","w")
# file.close(file)

# with open("newfile.txt","r",encoding="utf-8") as file:
with open("newfile.txt","r",encoding="utf-8") as file:
    content=file.read(10)
    print(content)
    file.seek(0)
    print(file.tell())
    content2=file.read()
    print(content2)





