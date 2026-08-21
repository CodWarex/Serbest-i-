# ============================================
# L9 - MODUL
# Tələbə qiymətləndirmə sistemi üçün
# hesablama funksiyaları
# ============================================


# L7 - FUNKSIYA
# Fənlərin orta qiymətini hesablayır
def orta_hesabla(qiymetler):
    return sum(qiymetler) / len(qiymetler)


# L7 - FUNKSIYA
# Qənaət balını orta qiymətə əlavə edir
def yekun_bal_hesabla(orta, qenaet):
    return orta + qenaet


# L8 - LAMBDA
# Davamiyyətə görə qiymətləndirməyə buraxılma vəziyyəti
status_lambda = lambda davamiyyet: (
    "Qiymətləndirilməyə buraxılır"
    if davamiyyet >= 75
    else
    "Bu tələbə qiymətləndirilməyə buraxılmır"
)


# L8 - LAMBDA + ÇOX SAYLI PARAMETR
# Yekun bala və davamiyyətə əsasən tələbənin vəziyyəti
netice_lambda = lambda yekun_bal, davamiyyet: (
    "Keçdi"
    if yekun_bal >= 51 and davamiyyet >= 75
    else
    "Kəsildi"
)


# L7 - PROSEDUR
# Tələbənin məlumatlarını ekrana çıxarır
# return istifadə etmir, birbaşa məlumat göstərir
def telebe_goster(telebe):
    print("\n" + "=" * 60)
    print("TƏLƏBƏ MƏLUMATLARI")
    print("=" * 60)

    print(f"Ad: {telebe['ad']}")
    print(f"Davamiyyət: {telebe['davamiyyet']} bal")
    print(f"Qənaət: {telebe['qenaet']} bal")

    print("\nFƏNLƏR:")

    for fenn, qiymet in telebe["fenler"].items():
        if qiymet >= 51:
            status = "Keçdi"
        else:
            status = "Kəsildi"

        print(f"  {fenn:<12} : {qiymet:>5.1f} bal -> {status}")

    print("-" * 60)

    orta = orta_hesabla(list(telebe["fenler"].values()))
    yekun = yekun_bal_hesabla(orta, telebe["qenaet"])

    print(f"Fənlərin orta balı : {orta:.2f}")
    print(f"Qənaət balı        : {telebe['qenaet']}")
    print(f"Yekun bal          : {yekun:.2f}")

    print(
        "Davamiyyət statusu : "
        + status_lambda(telebe["davamiyyet"])
    )

    print(
        "YEKUN NƏTİCƏ       : "
        + netice_lambda(yekun, telebe["davamiyyet"])
    )

    print("=" * 60)