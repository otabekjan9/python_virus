def satrlar_sonini_hisobla(fayl_nomi):
    try:
        with open(fayl_nomi, 'r') as fayl:
            satrlar_soni = 0
            for qator in fayl:
                satrlar_soni += 1
            return satrlar_soni
    except FileNotFoundError:
        return f"Fayl topilmadi: {fayl_nomi}"

# Fayl nomi
fayl_nomi = 'virus-python.txt'

# Satrlar sonini hisoblash
natija = satrlar_sonini_hisobla(fayl_nomi)

# Natijani chiqarish
print(f"{fayl_nomi} faylida {natija} ta qator bor.")
