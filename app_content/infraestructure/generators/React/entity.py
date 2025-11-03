from app_content.domain.entities.model_entity import ModelEntity
import os

class ReactEntity:
    def __init__(self) -> None:
        pass

    def execute(self, model: ModelEntity, basepath: str,):
        ''' Generate the entity for the file'''
        nombre = f"{model.nombre[0].capitalize()}{model.nombre[1:]}"
        path = os.path.join(basepath, "domain", "entities",)
        os.makedirs(path, exist_ok=True)
        filepath = os.path.join(path, f"{model.nombre}_entity.ts")
        try:
            with open(filepath, "w") as f:
                f.write(f"{self.__entity(model=model, nombre=nombre)}\n")
        except Exception as e:
            raise Exception(e)
        
    def __entity(self, model: ModelEntity, nombre: str)->str:
        return (
            f"export class {nombre}Entity {{  {('\n').join([f'{field.nombre}: {field.tipo if field.nombre != "id" else field.tipo+" | null"};' for field in model.fields])}\n}}\n"
            f"constructor({{ {(', ').join([f'{field.nombre}:{field.tipo if field.nombre != "id" else field.tipo+" | null"}' for field in model.fields]) }}}){{\n"
            f"{(' \n').join([f'this.{field.nombre} = {field.nombre};' for field in model.fields])}\n"
            f"}}\n"
        )