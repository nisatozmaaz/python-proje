def üye_ol():
    input("Kullanıcı adı oluşturunuz: ")
    input("Şifre oluşturunuz: ")
    print("Üyeliğiniz başarıyla oluşturulmuştur...\n")
    
    
def giriş_yap():
    input("Kullanıcı adınızı giriniz: ")
    input("Şifrenizi giriniz: ")
    input("1.Gaziantep\n2.Kahramanmaraş\n3.Hatay\n4.Adana\n5.Diyarbakır\nİlinizi giriniz: ")            
    print("Bulunduğunuz ildeki yardım yoğunluğunun olduğu ilçeler listelenmiştir...\n ")
    
    #pandas kütüphanesi yardımıyla gerekli ihtiyaçların olduğu excel tablomu okuttum:
    import pandas as pd
    df = pd.read_excel('ihtiyaç.xlsx')
    print(df)
    
    
def şifre_değişimi():
    input("Lütfen eski şifrenizi giriniz: ")
    input("Lütfen yeni şifrenizi giriniz: ")
    print("Şifreniz başarıyla değiştirilmiştir...\n")
    



print("                                Merhabalar Hoşgeldiniz                       ")    
print("****Öncelikle bölgenizde yaşanan felaket dolayısıyla geçmiş olsun diliyoruz...****")

# Seçeneklerin listesi
menu = ["1-Sisteme Üye Ol", "2-Sisteme Giriş Yap", "3-Şifremi Değiştirme", "4-Sistemden Çıkış Yap"]

while True:
    for option in menu:
        print(option)
    
    try:
        seçim = int(input("Seçiminizi yapın (1-4): "))
        
        if seçim == 1:
            print("Sisteme üye ol seçeneği seçildi.")    
            üye_ol() 
            
        elif seçim == 2:
            print("Sisteme giriş yap seçeneği seçildi.")
            giriş_yap()
                    
        elif seçim == 3:
            print("Şifremi değiştirme seçeneği seçildi.")
            şifre_değişimi()
                        
        elif seçim == 4:
            print("Sistemden çıkış yap seçeneği seçildi. Program sonlandırılıyor...")
            break
        
        else:
            print("Geçersiz seçenek seçildi! Lütfen tekrar deneyin.")
            
            
    except ValueError:
        #Girilen değer sayı değilse hata mesajı verir
        print("Lütfen bir sayı girin!")        

        
