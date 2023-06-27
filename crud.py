import json

file_path = 'todo.json'


class TodoBot:
    def __init__(self):
        self.todos = []
        self.load_data()

    def load_data(self):
        try:
            with open(file_path) as file:
                self.todos = json.load(file)
        except FileNotFoundError:
            self.todos = []

    def save_data(self):
        with open(file_path, 'w') as file:
            json.dump(self.todos, file)

    def create_task(self, task):
        new_task = {
            'id': len(self.todos) + 1,
            'task': task,
            'completed': False
        }
        self.todos.append(new_task)
        self.save_data()

    def get_all_tasks(self):
        return self.todos

    def get_task_by_id(self, task_id):
        for task in self.todos:
            if task['id'] == task_id:
                return task
        return None

    def update_task(self, task_id, new_task):
        task = self.get_task_by_id(task_id)
        if task:
            task['task'] = new_task
            self.save_data()

    def delete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            self.todos.remove(task)
            self.save_data()


bot = TodoBot()

# Пример использования бота
bot.create_task("Помыть посуду")
bot.create_task("Сходить в магазин")
bot.create_task("Выучить Python")

tasks = bot.get_all_tasks()
print("Список задач:")
for task in tasks:
    print(task)

bot.update_task(2, "Купить молоко")

tasks = bot.get_all_tasks()
print("Список задач после обновления:")
for task in tasks:
    print(task)

bot.delete_task(1)

tasks = bot.get_all_tasks()
print("Список задач после удаления:")
for task in tasks:
    print(task)
