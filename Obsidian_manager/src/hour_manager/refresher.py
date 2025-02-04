from const import DATE_FORMAT
from config import LAST_RUN_FILE, REGULAR_PATH_FILE, TASKS_PATH
from datetime import datetime
from src.hour_manager.task_manager import TaskManager, TasksUnchecker
from src.hour_manager.calendar_client import GoogleCalendar

if __name__ == "__main__":
    # Получаем дату последнего запуска из файла
    def get_last_run_date():
        try:
            with open(LAST_RUN_FILE, "r") as f:
                return f.read().strip()
        except FileNotFoundError:
            return None

    # Обновляем файл с датой выполнения
    def update_last_run_date():
        with open(LAST_RUN_FILE, "w") as f:
            f.write(datetime.now().strftime(DATE_FORMAT))


    last_run_date = get_last_run_date()

    if last_run_date.split("T")[0] != datetime.now().strftime(DATE_FORMAT).split("T")[0]:
        # Обновляю ежедневные задачи
        uncheker = TasksUnchecker()
        uncheker.uncheck_tasks(REGULAR_PATH_FILE, DATE_FORMAT)
        # Актуализирую информацию по задачам и получаю список невыполненных задач
        manage_task = TaskManager()
        tasks_dict = manage_task.task_manager(TASKS_PATH, )
        # Добавляем задачи в гугл календарь
        calendar = GoogleCalendar()
        calendar.add_to_calendar(tasks_dict)

        update_last_run_date()
        print("Скрипты выполнены, дата обновлена")
    else:
        print("Скрипты уже выполнялись сегодня.")
