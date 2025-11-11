from app_content.application.interface.special.event import Event
from app_content.domain.entities.model_entity import ModelEntity
import os

class FlutterEvent(Event):
    def execute(self, model: ModelEntity, basepath: str):
        ''' Generate the files for the model '''
        nombre = f"{model.nombre[0].capitalize()}{model.nombre[1:]}"
        path = os.path.join(basepath, "infraestructure", "blocs", f"{model.nombre}")
        os.makedirs(path, exist_ok=True)

        file_path = os.path.join(path, f"{model.nombre}_event.dart")
        try:
            with open(file_path, 'w') as f:
                f.write(f"{self.flutterimports(model=model, nombre=nombre)}\n")
                f.write(f"{self.eventclass(model=model, nombre=nombre)}\n")
        except Exception as e:
            raise Exception(e)
        
    def flutterimports(self, model: ModelEntity, nombre:str)->str:
        return (
            f"import 'package:equatable/equatable.dart';\n"
        )
    
    def eventclass(self, model: ModelEntity, nombre:str)->str:
        return (
            f"abstract class {nombre}Event extends Equatable {{\n"
            f"    const {nombre}Event();\n\n"
            f"    @override\n"
            f"    List<Object> get props => [];\n"
            f"}}\n"

            f"{self.loadevent(model=model, nombre=nombre)}\n"
            f"{self.createevent(model=model, nombre=nombre)}\n"
            f"{self.updateevent(model=model, nombre=nombre)}\n"
            f"{self.deleteevent(model=model, nombre=nombre)}\n"
        )
    
    def loadevent(self, model: ModelEntity, nombre:str)->str:
        return (
            f"class {nombre}EventLoad extends {nombre}Event {{\n"
            f"    final String? id;\n"
            f"    const {nombre}EventLoad(\n"
            f"        this.id,\n"
            f"    );\n"
            f"    @override\n"
            f"    List<Object> get props => [];\n"
            f"}}\n"
        )
    
    def createevent(self, model:ModelEntity, nombre:str)->str:
        campos = [field for field in model.fields if field.nombre != 'id']
        return (
            f"class {nombre}EventCreate extends {nombre}Event {{\n"
            f"    {(';\n').join(f'final {field.tipo} {field.nombre}' for field in campos)};\n"
            f"    const {nombre}EventCreate({{{(',').join([f'required this.{field.nombre}' if not field.tipo.__contains__('?') else f'this.{field.nombre}' for field in campos])}}});\n"
            f"    @override\n"
            f"    List<Object> get props => [{(','.join([f'{field.nombre}' for field in campos if not field.tipo.__contains__('?')]))}];\n"
            f"}}\n"
        )
    
    def updateevent(self, model: ModelEntity, nombre:str)->str:
        return (
            f"class {nombre}EventUpdate extends {nombre}Event {{\n"
            f"    final String id;\n"
            f"    final Map<String, dynamic> payload;\n"
            f"    const {nombre}EventUpdate({{required this.id, required this.payload}});\n"
            f"    @override\n"
            f"    List<Object> get props => [id, payload];\n"
            f"}}\n"
        )
    
    def deleteevent(self, model: ModelEntity, nombre:str)->str:
        return (
            f"class {nombre}EventDelete extends {nombre}Event {{\n"
            f"    final int id;\n"
            f"    const {nombre}EventDelete({{required this.id}});\n"
            f"    @override\n"
            f"    List<Object> get props => [id];\n"
            f"}}\n"
        )