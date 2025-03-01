from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Literal

@dataclass
class Task:
      title: str 
      description: str
      status: Literal["completed" , "pending" , "not started"] = "not started"

class TaskManager:
    
    def __init__(self):
           self.Tasks : dict[str,Task]= {}
          

    @abstractmethod
    def add_task(self,task: Task):
        self.Tasks = {task.title : Task(title=task.title,description=task.description,status=task.status)}
        return "Task successfully added"
    def del_task(self,title: str):
        pass
    def upt_task(self,title: str):
        pass
    def find_task(self,title: str):
        pass
    def get_tasks(self,title: str):
        pass