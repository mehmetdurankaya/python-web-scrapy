import os
import datetime

result = dir(os)
result=os.name
#Dizin değiştirme
# os.chdir("c:\\")
# os.chdir("..") # Bir üst klasöre geç
# os.chdir("../..") # iki üst klasöre geç
# Dizin öğrenme
# result=os.getcwd()
# Klasör oluturma
# os.mkdir("newdirectory")
# os.makedirs("newdirectory/yeniklasör")

# result = os.listdir()
# result = os.listdir("c:\\")

# for dosya in os.listdir():
#     if dosya.endswith(".py"):
#         print(dosya)
result = os.stat("_datetime.py")
# result= result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime) # create time   ctime  oluşturulma tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime) # axess time    atime  son erişilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime) # modified time mtime  değiştirilme tarihi

# os.rename("newdirectory","yeniklasör")
# os.rmdir("../newdirectory")
# os.removedirs("../yeniklasör/yeni")

# path
result = os.path.abspath("__os.py")
result= os.path.dirname("C:/Users/PC/Desktop/pyton-web/osmoduls/__os.py")
result= os.path.dirname(os.path.abspath("__os.py"))
result= os.path.exists("C:/Users/PC/Desktop/pyton-web/osmoduls/__os1.py")
result= os.path.exists("C:/Users/PC/Desktop/pyton-web/osmoduls")
result= os.path.isdir("C:/Users/PC/Desktop/pyton-web/osmoduls")
result= os.path.isfile("C:/Users/PC/Desktop/pyton-web/osmoduls/os_modulu.py")
result= os.path.join("c:\\","deneme","deneme1")
result = os.path.split("c:\\deneme")
result = os.path.splitext("__os.py")
# result = result[0]
result = result[1]

print(result)