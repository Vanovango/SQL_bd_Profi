import sqlite3


def create_db():
    # Создание подключения и базы данных
    conn = sqlite3.connect("medical.db")
    cursor = conn.cursor()

    # Создаем таблицы

    # Таблица пациентов
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Patients (
        patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
        last_name TEXT NOT NULL,
        first_name TEXT NOT NULL,
        middle_name TEXT,
        gender TEXT CHECK (gender IN ('М', 'Ж')) NOT NULL,
        birth_date DATE NOT NULL,
        oms_policy_number TEXT NOT NULL
    );
    """)

    # Таблица врачей
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Doctors (
        doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
        last_name TEXT NOT NULL,
        first_name TEXT NOT NULL,
        middle_name TEXT,
        snils TEXT UNIQUE NOT NULL,
        specialty_code TEXT NOT NULL,
        
        FOREIGN KEY (specialty_code) REFERENCES rbSpeciality(id)
    );
    """)

    # Таблица случаев оказания медицинской помощи
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS MedicalCases (
        case_id INTEGER PRIMARY KEY AUTOINCREMENT,        
        start_date DATE NOT NULL,
        end_date DATE,
        doctor_id INTEGER NOT NULL,
        result TEXT NOT NULL,
        
        FOREIGN KEY (doctor_id) REFERENCES rbSpeciality(id)
    );
    """)

    # Диагнозы, установленные в рамках случая
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS CaseDiagnoses (
        diagnosis_id INTEGER PRIMARY KEY AUTOINCREMENT,
        diagnosis_date DATE NOT NULL,
        diagnosis_code TEXT NOT NULL,
        diagnosis_type TEXT CHECK (diagnosis_type IN ('основной', 'сопутствующий')),
        
        FOREIGN KEY (diagnosis_code) REFERENCES mkb(code)
    );
    """)

    # Медицинские услуги, оказанные в рамках случая
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS CaseServices (
        service_id INTEGER PRIMARY KEY AUTOINCREMENT,
        service_date DATE NOT NULL,
        service_code TEXT NOT NULL,
        doctor_id INTEGER NOT NULL,

        FOREIGN KEY (service_code) REFERENCES rbService(code),
        FOREIGN KEY (doctor_id) REFERENCES rbSpeciality(id)
    );
    """)

    # Создание справочников
    with open("sql_scripts/create_table.sql", "r", encoding="utf-8") as f:
        sql_script = f.read()
    cursor.executescript(sql_script)


    # Сохраняем изменения и закрываем соединение
    conn.commit()
    conn.close()

# if __name__ == "__main__":
#     create_db()
