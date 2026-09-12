#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Türk Hukuku Dilekçe Operatörü
Basit dilekçe oluşturma sistemi
"""

import os
from datetime import datetime

def temizle_ekran():
    """Ekranı temizle"""
    os.system('clear' if os.name == 'posix' else 'cls')

def ana_menu():
    """Ana menüyü göster"""
    temizle_ekran()
    print("=" * 50)
    print("TÜRK HUKUKU DİLEKÇE OPERATÖRÜ")
    print("=" * 50)
    print("\n1. Yeni Dilekçe Oluştur")
    print("2. Örnek Dilekçe Göster")
    print("3. Çıkış")
    print("\n" + "=" * 50)
    secim = input("Seçiminiz (1-3): ")
    return secim

def bilgi_al():
    """Kullanıcıdan bilgi al"""
    temizle_ekran()
    print("=" * 50)
    print("DİLEKÇE OLUŞTURMAK İÇİN BİLGİ GİRİN")
    print("=" * 50)
    
    ad = input("\nAdınız: ").strip()
    soyad = input("Soyadınız: ").strip()
    tc_kimlik = input("T.C. Kimlik Numaranız: ").strip()
    adres = input("Adresiniz: ").strip()
    telefon = input("Telefon Numaranız: ").strip()
    email = input("E-mail Adresiniz: ").strip()
    
    dava_konusu = input("\nDava Konusu (Kısaca): ").strip()
    dava_detay = input("Dava Detayları (Uzun açıklama): ").strip()
    talep = input("Talep (Ne istiyorsunuz?): ").strip()
    
    bilgiler = {
        'ad': ad,
        'soyad': soyad,
        'tc_kimlik': tc_kimlik,
        'adres': adres,
        'telefon': telefon,
        'email': email,
        'dava_konusu': dava_konusu,
        'dava_detay': dava_detay,
        'talep': talep,
        'tarih': datetime.now().strftime("%d.%m.%Y")
    }
    
    return bilgiler

def dilekce_olustur(bilgiler):
    """Dilekçe oluştur"""
    dilekce = f"""
{'=' * 70}
                    DAVA DİLEKÇESİ
{'=' * 70}

TARİH: {bilgiler['tarih']}

DİLEKÇE SAHİBİ BİLGİLERİ:
─────────────────────────────────────────────────────────────────────
Ad Soyad        : {bilgiler['ad']} {bilgiler['soyad']}
T.C. Kimlik No  : {bilgiler['tc_kimlik']}
Adres           : {bilgiler['adres']}
Telefon         : {bilgiler['telefon']}
E-mail          : {bilgiler['email']}

DAVA KONUSU:
─────────────────────────────────────────────────────────────────────
{bilgiler['dava_konusu']}

DAVA DETAYLARı:
─────────────────────────────────────────────────────────────────────
{bilgiler['dava_detay']}

TALEP:
─────────────────────────────────────────────────────────────────────
{bilgiler['talep']}

DİLEKÇE AÇIKLAMASI:
─────────────────────────────────────────────────────────────────────
Yukarıda belirtilen hususlar gereğince, haklarımı korumak ve mağduriyetimi
gidermek amacıyla bu dilekçeyi saygılarımla sunuyorum.

İlgili makamlardan, bu dilekçenin incelenerek uygun işlemler yapılmasını
hürmetlerimle talep ederim.

{'=' * 70}
DİLEKÇE SAHİBİNİN İMZASI: _______________________

{'=' * 70}
"""
    return dilekce

def ornek_dilekce_goster():
    """Örnek dilekçe göster"""
    ornek_bilgiler = {
        'ad': 'Ahmet',
        'soyad': 'Yılmaz',
        'tc_kimlik': '12345678901',
        'adres': 'İstanbul, Türkiye',
        'telefon': '0212 555 5555',
        'email': 'ahmet@example.com',
        'dava_konusu': 'İş Sözleşmesinin Haksız Feshi',
        'dava_detay': 'Şirkette 5 yıl çalıştıktan sonra haklı bir sebep olmaksızın işime son verilmiştir.',
        'talep': 'İş sözleşmesinin iadesi veya tazminat ödenmesi',
        'tarih': datetime.now().strftime("%d.%m.%Y")
    }
    
    dilekce = dilekce_olustur(ornek_bilgiler)
    print(dilekce)
    input("\nDevam etmek için Enter tuşuna basın...")

def dilekce_kaydet(bilgiler, dilekce):
    """Dilekçeyi dosyaya kaydet"""
    dosya_adi = f"dilekce_{bilgiler['ad']}_{bilgiler['soyad']}_{datetime.now().strftime('%d%m%Y_%H%M%S')}.txt"
    
    with open(dosya_adi, 'w', encoding='utf-8') as f:
        f.write(dilekce)
    
    print(f"\n✓ Dilekçe başarıyla kaydedildi!")
    print(f"Dosya adı: {dosya_adi}")
    input("Devam etmek için Enter tuşuna basın...")

def main():
    """Ana program"""
    while True:
        secim = ana_menu()
        
        if secim == '1':
            # Yeni dilekçe oluştur
            bilgiler = bilgi_al()
            dilekce = dilekce_olustur(bilgiler)
            
            temizle_ekran()
            print(dilekce)
            
            print("\n" + "=" * 50)
            print("1. Dosyaya Kaydet")
            print("2. Ana Menüye Dön")
            print("=" * 50)
            sub_secim = input("Seçiminiz (1-2): ")
            
            if sub_secim == '1':
                dilekce_kaydet(bilgiler, dilekce)
        
        elif secim == '2':
            # Örnek dilekçe göster
            ornek_dilekce_goster()
        
        elif secim == '3':
            # Çıkış
            temizle_ekran()
            print("Program sonlandırılıyor... Hoşça kalın!")
            break
        
        else:
            print("Geçersiz seçim! Lütfen 1-3 arasında bir sayı girin.")
            input("Devam etmek için Enter tuşuna basın...")

if __name__ == "__main__":
    main()
