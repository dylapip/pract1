import csv

animalsdata = [
    {"животное": "лось", "среда": "лес"},
    {"животное": "белка", "среда": "лес"},
    {"животное": "тигр", "среда": "джунгли"},
    {"животное": "кит", "среда": "море"},
    {"животное": "медведь", "среда": "лес"},
    {"животное": "верблюд", "среда": "пустыня"},
]

with open("animals.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["животное", "среда"])
    writer.writeheader()
    for row in animalsdata:
        writer.writerow(row)

employeesdata = [
    {"имя": "алексей", "возраст": "28", "город": "москва", "должность": "инженер"},
    {"имя": "мария",  "возраст": "34", "город": "санкт-Петербург", "должность": "менеджер"},
    {"имя": "иван",   "возраст": "45", "город": "казань", "должность": "директор"},
    {"имя": "ольга",  "возраст": "неизвестно", "город": "новосибирск", "должность": "аналитик"},
    {"имя": "петр",   "возраст": "31", "город": "екатеринбург", "должность": "разработчик"},
    {"имя": "елена",  "возраст": "29", "город": "калининград", "должность": "дизайнер"},
]

csvfilename = "csvfile.csv"
with open(csvfilename, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["имя", "возраст", "город", "должность"])
    writer.writeheader()
    for row in employeesdata:
        writer.writerow(row)

print("животные, обитающие в лесу:")
try:
    with open("animals.csv", "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("среда", "").strip() == "лес":
                name = row.get("животное", "").strip()
                if name:
                    print(name)
except FileNotFoundError:
    print("файл animals.csv не найден")

print() 

print("имена сотрудников с возрастом > 30:")
try:
    with open(csvfilename, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            agestr = row.get("возраст", "").strip()
            try:
                age = int(agestr)
            except ValueError:
                continue
            if age > 30:
                name = row.get("имя", "").strip()
                if name:
                    print(name)
except FileNotFoundError:
    print("файл не найден")