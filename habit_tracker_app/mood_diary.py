from exceptions import MoodError

class MoodDiary:
      """Класс для ведения дневника настроения."""

    def __init__(self):
        """Инициализирует дневник настроения."""
        self.entries = []

    def add_entry(self, mood: str, note: str):
        """Добавляет запись в дневник настроения."""
        if not isinstance(mood, str) or not mood.strip():
            raise MoodError("Некорректное значение для настроения.")
        self.entries.append({"mood": mood.strip(), "note": note.strip()})

    def get_entries(self):
        """Возвращает все записи дневника настроения."""
        return self.entries
