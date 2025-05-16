import pandas as pd
import sqlite3

def load_data():
    df = pd.read_csv('data/персона.csv', encoding='utf-8', sep=';')
    data = df.to_dict(orient='records')
    return data

def main():
    conn = sqlite3.connect("medical.db")
    cursor = conn.cursor()

    data = load_data()

    for row in data:
        cursor.execute("""
            INSERT INTO Patients (patient_id, last_name, first_name, middle_name, gender, birth_date, oms_policy_number)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            row["ID"],
            row["фамилия"],
            row["имя"],
            row["отчество"],
            row["пол"],
            row["дата рождения"],
            row["номер полиса ОМС"]
        ))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()



