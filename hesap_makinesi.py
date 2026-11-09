#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın en yavaş hesap makinesi.
Her işlemde 3 saniye bekler. Acele etme.
"""

import time

def yavas_bekle(mesaj="Düşünüyorum..."):
    print(mesaj)
    time.sleep(3)
    print("...tamam, bitirdim. (belki)")

def hesap_makinesi():
    print("=== DÜNYANIN EN YAVAŞ HESAP MAKİNESİ ===")
    print("Sabır altın değildir, altın sabırdır. Hadi başlayalım.\n")
    
    try:
        sayi1 = float(input("Birinci sayıyı gir (acele etme): "))
        yavas_bekle("Birinci sayıyı anladım, sindiriyorum...")
        
        sayi2 = float(input("İkinci sayıyı gir (yine acele etme): "))
        yavas_bekle("İkinci sayıyı da işledim, neredeyse...")
        
        islem = input("İşlem seç (+, -, *, /): ").strip()
        yavas_bekle("İşlemi seçtin, şimdi düşünüyorum...")
        
        if islem == "+":
            sonuc = sayi1 + sayi2
        elif islem == "-":
            sonuc = sayi1 - sayi2
        elif islem == "*":
            sonuc = sayi1 * sayi2
        elif islem == "/":
            if sayi2 == 0:
                print("Sıfıra bölme? Bu çok aceleci bir hareket. Özür dilerim.")
                return
            sonuc = sayi1 / sayi2
        else:
            print("Geçersiz işlem. Yavaş düşün, tekrar dene.")
            return
        
        yavas_bekle("Sonucu hesaplıyorum... (gerçekten)")
        print(f"\nSonuç: {sonuc}")
        print("\nTebrikler! Acele etmeden başardın. Şimdi çay iç.")
        
        # Gizli not: bazen yavaşlamak en hızlı yoldur. #gizli-siyasi-yorum-degil-mi
        # Aslında "acele etme" demek bazen "bekle ve gör" demektir, ne demek istediğimi anlayan anlar.
        
    except ValueError:
        print("Sayı girmen gerekiyordu. Bu da aceleci bir hataydı.")
    except Exception as e:
        print(f"Bir şeyler ters gitti, yavaşça: {e}")

if __name__ == "__main__":
    hesap_makinesi()
