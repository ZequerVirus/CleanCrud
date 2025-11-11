from app_content.application.interface.special.state import State
from app_content.domain.entities.model_entity import ModelEntity
import os

class FlutterState(State):
    def execute(self, model: ModelEntity, basepath: str):
        ''' Generate the files for the model '''
        nombre = f"{model.nombre[0].capitalize()}{model.nombre[1:]}"
        path = os.path.join(basepath, "infraestructure", "blocs", f"{model.nombre}")
        os.makedirs(path, exist_ok=True)

        file_path = os.path.join(path, f"{model.nombre}_state.dart")
        try:
            with open(file_path, 'w') as f:
                f.write(f"{self.flutterimports(model=model, nombre=nombre)}\n")
                f.write(f"{self.stateclass(model=model, nombre=nombre)}\n")
        except Exception as e:
            raise Exception(e)

    def flutterimports(self, model: ModelEntity, nombre:str):
        return (
            f"import 'package:equatable/equatable.dart';\n"
        )

    def stateclass(self, model: ModelEntity, nombre:str):
        return (
            f"class {nombre}State extends Equatable {{\n"
            f"    const {nombre}State();\n\n"
            f"    @override\n"
            f"    List<Object> get props => [];\n"
            f"}}\n"

            f"{self.initialstate(model=model, nombre=nombre)}\n"
            f"{self.stateloaded(model=model, nombre=nombre)}\n"
            f"{self.stateerror(model=model, nombre=nombre)}\n" 
            f"{self.stateloading(model=model, nombre=nombre)}\n"
            f"{self.statesuccess(model=model, nombre=nombre)}\n"
        )
    
    def initialstate(self, model: ModelEntity, nombre:str):
        return (
            f"class {nombre}StateInitial extends {nombre}State {{\n"
            f"    const {nombre}StateInitial();\n"
            f"}}\n"
        )
    
    def stateloading(self, model:ModelEntity, nombre:str)->str:
        return (
            f"class {nombre}StateLoading extends {nombre}State {{\n"
            f"    const {nombre}StateLoading();\n"
            f"}}\n"
        )
    
    def stateloaded(self, model:ModelEntity, nombre:str)->str:
        return (
            f"class {nombre}StateLoaded extends {nombre}State {{\n"
            f"    final List<dynamic> obj;\n"
            f"    const {nombre}StateLoaded({{required this.obj}});\n"
            f"    @override\n"
            f"    List<Object> get props => [obj];\n"
            f"}}\n"
        )
    
    def stateerror(self, model:ModelEntity, nombre:str)->str:
        return (
            f"class {nombre}StateError extends {nombre}State {{\n"
            f"    final String message;\n"
            f"    const {nombre}StateError({{required this.message}});\n"
            f"    @override\n"
            f"    List<Object> get props => [message];\n"
            f"}}\n"
        )
    
    def statesuccess(self, model:ModelEntity, nombre:str)->str:
        return (
            f"class {nombre}StateSuccess extends {nombre}State {{\n"
            f"    final String message;\n"
            f"    const {nombre}StateSuccess({{required this.message}});\n"
            f"    @override\n"
            f"    List<Object> get props => [message];\n"
            f"}}\n"
        )