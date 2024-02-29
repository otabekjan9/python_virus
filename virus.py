import os

def scan_directory(directory):
    virus_count = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            # Bu joyda siz o'zingizning virus identifikatsiya tizimini qo'llashingiz kerak
            # Bu namuna orqali emulyatsiya qilinmoqda
            is_infected = check_for_virus(file_path)

            if is_infected:
                print(f"Virus topildi: {file_path}")
                virus_count += 1

    return virus_count

def word_file_size(file_path):
    try:
        #Fayl hajmini olish
        size_in_bytes=os.path.getsize(file_path)

        #Hajmini mb va kb larda aylantiramiz
        size_in_mb=size_in_bytes/(1024)
        
        return size_in_mb
    except FileNotFoundError:
        return "Fayl topilmadi"
    except Exception as e:
        return f"Xatolik yuz berdi:{e}"

file_path="otabek.doc" 
result=word_file_size(file_path)
print(f"Fayl hajmi:r{result}KB")   

def check_for_virus(file_path):
    # Bu joyda siz o'zingizning virus identifikatsiya tizimini qo'llashingiz kerak
    # Bu namuna orqali emulyatsiya qilinmoqda
    # Sizning haqingizda bo'lgan qo'shimcha ma'lumotni qo'shishingiz kerak

    # Misol: agar fayl nomi "virus.exe" bo'lsa, uni virus sifatida tanlaymiz
    if "virus" in file_path.lower():
        return True

    return False




import fitz  # PyMuPDF kutubxonasini chaqirib olish
from docx import Document
def hisoblash(word_fayli):
    qator_soni = 0

    # Word faylini ochamiz
    doc = Document(word_fayli)

    # Har bir sahifadagi qatorlarni hisoblaymiz
    for paragraf in doc.paragraphs:
        qator_soni += len(paragraf.text.split('\n'))

    return qator_soni

# Word faylini joylashgan manzilni kiriting
word_fayli = 'otabek1.docx'

# Qatorlar sonini hisoblash
natija = hisoblash(word_fayli)

print(f"{word_fayli} faylida {natija} ta qator bor.")




def main():
    print("Virus skaneri uchun kalkulyator dasturiga xush kelibsiz!")
    directory = input("Skanirovatmoqchi bo'lgan direktoriyani kiriting: ")

    if os.path.exists(directory):
        print(f"\nSkanoriya boshlanmoqda {directory}...")
        virus_count = scan_directory(directory)
        print(f"\nSkanoriya tugatildi. Jami viruslar soni: {virus_count}")
    else:
        print("Xatolik: Kiritilgan direktoriya mavjud emas.")

if __name__ == "__main__":
    main()
