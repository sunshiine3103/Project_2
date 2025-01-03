# Project_2

# Habit Tracker

Habit Tracker — это приложение, которое позволяет пользователям отслеживать свои привычки и вести дневник настроения. Оно помогает пользователям формировать положительные привычки, а также анализировать, как выполнение или невыполнение привычек влияет на их эмоциональное состояние.

## Функциональность

- Отслеживание привычек: Пользователи могут добавлять новые привычки, отмечать их выполнение и просматривать статистику по выполнению.
- Дневник настроения: Пользователи могут записывать свои эмоции и наблюдения о том, как привычки влияют на их настроение.
  
## Установка

1. Клонируйте репозиторий.
2. Установите зависимости:

   pip install -r requirements.txt
   
3. Запустите приложение:
   
   python habittrackerapp/main.py   

## Использование API

### Добавление привычки

Запрос: POST /add_habit

Тело запроса (JSON):
json
{
    "habit": "Чтение книги"
}
Ответ:
json
{
    "message": "Привычка добавлена!"
}
### Отметить выполнение привычки

Запрос: POST /mark_habit

Тело запроса (JSON):
json
{
    "habit": "Чтение книги"
}
Ответ:
json
{
    "message": "Привычка отмечена как выполненная!"
}
### Получить статистику по привычкам

Запрос: GET /get_stats

Ответ:
json
{
    "Чтение книги": false,
    "Спорт": true
}
### Добавить запись в дневник настроения

Запрос: POST /add_mood_entry

Тело запроса (JSON):
json
{
    "mood": "Счастлив",
    "note": "Сегодня прочитал интересную книгу."
}
Ответ:
json
{
    "message": "Запись в дневник настроения добавлена!"
}
### Получить записи дневника настроения

Запрос: GET /get_mood_entries

Ответ:
json
[
    {
        "mood": "Счастлив",
        "note": "Сегодня прочитал интересную книгу."
    },
    {
        "mood": "Устал",
        "note": "Много работал сегодня."
    }
]
