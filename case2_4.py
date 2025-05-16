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
            INSERT INTO CaseServices (service_date, service_code, doctor_id)
            VALUES (?, ?, ?)
        """, (
            row["дата начала"],
            row["Услуга"],
            row["Специальность врача"]
        ))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()



