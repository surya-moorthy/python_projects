from task import Task , TaskManager
from typing import Literal

task = input("Do you want to create task Manager (y,n):")
if task == "y":
        tasks = TaskManager()
        while(True):
            operation : str = input("What do you want to do?:\n 1) Add Task \n 2) Delete Task \n 3) Update Task \n 4)Find Task\n5)Exit\n:")
            if operation == "Add Task":
                title: str = input('Enter the title:')
                descripton: str = input('Enter the Description:')
                status: Literal["completed" , "pending" , "not started"] = input('Enter the status:')
                status = tasks.add_task(Task(title=title,description=descripton,status=status))
                print(status)
                print(tasks)
                print("length of the tasks:",len(tasks.Tasks))
            if operation == "Delete Task":
                title: str = input('Enter the title of the task that you want to delete:')
                status = tasks.del_task(title)
                print(status)
                print(task)
            if operation == "exit":
                exit()

            
        
