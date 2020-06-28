import random
Kelimeler = ["apple", "windows", "microsoft", "samsung", "tesla", "spacex", "nvidia", "intel", "siemens", "nokia",
         "oracle", "google", "lenovo", "monster", "amazon", "spotify", "aselsan", "roketsan", "casper", "pardus"]
         # Adam asmaca da bulunacak kelimeleri giriniz.

rastgele_secilen_kelime = random.choice(Kelimeler) # Random fonksiyonunu kullanarak rastgele bir kelime seçtik
tahmin_edilen_harfler = ["a", "b", "c", "d", "e", "f"]
alfabe = ("abcçdefgğhıijklmnoöpqrstuüvwxyz") # Alfabeniz de olan harfleri giriniz.
eklenecek_can = 5   # Rastgele seçilen kelimenin uzunluğu ve buraya yazılan sayının toplamı kullanıcının deneme sayısını belirliyor.                 

#   Rastgele seçilen kelimedeki harflerin hepsi bulunduğu zaman True
# değerini döndürerek kelimenin bulunduğunu kullanıcıya belirtilir.
def Kazanma_Kontrol(rastgele_secilen_kelime, tahmin_edilen_harfler):
    list = []
    sayac = -1
    for i in rastgele_secilen_kelime:
        list.append(i)
        sayac += 1
        if list[sayac] not in tahmin_edilen_harfler:
            return False
    return True

# Rastgele seçilen kelimenin harf uzunluğu alınarak adeti kadar "_" bastırıldı.
# Kullanıcının seçtiği harf rastgele seçilen kelimenin içinde var ise a değeri kullanıcının seçtiği harf ile değiştirildi.
def Kelime_Duzeltme(rastgele_secilen_kelime, tahmin_edilen_harfler):
    list = []
    sayac = -1
    for i in rastgele_secilen_kelime:
        list.append(i)
        sayac += 1
        if list[sayac] not in tahmin_edilen_harfler:
            list.pop(sayac)
            list.append("_ ")
    list = "".join(list)
    return list

# Bu fonksiyonda kullanılan harfler alfabe listesinden çıkarıldı.
def Alfabe_Yazdırma(tahmin_edilen_harfler):
    list = []
    sayac = -1
    for i in alfabe:
        list.append(i)
        sayac += 1
        if list[sayac] in tahmin_edilen_harfler:
            list[sayac] = ("")  # kullanılan harfin listede bulunduğu konumu belirleyip o değeri boşluk ile değiştirerek listeden kullanılan harf çıkartıldı.
    list = "".join(list)
    return list


def Oyun_Kontrol():
    can = eklenecek_can + len(rastgele_secilen_kelime)
    print("Adam Asmaca oyununa hoş geldiniz!")
    print(f"Kelimeniz {len(rastgele_secilen_kelime)} harflidir")
    print(f"{can} hakkınız kalmıştır")
    print("Kullanılabilen Harfler: abcçdefgğhıijklmnoöpqrstuüvwxyz")
    kullanılan_harfler = []
    tahmin_edilen_harfler = []
    kontrol = False
    while can > 0:
        can -= 1
        harf = input("Lütfen bir harf giriniz: ")
        tahmin_edilen_harfler.append(harf)
        Kelime_Duzeltme(rastgele_secilen_kelime, tahmin_edilen_harfler)
        print(f"\n{can} hakkınız kalmıştır")
        print("Kullanılabilen Harfler: " + Alfabe_Yazdırma(tahmin_edilen_harfler))

        if harf in rastgele_secilen_kelime and harf not in kullanılan_harfler:
            print("Doğru Tahmin: " + Kelime_Duzeltme(rastgele_secilen_kelime, tahmin_edilen_harfler))
            kullanılan_harfler.append(harf)

        elif harf in kullanılan_harfler:
            print("Üzgünüm! Bu harfi zaten kullanmıştın.")

        else:
            print("Yanlış Tahmin, Lütfen bir daha deneyin. " + Kelime_Duzeltme(rastgele_secilen_kelime, tahmin_edilen_harfler))
            kullanılan_harfler.append(harf)

        # Son hak ile oyun kazanılırsa oluşacak hata çözülmek için kontrol değişkeni atandı.
        if Kazanma_Kontrol(rastgele_secilen_kelime, tahmin_edilen_harfler) == True:
            print("Tebrikler, Kazandınız!")
            kontrol = True  
            break

    if can == 0 and kontrol == False:
        print("Kaybettiniz")
        print(f"Kelimeniz: {rastgele_secilen_kelime}")

Oyun_Kontrol()
