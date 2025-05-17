import sqlite3
import csv
from datetime import datetime
import os

def save_to_csv(filename, headers, data):
    export_dir = "./saved_csv"
    if not os.path.exists(export_dir):
        os.makedirs(export_dir)

    with open(f'{export_dir}/{filename}', "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)
    print(f"Сохранено в файл: {filename}")

def export_patients_grouped_by_age_gender():
    conn = sqlite3.connect("medical.db")
    cursor = conn.cursor()

    cursor.execute("SELECT gender, birth_date FROM Patients")
    rows = cursor.fetchall()

    from collections import defaultdict

    def parse_birth(date_str):
        for fmt in ("%d.%m.%Y", "%Y-%m-%d"):
            try:
                return datetime.strptime(date_str.strip(), fmt)
            except:
                continue
        return None

    result = defaultdict(int)
    for gender, birth_str in rows:
        date = parse_birth(birth_str)
        if not date: continue
        age = int((datetime.now() - date).days / 365.25)
        age_group = (age // 10) * 10
        result[(gender, age_group)] += 1

    data = [(g, f"{a}-{a+9}", count) for (g, a), count in sorted(result.items())]
    save_to_csv("patients_by_age_gender.csv", ["Пол", "Возрастная группа", "Количество"], data)
    conn.close()

def export_case_diagnoses_grouped():
    conn = sqlite3.connect("medical.db")
    cursor = conn.cursor()

    cursor.execute("SELECT diagnosis_code FROM CaseDiagnoses")
    rows = cursor.fetchall()

    from collections import defaultdict
    counts = defaultdict(int)
    for (code,) in rows:
        if code:
            counts[code.strip().upper()] += 1

    data = [(code, count) for code, count in sorted(counts.items(), key=lambda x: -x[1])]
    save_to_csv("diagnoses_grouped.csv", ["Код МКБ", "Количество"], data)
    conn.close()

def export_case_services_grouped():
    conn = sqlite3.connect("medical.db")
    cursor = conn.cursor()

    cursor.execute("SELECT service_code FROM CaseServices")
    rows = cursor.fetchall()

    from collections import defaultdict
    counts = defaultdict(int)
    for (code,) in rows:
        if code:
            counts[code.strip().upper()] += 1

    data = [(code, count) for code, count in sorted(counts.items(), key=lambda x: -x[1])]
    save_to_csv("services_grouped.csv", ["Код услуги", "Количество"], data)
    conn.close()

def export_medical_cases_by_month():
    conn = sqlite3.connect("medical.db")
    cursor = conn.cursor()

    cursor.execute("SELECT start_date FROM MedicalCases")
    rows = cursor.fetchall()

    from collections import defaultdict
    counts = defaultdict(int)

    def parse_date(date_str):
        for fmt in ("%d.%m.%Y", "%Y-%m-%d"):
            try:
                return datetime.strptime(date_str.strip(), fmt)
            except:
                continue
        return None

    for (d,) in rows:
        date = parse_date(d)
        if date:
            key = date.strftime("%Y-%m")
            counts[key] += 1

    data = [(k, v) for k, v in sorted(counts.items())]
    save_to_csv("medical_cases_by_month.csv", ["Месяц", "Количество случаев"], data)
    conn.close()


def main():
    export_patients_grouped_by_age_gender()
    export_case_diagnoses_grouped()
    export_case_services_grouped()
    export_medical_cases_by_month()

#
# if __name__ == "__main__":
#     main()
