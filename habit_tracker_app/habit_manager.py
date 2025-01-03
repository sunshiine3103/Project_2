from exceptions import HabitError

class HabitManager:
    """Класс для управления привычками."""

    def __init__(self):
        """Инициализирует менеджер привычек."""
        self.habits = {}

    def add_habit(self, habit: str):
        """Добавляет новую привычку."""
        if not isinstance(habit, str) or not habit.strip():
            raise HabitError("Некорректное значение для привычки.")
        self.habits[habit] = {"completed": False}

    def mark_habit(self, habit: str):
        """Отмечает привычку как выполненную."""
        if habit not in self.habits:
            raise HabitError("Привычка не найдена.")
        self.habits[habit]["completed"] = True

    def get_stats(self):
        """Возвращает статистику по привычкам."""
        return {habit: info["completed"] for habit, info in self.habits.items()}
