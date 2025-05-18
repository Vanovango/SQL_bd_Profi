def main():
    import pandas as pd
    import os

    # Создание папки для результатов
    output_dir = "case3_tables"
    os.makedirs(output_dir, exist_ok=True)

    # Загрузка исходных данных
    persons = pd.read_csv("data/персона.csv", delimiter=";")
    services = pd.read_csv("data/услуги.csv", delimiter=";")

    # Определение базовых строк (строки 2, 3, 4 → индексы 1, 2, 3)
    base_indices = [1, 2, 3]
    max_index = len(services)
    rows_to_select = []

    # Формируем индексы: каждая базовая строка + 6 * k
    for base in base_indices:
        k = 0
        while (index := base + 6 * k) < max_index:
            rows_to_select.append(index)
            k += 1

    # Получаем выборку
    services_subset = services.iloc[rows_to_select].copy()
    services_subset.to_csv(os.path.join(output_dir, "выборка_услуги_до_очистки.csv"), index=False, sep=";")

    # Преобразуем дату рождения и исключим некорректные
    persons['дата рождения'] = pd.to_datetime(persons['дата рождения'], format="%d.%m.%Y", errors='coerce')

    # Объединение по идентификатору пациента
    merged = services_subset.merge(persons, left_on="Ref_PersSchet", right_on="ID", how="left")
    merged.to_csv(os.path.join(output_dir, "выборка_с_пациентами.csv"), index=False, sep=";")

    # Удаление строк с некорректной датой рождения
    cleaned_subset = merged[merged['дата рождения'].notna()].copy()
    cleaned_subset.to_csv(os.path.join(output_dir, "выборка_услуги_после_очистки.csv"), index=False, sep=";")

    # Вывод статистики
    print(f"До очистки: {len(merged)} строк")
    print(f"После очистки: {len(cleaned_subset)} строк")
    print(f"Удалено: {len(merged) - len(cleaned_subset)} строк")


if __name__ == "__main__":
    main()
