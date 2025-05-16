import pandas as pd
import sqlite3

def load_data():
    df = pd.read_csv('data/услуги.csv', encoding='utf-8', sep=';')
    data = df.to_dict(orient='records')
    return data

def main():
    conn = sqlite3.connect("medical.db")
    cursor = conn.cursor()

    data = load_data()

    for row in data:
        cursor.execute("""
            INSERT INTO MedicalCases (start_date, end_date, doctor_id, result)
            VALUES (?, ?, ?, ?)
        """, (
            row["дата начала"],
            row["дата окончания"],
            row["Специальность врача"],
            row["Исход обращения"]
        ))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()



