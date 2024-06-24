class Task():
    def __init__(self):
        self.tasks = []

    def add_task(self, deadline, description):
        self.tasks.append({"deadline": deadline,
                           "description": description, "status": "не выполнено"})

    def complete_task(self, description):
        for task in self.tasks:
            if task["description"] == description:
                task["status"] = "выполнено"
                print(f"Задача '{description}' успешно выполнена")
            else:
                print(f"Задача '{description}' Задача не найдена")

    def show_tasks(self):
        print("текущие задачи")
        for task in self.tasks:
            if task['status'] == "не выполнено":
                print(f"{task['description']} - {task['deadline']}")


t = Task()
t.add_task("02.06.2024", "пообедать")
t.add_task("03.06.2024", "сделать домашнее задание")
t.add_task("04.06.2024", "погулять с собакой")

t.show_tasks()

t.complete_task("пообедать")