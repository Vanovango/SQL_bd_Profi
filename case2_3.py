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
            INSERT INTO CaseDiagnoses (diagnosis_date, diagnosis_code)
            VALUES (?, ?)
        """, (
            row["дата окончания"],
            row["Диагноз"]
        ))

    conn.commit()
    conn.close()
#
# if __name__ == "__main__":
#     main()



