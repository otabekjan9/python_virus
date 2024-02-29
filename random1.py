import random
def random_ism_generatsiya():
    ismlar = ["Ali", "Vali", "Husan", "Odil", "Nigina", "Zulfiya", "Bahrom", "Dilfuza", "Farruh", "Gulbahor"]
    random_ism = random.choice(ismlar)
    return random_ism

# Test qilish
for _ in range(1):
    print(random_ism_generatsiya())
