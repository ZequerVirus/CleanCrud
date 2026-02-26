from app_content.application.interface.mobile.event import Event
import os
from app_content.application.interface.generator import Generator

class FlutterEvent(Event, Generator):
    def execute(self,):
        ''' Generate the files for the model '''
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        path = os.path.join(self.basepath, "infraestructure", "blocs", f"{self.model.nombre}")
        os.makedirs(path, exist_ok=True)

        file_path = os.path.join(path, f"{self.model.nombre}_event.dart")
        try:
            with open(file_path, 'w') as f:
                f.write(f"{self.flutterimports()}\n")
                f.write(f"{self.eventclass()}\n")
        except Exception as e:
            raise Exception(e)
        
    def flutterimports(self,)->str:
        return (
            f"import 'package:equatable/equatable.dart';\n"
        )
    
    def eventclass(self, )->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"abstract class {nombre}Event extends Equatable {{\n"
            f"    const {nombre}Event();\n\n"
            f"    @override\n"
            f"    List<Object> get props => [];\n"
            f"}}\n"

            f"{self.loadevent()}\n"
            f"{self.createevent()}\n"
            f"{self.updateevent()}\n"
            f"{self.deleteevent()}\n"
        )
    
    def loadevent(self,)->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
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
    
    def createevent(self,)->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        campos = [field for field in self.model.fields if field.nombre != 'id']
        return (
            f"class {nombre}EventCreate extends {nombre}Event {{\n"
            f"    {(';\n').join(f'final {field.tipo} {field.nombre}' for field in campos)};\n"
            f"    const {nombre}EventCreate({{{(',').join([f'required this.{field.nombre}' if not field.tipo.__contains__('?') else f'this.{field.nombre}' for field in campos])}}});\n"
            f"    @override\n"
            f"    List<Object> get props => [{(','.join([f'{field.nombre}' for field in campos if not field.tipo.__contains__('?')]))}];\n"
            f"}}\n"
        )
    
    def updateevent(self,)->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"class {nombre}EventUpdate extends {nombre}Event {{\n"
            f"    final String id;\n"
            f"    final Map<String, dynamic> payload;\n"
            f"    const {nombre}EventUpdate({{required this.id, required this.payload}});\n"
            f"    @override\n"
            f"    List<Object> get props => [id, payload];\n"
            f"}}\n"
        )
    
    def deleteevent(self,)->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"class {nombre}EventDelete extends {nombre}Event {{\n"
            f"    final int id;\n"
            f"    const {nombre}EventDelete({{required this.id}});\n"
            f"    @override\n"
            f"    List<Object> get props => [id];\n"
            f"}}\n"
        )