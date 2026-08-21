# =========================================================
# TƏLƏBƏ QİYMƏTLƏNDİRMƏ SİSTEMİ
# L2 - L9 mövzularının inteqrasiyası
# =========================================================

# L9 - MODUL
# Funksiyaları hesablama.py faylından import edirik
from hesablama import (
    orta_hesabla,
    yekun_bal_hesabla,
    status_lambda,
    netice_lambda,
    telebe_goster
)

import random


# =========================================================
# L2 - ƏDƏDİ / MƏNTİQİ VERİLƏNLƏR VƏ SƏTİRLƏR
# =========================================================

fenler = (
    "Riyaziyyat",
    "Fəlsəfə",
    "Tarix",
    "Kod"
)

# L3 - DİGƏR VERİLƏNLƏR TİPLƏRİ
# List
adlar = [
    "Ali",
    "Zəhra",
    "İsmayıl",
    "Gülnar",
    "Fidan",
    "Zaid",
    "Zaur",
    "Nigar"
]


# =========================================================
# L7 - FUNKSİYA
# Tələbə məlumatı yaradır
# =========================================================

def telebe_yarat(ad):
    fen_qiymetleri = {}

    # L6 - DÖVR OPERATORU
    for fenn in fenler:
        # 0-100 arasında təsadüfi bal
        fen_qiymetleri[fenn] = random.randint(10, 90)

    davamiyyet = random.randint(60, 100)

    qenaet = random.randint(0, 15)

    return {
        "ad": ad,
        "fenler": fen_qiymetleri,
        "davamiyyet": davamiyyet,
        "qenaet": qenaet
    }


# =========================================================
# L7 - PROSEDUR
# Bütün tələbələri ekrana çıxarır
# =========================================================

def butun_telebeleri_goster(telebeler):

    print("\n")
    print("=" * 70)
    print("              BÜTÜN TƏLƏBƏLƏR")
    print("=" * 70)

    # L6 - FOR DÖVRÜ
    for telebe in telebeler:

        orta = orta_hesabla(
            list(telebe["fenler"].values())
        )

        yekun = yekun_bal_hesabla(
            orta,
            telebe["qenaet"]
        )

        netice = netice_lambda(
            yekun,
            telebe["davamiyyet"]
        )

        print(
            f"{telebe['ad']:<12} | "
            f"Orta: {orta:>5.2f} | "
            f"Qənaət: {telebe['qenaet']:>2} | "
            f"Yekun: {yekun:>5.2f} | "
            f"Davamiyyət: {telebe['davamiyyet']:>3} | "
            f"{netice}"
        )

    print("=" * 70)


# =========================================================
# L4 - GİRİŞ / ÇIXIŞ
# L5 - ŞƏRT OPERATORU
# L6 - WHILE DÖVRÜ
# =========================================================

def proqram():

    print("=" * 70)
    print("          TƏLƏBƏ QİYMƏTLƏNDİRMƏ SİSTEMİ")
    print("=" * 70)

    print("\nSistemdə 8 tələbə yaradılır...")
    print("Fənlər: Riyaziyyat, Fəlsəfə, Tarix, Kod")
    print("Keçid balı: 51")
    print("Minimum davamiyyət: 75")
    print("Qənaət balı yekun orta bala əlavə olunur.")

    # =====================================================
    # 8 TƏLƏBƏ YARADILIR
    # =====================================================

    telebeler = []

    # L6 - DÖVR
    for ad in adlar:
        telebeler.append(
            telebe_yarat(ad)
        )

    # =====================================================
    # ƏSAS MENYU
    # =====================================================

    while True:

        print("\n")
        print("1 - Bütün tələbələrə bax")
        print("2 - Tələbə axtar")
        print("3 - Proqramdan çıx")

        secim = input("\nSeçiminizi daxil edin: ")

        # L5 - ŞƏRT OPERATORU

        if secim == "1":

            butun_telebeleri_goster(telebeler)

        elif secim == "2":

            ad = input(
                "\nTələbənin adını daxil edin: "
            ).strip()

            tapildi = False

            # L6 - FOR
            for telebe in telebeler:

                # L5 - IF
                if telebe["ad"].lower() == ad.lower():

                    telebe_goster(telebe)

                    tapildi = True
                    break

            if not tapildi:
                print(
                    "\n❌ Bu adda tələbə sistemdə tapılmadı."
                )

        elif secim == "3":

            print("\nProqram bağlandı. Uğurlar!")
            break

        else:

            print(
                "\n❌ Yanlış seçim! "
                "1, 2 və ya 3 daxil edin."
            )


# =========================================================
# İNTEQRASİYA VƏ SAZLAMA
# =========================================================

try:
    proqram()

except ValueError:
    print(
        "\n❌ Xəta baş verdi: "
        "daxil edilən məlumat düzgün deyil."
    )

except Exception as xeta:
    print(
        "\n❌ Proqramda gözlənilməyən xəta baş verdi:"
    )
    print(xeta)