import os
from app_content.domain.entities.model_entity import ModelEntity
from app_content.application.interface.repository import Repository

class PythonRepository(Repository):

    def execute(self, model: ModelEntity, basepath: str,):
        ''' Generate the files for the model '''
        nombre = f"{model.nombre[0].capitalize()}{model.nombre[1:]}"
        path = os.path.join(basepath, "application", "repositories")
        os.makedirs(path, exist_ok=True)

        file_path = os.path.join(path, f"{model.nombre}_repository.py")
        try:
            with open(file_path, "w") as f:
                f.write(f"from abc import ABC, abstractmethod\n")
                f.write(f"from {basepath}.domain.entities.{model.nombre}_entity import {nombre}Entity\n\n")
                
                f.write(f"class {nombre}Repository(ABC):\n")
                f.write(f"    def __init__(self):\n")
                f.write(f"        pass\n\n")
                
                f.write(f"{self.save(model=model, nombre=nombre)}\n")
                f.write(f"{self.get_by_id(model=model, nombre=nombre)}\n")
                f.write(f"{self.exists_by_id(model=model, nombre=nombre)}\n")
                f.write(f"{self.get_all(model=model, nombre=nombre)}\n")
                f.write(f"{self.delete(model=model, nombre=nombre)}\n")
        except Exception as e:
            raise Exception(e)
        
    def save(self, model:ModelEntity, nombre:str):
        return (
            f"    @abstractmethod\n"
            f"    def save(self, obj: {nombre}Entity)-> {nombre}Entity:\n"
            f"        pass\n"
        )
    
    def get_by_id(self,model:ModelEntity, nombre:str):
        return (
            f"    @abstractmethod\n"
            f"    def get_by_id(self, id)-> {nombre}Entity :\n"
            f"        pass\n"
        )
    
    def exists_by_id(self,model:ModelEntity, nombre:str):
        return (
            f"    @abstractmethod\n"
            f"    def exists_by_id(self, id)-> bool:\n"
            f"        pass\n"
        )
    
    def get_all(self,model:ModelEntity, nombre:str):
        return (
            f"    @abstractmethod\n"
            f"    def get_all(self)-> list[{nombre}Entity]:\n"
            f"        pass\n"
        )
    
    def delete(self,model:ModelEntity, nombre:str):
        return (
            f"    @abstractmethod\n"
            f"    def delete(self, id)-> bool:\n"
            f"        pass\n"
        )
        
        