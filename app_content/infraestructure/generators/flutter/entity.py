from app_content.application.interface.entity import Entity
from app_content.domain.entities.model_entity import ModelEntity
import os

class FlutterEntity(Entity):
    def execute(self, model: ModelEntity, basepath: str,):
        ''' Generate the files for the model '''
        nombre = f"{model.nombre[0].capitalize()}{model.nombre[1:]}"
        path = os.path.join(basepath, "domain", "entities")
        os.makedirs(path, exist_ok=True)

        file_path = os.path.join(path, f"{model.nombre}_entity.dart")
        try:
            with open(file_path, "w") as f:
                f.write(f"class {nombre}Entity {{\n")
                for field in model.fields:
                    f.write(f"    final {field.tipo if field.nombre != 'id' else field.tipo+'?'} {field.nombre};\n")
                f.write(f"    {nombre}Entity({{{(', ').join([f'required this.{field.nombre}' \
                if not field.tipo.__contains__('?') else f'this.{field.nombre}' for field in model.fields])}}});\n\n")
                f.write(f"{self.fromjson(model=model, nombre=nombre)}\n")
                f.write(f"{self.tojson(model=model, nombre=nombre)}\n")
                f.write(f"}}\n")
        except Exception as e:
            raise Exception(e)
        
    def fromjson(self, model:ModelEntity, nombre:str)->str:
        return (
            f"factory {nombre}Entity.fromJson(Map<String, dynamic> json) {{\n"
            f"    return {nombre}Entity(\n"
            f"{',\n'.join([f"        {field.nombre}: json[\'{field.nombre}\']" for field in model.fields])},\n"
            f"    );\n"
            f"}}\n"
        )
    
    def tojson(self, model:ModelEntity, nombre:str)->str:
        return (
            f"Map<String, dynamic> toJson() {{\n"
            f"    return {{\n"
            f"{',\n'.join([f"        \'{field.nombre}\': {field.nombre}" for field in model.fields])},\n"
            f"    }};\n"
            f"}}\n"
        )
