import os
from app_content.application.interface.backend.usecase import UseCase
from app_content.application.interface.generator import Generator

class PythonUseCase(UseCase, Generator):

    def execute(self,):
        ''' Generate the files for the model '''
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        path = os.path.join(self.basepath, "application", "usecases")
        os.makedirs(path, exist_ok=True)

        file_path = os.path.join(path, f"{self.model.nombre}_usecase.py")
        try:
            with open(file_path, "w") as f:
                f.write(f"from {self.basepath.replace('/','.')}.domain.entities.{self.model.nombre}_entity import {nombre}Entity\n\n")
                f.write(f"from {self.basepath.replace('/','.')}.application.repositories.{self.model.nombre}_repository import {nombre}Repository\n\n")

                f.write(f"class {nombre}UseCase:\n")
                f.write(f"    def __init__(self, repository: {nombre}Repository):\n")
                f.write(f"        self.repository = repository\n\n")

                f.write(f"{self.get()}\n")
                f.write(f"{self.create()}\n")
                f.write(f"{self.update()}\n")
                f.write(f"{self.delete()}\n")
        except Exception as e:
            raise Exception(e)
            
    def get(self, )->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
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
    
    def create(self,)->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        campos1 = []
        campos2 = []
        for field in self.model.fields:
            if field.nombre != 'id':
                campos1.append(field)
            if not field.tipo.__contains__('None') and field.nombre != 'id':
                campos2.append(field)

        return (f"    def create(self, {', '.join([f'{field.nombre}:{field.tipo}' for field in campos1])})-> {nombre}Entity:\n"
                f"        if not all([{(', ').join([f'{field.nombre}' for field in campos2])}]):\n"
                f"            raise Exception(\"Todos los campos son obligatorios: {', '.join([f'{field.nombre}' for field in campos2])}\")\n"
                f"        try:\n"
                f"            obj = self.repository.save({nombre}Entity(\n{',\n'.join([\
                f"                {field.nombre}={field.nombre if field.nombre != 'id'\
                                  else 'None'}" for field in self.model.fields])}))\n"
                f"            if not obj:\n"
                f"                raise Exception(\"No se pudo crear el registro\")\n"
                f"            return obj\n"
                f"        except Exception as e:\n"
                f"            raise Exception(f\"No se pudo crear el registro: {{e}}\")\n"
                )
    
    def update(self,)->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
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
    
    def delete(self,)->str:
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