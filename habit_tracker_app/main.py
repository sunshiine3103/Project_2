from flask import Flask, request, jsonify
from habit_manager import HabitManager
from mood_diary import MoodDiary
from exceptions import HabitError, MoodError

app = Flask(__name__)
habit_manager = HabitManager()
mood_diary = MoodDiary()

@app.route('/add_habit', methods=['POST'])
def add_habit():
    data = request.json
    try:
        habit_manager.add_habit(data['habit'])
        return jsonify({"message": "Привычка добавлена!"}), 201
    except HabitError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/mark_habit', methods=['POST'])
def mark_habit():
    data = request.json
    try:
        habit_manager.mark_habit(data['habit'])
        return jsonify({"message": "Привычка отмечена как выполненная!"}), 200
    except HabitError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/get_stats', methods=['GET'])
def get_stats():
    stats = habit_manager.get_stats()
    return jsonify(stats)

@app.route('/add_mood_entry', methods=['POST'])
def add_mood_entry():
    data = request.json
    try:
        mood_diary.add_entry(data['mood'], data.get('note', ''))
        return jsonify({"message": "Запись в дневник настроения добавлена!"}), 201
    except MoodError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/get_mood_entries', methods=['GET'])
def get_mood_entries():
    entries = mood_diary.get_entries()
    return jsonify(entries)

if __name__ == '__main__':
    app.run(debug=True)
