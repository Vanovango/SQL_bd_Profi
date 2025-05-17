import sqlite3
import csv
import os

def count_lines_in_csv(filepath, skip_header=True):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return len(lines) - 1 if skip_header else len(lines)

def check_table_counts():
    print("\n--- Проверка количества строк ---")
    expected = {
        "Patients": count_lines_in_csv("./data/персона.csv"),
        "MedicalCases": count_lines_in_csv("./data/услуги.csv"),
        "CaseDiagnoses": count_lines_in_csv("./data/услуги.csv"),
        "CaseServices": count_lines_in_csv("./data/услуги.csv"),
    }

    conn = sqlite3.connect("medical.db")
    cursor = conn.cursor()

    for table, expected_count in expected.items():
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        actual_count = cursor.fetchone()[0]
        print(f"{table}: {actual_count} / {expected_count} строк —", end=" ")
        print("✅ OK" if actual_count == expected_count else "❌ НЕСОВПАДЕНИЕ")

    conn.close()

def check_foreign_keys():
    print("\n--- Проверка связей между таблицами ---")
    conn = sqlite3.connect("medical.db")
    cursor = conn.cursor()

    checks = [
        # Таблица, поле, справочник, справочное поле
        ("MedicalCases", "doctor_id", "Doctors", "doctor_id"),
        ("CaseDiagnoses", "diagnosis_code", "mkb", "code"),
        ("CaseServices", "service_code", "rbService", "code"),
        ("CaseServices", "doctor_id", "Doctors", "doctor_id")
    ]

    for table, fk_field, ref_table, ref_field in checks:
        query = f"""
            SELECT COUNT(*) 
            FROM {table} t
            LEFT JOIN {ref_table} r ON t.{fk_field} = r.{ref_field}
            WHERE r.{ref_field} IS NULL
        """
        cursor.execute(query)
        missing = cursor.fetchone()[0]
        print(f"{table}.{fk_field} → {ref_table}.{ref_field}: ", end="")
        print("✅ OK" if missing == 0 else f"❌ {missing} не найдены в {ref_table}")

    conn.close()

def main():
    check_table_counts()
    check_foreign_keys()


# if __name__ == "__main__":
#     main()
