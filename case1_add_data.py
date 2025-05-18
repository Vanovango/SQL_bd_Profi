import sqlite3


def main():
    # Подключаемся к БД
    conn = sqlite3.connect("medical.db")
    cursor = conn.cursor()

    # Загружаем и выполняем SQL-скрипты из файлов
    with open("sql_scripts/mkb.sql", "r", encoding="utf-8") as f:
        data_mkb = f.read()
    cursor.executescript(data_mkb)

    with open("sql_scripts/Spec.sql", "r", encoding="utf-8") as f:
        data_spec = f.read()
    cursor.executescript(data_spec)

    with open("sql_scripts/Usl.sql", "r", encoding="utf-8") as f:
        data_usl = f.read()
    cursor.executescript(data_usl)

    # Сохраняем изменения
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()





