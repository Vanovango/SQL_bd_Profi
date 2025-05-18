import pandas as pd
import sqlite3

def load_data_person():
    df = pd.read_csv('data/персона.csv', encoding='utf-8', sep=';')
    data = df.to_dict(orient='records')
    return data

def load_data_service():
    df = pd.read_csv('data/услуги.csv', encoding='utf-8', sep=';')
    data = df.to_dict(orient='records')
    return data


#======================================================================================================================
def load_into_patients():
    conn = sqlite3.connect("medical.db")
    cursor = conn.cursor()

    data = load_data_person()

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


def load_into_medical_cases():
    conn = sqlite3.connect("medical.db")
    cursor = conn.cursor()

    data = load_data_service()

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



def load_into_case_diagnoses():
    conn = sqlite3.connect("medical.db")
    cursor = conn.cursor()

    data = load_data_service()

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


def load_into_case_services():
    conn = sqlite3.connect("medical.db")
    cursor = conn.cursor()

    data = load_data_service()

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


def load_all_data():
    load_into_patients()
    load_into_medical_cases()
    load_into_case_diagnoses()
    load_into_case_services()


if __name__ == "__main__":
    load_all_data()
