import pandas as pd
from datetime import datetime

# Загрузка очищенной выборки
df = pd.read_csv("case3_tables/выборка_услуги_после_очистки.csv", delimiter=";")

# Преобразуем даты
df["дата рождения"] = pd.to_datetime(df["дата рождения"], errors="coerce")
df["дата начала"] = pd.to_datetime(df["дата начала"], errors="coerce")

# ------------------------------
# Вопрос 1: Диагнозы в выборке
# ------------------------------
diag_check = ["A09.0", "B35.4", "C20"]
diag_result = {code: "ДА" if code in df["Диагноз"].values else "НЕТ" for code in diag_check}

# ------------------------------
# Вопрос 2: Группировка по полу и возрасту
# ------------------------------
# Текущий год для расчёта возраста
current_year = datetime.now().year

# Возраст на момент обращения
df["возраст"] = df["дата начала"].dt.year - df["дата рождения"].dt.year

# Условия по группам
conditions = {
    "мужчины до 30": ((df["пол"] == "М") & (df["возраст"] < 30)),
    "мужчины 30-50": ((df["пол"] == "М") & (df["возраст"] >= 30) & (df["возраст"] < 50)),
    "мужчины 50+": ((df["пол"] == "М") & (df["возраст"] >= 50)),
    "женщины до 30": ((df["пол"] == "Ж") & (df["возраст"] < 30)),
    "женщины 30-50": ((df["пол"] == "Ж") & (df["возраст"] >= 30) & (df["возраст"] < 50)),
    "женщины 50+": ((df["пол"] == "Ж") & (df["возраст"] >= 50)),
}

group_counts = {group: df[cond].shape[0] for group, cond in conditions.items()}

# ------------------------------
# Вопрос 3: Уникальные пациенты
# ------------------------------
unique_patients = df["ID"].nunique()

# ------------------------------
# Вопрос 4: Последние визиты по группам
# ------------------------------
def last_visit_date(condition):
    subset = df[condition]
    return subset["дата начала"].max() if not subset.empty else None

last_visits = {
    "женщины 50+": last_visit_date(conditions["женщины 50+"]),
    "мужчины до 30": last_visit_date(conditions["мужчины до 30"]),
    "все 30-50": last_visit_date(
        ((df["возраст"] >= 30) & (df["возраст"] < 50))
    ),
}

# ------------------------------
# Печать результата
# ------------------------------
print("\nВопрос 1: Диагнозы")
for d, result in diag_result.items():
    print(f"{d}: {result}")

print("\nВопрос 2: Количество услуг по полу и возрасту:")
for group, count in group_counts.items():
    print(f"{group}: {count}")

print(f"\nВопрос 3: Уникальных пациентов: {unique_patients}")

print("\nВопрос 4: Последние приёмы")
for group, date in last_visits.items():
    print(f"{group}: {date.strftime('%d.%m.%Y') if pd.notna(date) else 'нет данных'}")
