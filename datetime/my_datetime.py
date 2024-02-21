from datetime import datetime
from datetime import timedelta


simdi=datetime.now()

result=datetime.today()

result=simdi.year

result=simdi.month

result=simdi.day
result=simdi.hour
result=simdi.minute
result=simdi.second


result= datetime.ctime(simdi)
result= datetime.strftime(simdi,'%Y')#yıl bilgisi
result= datetime.strftime(simdi,'%X')#saat bilgisi
result= datetime.strftime(simdi,'%d')#gün bilgisi
result= datetime.strftime(simdi,'%A')#gün bilgisi string olarak verilir
result= datetime.strftime(simdi,'%B')#ay bilgisi string olarak verilir
result= datetime.strftime(simdi,'%Y,%B,%A')

t = "06 February 2023 hour 04:17:00"
result = datetime.strptime(t,"%d %B %Y hour %H:%M:%S")
result=result.year
birthday = datetime(1977,6,13,5,30)
result=datetime.timestamp(birthday)#zaman bilgisi saniye cinsinden gelir
result=datetime.fromtimestamp(result)#saniyeyi datetime bilgisine çevirir
result= datetime.fromtimestamp(0)# 1970 baz alınır
result=simdi - birthday # iki tarih arası hesaplandığında timedelta öğesi geliyor
#result= result.days
#result= result.seconds
# result = result.microseconds
print(simdi)
# result = simdi + timedelta(days=10)
# result = simdi + timedelta(days=730,minutes = 10)
result = simdi - timedelta(days=10)
print(result)







