from app_content.domain.entities.model_entity import ModelEntity
import os
from app_content.application.interface.entity import Entity

class PythonEntity(Entity):

    def execute(self, model: ModelEntity, basepath: str,):
        ''' Generate the files for the model '''
        nombre = f"{model.nombre[0].capitalize()}{model.nombre[1:]}"
        path = os.path.join(basepath, "domain", "entities")
        os.makedirs(path, exist_ok=True)

        file_path = os.path.join(path, f"{model.nombre}_entity.py")
        try:
            with open(file_path, "w") as f:
                f.write(f"from dataclasses import dataclass\n\n")
                f.write(f"@dataclass(kw_only=True)\n")
                f.write(f"class {nombre}Entity:\n")
                for field in model.fields:
                    f.write(f"    {field.nombre}: {field.tipo}\n")
                                
        except Exception as e:
            raise Exception(e)