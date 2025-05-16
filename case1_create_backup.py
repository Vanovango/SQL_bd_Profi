import sqlite3

def main():
    conn = sqlite3.connect("medical.db")

    # Создаем новое соединение для резервной копии
    backup_conn = sqlite3.connect("medical_backup.db")

    # Копируем данные из исходной базы в резервную
    with backup_conn:
        conn.backup(backup_conn)

    # Закрываем соединения
    conn.close()
    backup_conn.close()

#
# if __name__ == "__main__":
#     main()




