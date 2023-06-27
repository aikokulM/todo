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


def print_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}")


def create_task(bot):
    task = input("Введите задание:")
    bot.create_task(task)
    print("Задача успешно создана.")


def list_tasks(bot):
    tasks = bot.get_all_tasks()
    print("Tasks:")
    print_tasks(tasks)


def update_task(bot):
    task_id = int(input("Введите id задачи для обновления:"))
    new_task = input("Введите новую задачу:")
    bot.update_task(task_id, new_task)
    print("Задача успешно обновлена.")


def delete_task(bot):
    task_id = int(input("Введите id задачи для удаления:"))
    bot.delete_task(task_id)
    print("Задача успешно удалена.")


def main():
    bot = TodoBot()

    while True:
        print("\n==== TODO Bot ====")
        print("1. Create task")
        print("2. List tasks")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Введите свой выбор (1-5): ")

        if choice == '1':
            create_task(bot)
        elif choice == '2':
            list_tasks(bot)
        elif choice == '3':
            update_task(bot)
        elif choice == '4':
            delete_task(bot)
        elif choice == '5':
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте еще раз.")


if __name__ == "__main__":
    main()