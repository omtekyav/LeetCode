import time

def zaman_hesapla(fonk):
    #icine bir fonksiyon alıyor 
    def wrapper(*args,**kwargs):
        #burası içerdeki fonksiyonun kareleri al veya küpleri al fonksiyonun calışacağı yer parametetleri
        #bilemedigimiz icin *args ve ** args ekliyoruz 
        baslangic  = time.time()
        sonuc = fonk(*args,**kwargs)
        bitis = time.time()
        print(f"islem {bitis - baslangic}saniye sürdü.")
        return sonuc
    return wrapper

#wrapper oldugu durumda sonuc elde etmek icin sonuc'u return etmek gerekiyor yoksa print edilmiyor
#def kareleri hesapla dendiği zaman wrapper paramtetre olarak fonk aldığı icin hangisiyse ona gidior



@zaman_hesapla
def kareleri_al(liste):
    sonuc = []
    for i in liste:
        sonuc.append(i * i )
    return sonuc

@zaman_hesapla
def kupleri_al(liste):
    sonuc = []
    for i in liste:
        sonuc.append(i **3)
    return sonuc

@zaman_hesapla
def topla(*args):
    time.sleep(1)
    return sum(args)


print(kupleri_al(range(20)))