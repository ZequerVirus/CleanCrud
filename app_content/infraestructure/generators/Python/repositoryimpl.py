import os
from app_content.domain.entities.model_entity import ModelEntity
from app_content.application.interface.repositoryimpl import RepositoryImpl

class PythonRepositoryImpl(RepositoryImpl):

    def execute(self, model: ModelEntity, basepath: str,):
        ''' Generate the files for the model '''
        nombre = f"{model.nombre[0].capitalize()}{model.nombre[1:]}"
        path = os.path.join(basepath, "infraestructure", "repositories")
        os.makedirs(path, exist_ok=True)

        file_path = os.path.join(path, f"django{model.nombre}_repository.py")
        try:
            with open(file_path, "w") as f:
                f.write(f"from {basepath}.application.repositories.{model.nombre}_repository import {nombre}Repository\n")
                f.write(f"from {basepath}.domain.entities.{model.nombre}_entity import {nombre}Entity\n\n")
                f.write(f"from {basepath}.models import {model.nombre}\n")
                f.write(f"from django.utils import timezone\n\n")

                f.write(f"class Django{nombre}Repository({nombre}Repository):\n")
                f.write(f"    def __init__(self):\n")
                f.write(f"        pass\n\n")
                
                f.write(f"{self.map( model=model, nombre=nombre)}\n")
                f.write(f"{self.save(model=model, nombre=nombre)}\n")
                f.write(f"{self.get(model=model, nombre=nombre)}\n")
                f.write(f"{self.get_by_id(model=model, nombre=nombre)}\n")
                f.write(f"{self.exists_by_id(model=model, nombre=nombre)}\n")
                f.write(f"{self.get_all(model=model, nombre=nombre)}\n")
                f.write(f"{self.delete(model=model, nombre=nombre)}\n")
        except Exception as e:
            raise Exception(e)
        
    def map(self, model: ModelEntity, nombre:str)->str:
        return (
            f"    def _map_to_entity(self, instance: {nombre})-> {nombre}Entity:\n"
            f"        if not instance:\n"
            f"            raise Exception(\"El objeto es obligatorio\")\n"
            f"        try:\n"
            f"            return {nombre}Entity(\n"
            f"{",\n".join([f"                {field.nombre}=instance.{field.nombre}" for field in model.fields])}"
            f"            )\n"
            f"        except Exception as e:\n"
            f"            raise Exception(f\"No se pudo mapear el registro: {{e}}\")\n"
        )
        
    def save(self, model: ModelEntity, nombre:str)->str:
        return (
            f"    def save(self, obj: {nombre}Entity)-> {nombre}Entity:\n"
            f"        if not obj:\n"
            f"            raise Exception(\"El objeto es obligatorio\")\n"
            f"        try:\n"
            f"            if not obj.id:\n"
            f"                instance = {nombre}()\n"
            f"                instance.created_at = timezone.now()\n"
            f"            else:\n"
            f"                instance = {nombre}.objects.get(id=obj.id, deleted_at=None)\n"
            f"{"\n".join([f'            instance.{field.nombre} = obj.{field.nombre}' for field in model.fields])}" 
            f"            instance.updated_at = timezone.now()\n"
            f"            instance.deleted_at = instance.deleted_at\n"
            f"            instance.created_at = instance.created_at\n"
            f"            instance.save()\n"
            f"            return _map_to_entity(instance)\n"
            f"        except Exception as e:\n"
            f"            raise Exception(f\"No se pudo guardar el registro: {{e}}\")\n"
        )
        
    def get(self, model: ModelEntity, nombre:str)->str:
        return (
            f"    def get(self, **kwargs)-> list[{nombre}Entity]| {nombre}Entity:\n"
            f"        try:\n"
            f"            kwargs.pop(\"deleted_at\", None)\n"
            f"            kwargs.pop(\"password\", None)\n"
            f"            return [_map_to_entity(instance) for instance in {nombre}.objects.filter(**kwargs, deleted_at=None)]\n"
            f"        except Exception as e:\n"
            f"            raise Exception(f\"No se pudo obtener el registro: {{e}}\")\n"
        )
    
    def get_by_id(self,model: ModelEntity, nombre:str)->str:
        return (
            f"    def get_by_id(self, id)-> {nombre}Entity :\n"
            f"        if not id:\n"
            f"            raise Exception(\"El id es obligatorio\")\n"
            f"        try:\n"
            f"            return _map_to_entity({nombre}.objects.get(id=id, deleted_at=None))\n"
            f"        except Exception as e:\n"
            f"            raise Exception(f\"No se pudo obtener el registro: {{e}}\")\n"
        )
    
    def exists_by_id(self,model: ModelEntity, nombre:str)->str:
        return (
            f"    def exists_by_id(self, id)-> bool:\n"
            f"        if not id:\n"
            f"            raise Exception(\"El id es obligatorio\")\n"
            f"        try:\n"
            f"            return {nombre}.objects.filter(id=id, deleted_at=None).exists()\n"
            f"        except Exception as e:\n"
            f"            raise Exception(f\"No se pudo obtener el registro: {{e}}\")\n"
        )
    
    def get_all(self,model: ModelEntity, nombre:str)->str:
        return (
            f"    def get_all(self)-> list[{nombre}Entity]:\n"
            f"        try:\n"
            f"            return [_map_to_entity(instance) for instance in {nombre}.objects.filter(deleted_at=None)]\n"
            f"        except Exception as e:\n"
            f"            raise Exception(f\"No se pudo obtener el registro: {{e}}\")\n"
        )
    
    def delete(self,model: ModelEntity, nombre:str)->str:
        return (
            f"    def delete(self, id)-> bool:\n"
            f"        if not id:\n"
            f"            raise Exception(\"El id es obligatorio\")\n"
            f"        try:\n"
            f"            instance = {nombre}.objects.get(id=id, deleted_at=None)\n"
            f"            instance.deleted_at = timezone.now()\n"
            f"            instance.save()\n"
            f"            return True\n"
            f"        except Exception as e:\n"
            f"            raise Exception(f\"No se pudo eliminar el registro: {{e}}\")\n"
        )
        
        