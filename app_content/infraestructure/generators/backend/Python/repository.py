import os
from app_content.application.interface.backend.repository import Repository
from app_content.application.interface.generator import Generator

class PythonRepository(Repository, Generator):
    def execute(self,):
        ''' Generate the files for the model '''
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        path = os.path.join(self.basepath, "application", "repositories")
        os.makedirs(path, exist_ok=True)

        file_path = os.path.join(path, f"{self.model.nombre}_repository.py")
        try:
            with open(file_path, "w") as f:
                f.write(f"from abc import ABC, abstractmethod\n")
                f.write(f"from {self.basepath.replace('/', '.')}.domain.entities.{self.model.nombre}_entity import {nombre}Entity\n\n")
                
                f.write(f"class {nombre}Repository(ABC):\n")
                f.write(f"    def __init__(self):\n")
                f.write(f"        pass\n\n")
                
                f.write(f"{self.save()}\n")
                f.write(f"{self.get_by_id()}\n")
                f.write(f"{self.get()}\n")
                f.write(f"{self.exists_by_id()}\n")
                f.write(f"{self.get_all()}\n")
                f.write(f"{self.delete()}\n")
        except Exception as e:
            raise Exception(e)
        
    def save(self,)->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"    @abstractmethod\n"
            f"    def save(self, obj: {nombre}Entity)-> {nombre}Entity:\n"
            f"        pass\n"
        )
        
    def get(self,)->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"    @abstractmethod\n"
            f"    def get(self, **kwargs)->list[{nombre}Entity] | {nombre}Entity:\n"
            f"        pass\n"
        )
    
    def get_by_id(self)->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"    @abstractmethod\n"
            f"    def get_by_id(self, id)-> {nombre}Entity :\n"
            f"        pass\n"
        )
    
    def exists_by_id(self)->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"    @abstractmethod\n"
            f"    def exists_by_id(self, id)-> bool:\n"
            f"        pass\n"
        )
    
    def get_all(self)->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"    @abstractmethod\n"
            f"    def get_all(self)-> list[{nombre}Entity]:\n"
            f"        pass\n"
        )
    
    def delete(self)->str:
        return (
            f"    @abstractmethod\n"
            f"    def delete(self, id)-> bool:\n"
            f"        pass\n"
        )
        
        