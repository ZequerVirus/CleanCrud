from app_content.domain.entities.model_entity import ModelEntity
import os
from app_content.application.interface.usecase import UseCase

class PythonUseCase(UseCase):

    def execute(self, model: ModelEntity, basepath: str,):
        ''' Generate the files for the model '''
        nombre = f"{model.nombre[0].capitalize()}{model.nombre[1:]}"
        path = os.path.join(basepath, "application", "usecases")
        os.makedirs(path, exist_ok=True)

        file_path = os.path.join(path, f"{model.nombre}_usecase.py")
        try:
            with open(file_path, "w") as f:
                f.write(f"from {basepath.replace('/','.')}.domain.entities.{model.nombre}_entity import {nombre}Entity\n\n")
                f.write(f"from {basepath.replace('/','.')}.application.repositories.{model.nombre}_repository import {nombre}Repository\n\n")

                f.write(f"class {nombre}UseCase:\n")
                f.write(f"    def __init__(self, repository: {nombre}Repository):\n")
                f.write(f"        self.repository = repository\n\n")

                f.write(f"{self.get(model=model, nombre=nombre)}\n")
                f.write(f"{self.create(model=model, nombre=nombre)}\n")
                f.write(f"{self.update(model=model, nombre=nombre)}\n")
                f.write(f"{self.delete(model=model, nombre=nombre)}\n")
        except Exception as e:
            raise Exception(e)
            
    def get(self, model:ModelEntity, nombre:str):
        return (f"    def get(self, **kwargs)->list[{nombre}Entity] | {nombre}Entity:\n"
                f"        try:\n"
                f"            if not id:\n"
                f"                obj = self.repository.get_all()\n"
                f"            else:\n"
                # f"                obj = self.repository.get_by_id(id)\n"
                f"                obj = self.repository.get(**kwargs)\n"
                f"            if obj is None:\n"
                f"                raise Exception(\"No se encontraron registros\")\n"
                f"            return obj\n"
                f"        except Exception as e:\n"
                f"            raise Exception(f\"No se pudo obtener el registro: {{e}}\")\n"
                )
    
    def create(self, model:ModelEntity, nombre:str):
        return (f"    def create(self, {' '.join([(f'{field.nombre}:{field.tipo},' if field.nombre != 'id' \
                                            else '')  for field in model.fields])})-> {nombre}Entity:\n"
                f"        if not all([{' '.join([(f'{field.nombre},' if not field.tipo.__contains__('None') else '') for field in model.fields])}]):\n"
                f"            raise Exception(\"Todos los campos son obligatorios\")\n"
                f"        try:\n"
                f"            obj = self.repository.save(\n{nombre}Entity(\n\
                {',\n'.join([f'                {field.nombre}={field.nombre}' if field.nombre != 'id' else\
                              f'                {field.nombre}=None' for field in model.fields])}\n)\n)\n"
                f"            if not obj:\n"
                f"                raise Exception(\"No se pudo crear el registro\")\n"
                f"            return obj\n"
                f"        except Exception as e:\n"
                f"            raise Exception(f\"No se pudo crear el registro: {{e}}\")\n"
                )
    
    def update(self, model:ModelEntity, nombre:str):
        return (f"    def update(self, id, **kwargs)-> {nombre}Entity:\n"
                f"        if not id:\n"
                f"            raise Exception(\"El id es obligatorio\")\n"
                f"        try:\n"
                f"            obj = self.repository.get_by_id(id)\n"
                f"            if not obj:\n"
                f"                raise Exception(\"No se encontraron registros\")\n"
                f"            data = obj.__dict__\n"
                f"            for key, value in kwargs.items():\n"
                f"                if key in data and key != 'id':\n"
                f"                    data[key] = value\n"
                f"            obj = {nombre}Entity(**data)\n"
                f"            return self.repository.save(obj)\n"
                f"        except Exception as e:\n"
                f"            raise Exception(f\"No se pudo actualizar el registro: {{e}}\")\n"
                )
    
    def delete(self, model:ModelEntity, nombre:str):
        return (f"    def delete(self, id)->bool:\n"
                f"        if not id:\n"
                f"            raise Exception(\"El id es obligatorio\")\n"
                f"        try:\n"
                f"            obj = self.repository.get_by_id(id)\n"
                f"            if not obj:\n"
                f"                raise Exception(\"No se encontraron registros\")\n"
                f"            return self.repository.delete(id)\n"
                f"        except Exception as e:\n"
                f"            raise Exception(f\"No se pudo eliminar el registro: {{e}}\")\n"
                )