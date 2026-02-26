import os
from app_content.application.interface.generator import Generator

class ReactEntity(Generator):
    def __init__(self) -> None:
        pass

    def execute(self, ):
        ''' Generate the entity for the file'''
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        path = os.path.join(self.basepath, "domain", "entities",)
        os.makedirs(path, exist_ok=True)
        filepath = os.path.join(path, f"{self.model.nombre}_entity.ts")
        try:
            with open(filepath, "w") as f:
                f.write(f"{self.__entity()}\n")
        except Exception as e:
            raise Exception(e)
        
    def __entity(self,)->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"export class {nombre}Entity extends TimeStamp {{  {('\n').join([f'{field.nombre}: {field.tipo if field.nombre != "id" else field.tipo+" | null"};' for field in self.model.fields])}\n\n"
            f"constructor({(', ').join([f'{field.nombre}:{field.tipo if field.nombre != "id" else field.tipo+" | null"}' for field in self.model.fields]) }, \
                created_at: Date | null = null, updated_at:Date | null = null, deleted_at:Date | null = null){{\n"
            f"super(created_at, updated_at, deleted_at);\n"
            f"{(' \n').join([f'this.{field.nombre} = {field.nombre};' for field in self.model.fields])}\n"
            f"}}\n"
            f"}}\n"
        )