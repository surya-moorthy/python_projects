from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Literal,Dict

@dataclass
class Task:
      title: str 
      description: str
      status: Literal["completed" , "pending" , "not started"] = "not started"

class TaskManager:
    
    def __init__(self):
           self.Tasks : Dict[str,Task]= {}
          

    @abstractmethod
    def add_task(self,task: Task):
        self.Tasks = {task.title : Task(title=task.title,description=task.description,status=task.status)}
        return "Task successfully added"
    def del_task(self,title: str):
        if not self.Tasks:
            return "No Tasks are added"
        if title in self.Tasks:
                del self.Tasks[title]
                return "Deleted successfully"
        return "No such Task"
    def upt_task(self,title: str,Updatevalues: str | Task):
         pass
    def find_task(self,title: str):
        pass
    def get_tasks(self,title: str):
        pass
    def __repr__(self):
         return f"TaskManager(Tasks={self.Tasks})"