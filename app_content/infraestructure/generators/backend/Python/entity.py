import os
from app_content.application.interface.backend.entity import Entity
from app_content.application.interface.generator import Generator

class PythonEntity(Entity, Generator):

    def execute(self,):
        ''' Generate the files for the model '''
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        path = os.path.join(self.basepath, "domain", "entities")
        os.makedirs(path, exist_ok=True)

        file_path = os.path.join(path, f"{self.model.nombre}_entity.py")
        try:
            with open(file_path, "w") as f:
                f.write(f"from dataclasses import dataclass\n\n")
                f.write(f"@dataclass(kw_only=True)\n")
                f.write(f"class {nombre}Entity:\n")
                for field in self.model.fields:
                    f.write(f"    {field.nombre}: {field.tipo if field.nombre != 'id' else field.tipo+' | None'}\n")
                                
        except Exception as e:
            raise Exception(e)