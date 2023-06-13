import pandas as pd2

def üye_ol():
 ad = input("Adınızı girin: ")
 soyad = input("Soyadınızı girin: ")
 sifre = input("Şifrenizi girin: ")
 print("Üyeliğiniz başarıyla gerçekleşmiştir...")
 
 uye = {"Ad": ad, "Soyad": soyad, "Sifre": sifre}
 df = pd2.DataFrame([uye])
 df.to_excel("uyeler.xlsx", index=False) 

  
def giris():
    print("Kullanıcı paneline hoş geldiniz...")
    input("Adınızı giriniz: ")
    input("Soyadınızı girin: ")
    input("Şifrenizi giriniz: ")
    input("1.Gaziantep\n2.Kahramanmaraş\n3.Hatay\n4.Adana\n5.Diyarbakır\nİlinizi giriniz: ")            
    print("Bulunduğunuz ildeki yardım yoğunluğunun olduğu ilçeler listelenmiştir...\n ")
   
    #pandas kütüphanesi yardımıyla gerekli ihtiyaçların olduğu excel tablomu okuttum:
    import pandas as pd
    df = pd.read_excel('ihtiyaç.xlsx')
    print(df)
    
    
def admin_paneli():
    print("Admin paneline erişiminiz maalesef yoktur...")
    print("Kullanıcı paneline yönlendiriliyosunuz.")


print("                                Merhabalar Hoşgeldiniz                       ")    

print("****Öncelikle bölgenizde yaşanan felaket dolayısıyla geçmiş olsun diliyoruz...****")

print("Lütfen kullanıcı tipinizi seçin:")
print("1. Admin")
print("2. Kullanıcı")
    
secim = input("Seçiminizi yapın (1 veya 2): ")
    
if secim == "1":
      admin_paneli()
elif secim == "2":
      giris()
else:
      print("Geçersiz seçim. Lütfen tekrar deneyin.")
      

# Seçeneklerin listesi
menu1 = ["1-Sisteme Üye Ol", "2-Sisteme Giriş Yap", "3-Sistemden Çıkış Yap"]

while True:
    for option in menu1:
        print(option)
    
    try:
        seçim = int(input("Kullanıcı seçiminizi yapın (1-3): "))
        
        if seçim == 1:
            print("Sisteme üye ol seçeneği seçildi.")    
            üye_ol() 
            
        elif seçim == 2:
            print("Sisteme giriş yap seçeneği seçildi.")
            giris()
          
    
        elif seçim == 3:
            print("Sistemden çıkış yap seçeneği seçildi. Program sonlandırılıyor...")
            break
        
        else:
            print("Geçersiz seçenek seçildi! Lütfen tekrar deneyin.")
        
            
            
    except ValueError:
        #Girilen değer sayı değilse hata mesajı verir
       print("Lütfen bir sayı girin!")        
