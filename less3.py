
class Task:
    def __init__(self, id, name, description,deadline, is_done):
        self.name = name
        self.id = id
        self.description = description
        self.deadline = deadline
        self.isDone = is_done

    def print_info(self):
         print(f'name:{self.name}')
         print(f'task #{self.id}')
         print(f'description: {self.description}')
         print(f'deadline: {self.deadline}')
         print(f'is_done: {self.isDone}')
task1 = Task(1, 'Buy gta6', "just buy gta 6",deadline ='10.11.2025',is_done = False)
task1.print_info()

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add(self):
        name=input(" task name: ")
        description=input("description: ")
        deadline = input("deadline: ")
        is_done = input(" is_done: True/False: ")
        id=len(self.tasks)+1

        new_task = Task(id, name, description, deadline, is_done)
        self.tasks.append(new_task)

    def print_all_tasks(self):
        for task in self.tasks:
            task.print_info()
task_manager = TaskManager()
while True:
    choose=input(f'Menu:   \n[1]-add task\n[2]-show all task\n[3]-exit')
    if choose == '1':
        task_manager.add()
    if choose == '2':
        task_manager.print_all_tasks()
    if choose == '3':
        break
    else:
        print('Make your choice:')






