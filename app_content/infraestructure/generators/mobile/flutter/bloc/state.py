from app_content.application.interface.mobile.state import State
import os
from app_content.application.interface.generator import Generator

class FlutterState(State, Generator):
    def execute(self,):
        ''' Generate the files for the model '''
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        path = os.path.join(self.basepath, "infraestructure", "blocs", f"{self.model.nombre}")
        os.makedirs(path, exist_ok=True)

        file_path = os.path.join(path, f"{self.model.nombre}_state.dart")
        try:
            with open(file_path, 'w') as f:
                f.write(f"{self.flutterimports()}\n")
                f.write(f"{self.stateclass()}\n")
        except Exception as e:
            raise Exception(e)

    def flutterimports(self,):
        return (
            f"import 'package:equatable/equatable.dart';\n"
        )

    def stateclass(self,):
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"class {nombre}State extends Equatable {{\n"
            f"    const {nombre}State();\n\n"
            f"    @override\n"
            f"    List<Object> get props => [];\n"
            f"}}\n"

            f"{self.initialstate()}\n"
            f"{self.stateloaded()}\n"
            f"{self.stateerror()}\n" 
            f"{self.stateloading()}\n"
            f"{self.statesuccess()}\n"
        )
    
    def initialstate(self,)->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"class {nombre}StateInitial extends {nombre}State {{\n"
            f"    const {nombre}StateInitial();\n"
            f"}}\n"
        )
    
    def stateloading(self,)->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"class {nombre}StateLoading extends {nombre}State {{\n"
            f"    const {nombre}StateLoading();\n"
            f"}}\n"
        )
    
    def stateloaded(self,)->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"class {nombre}StateLoaded extends {nombre}State {{\n"
            f"    final List<dynamic> obj;\n"
            f"    const {nombre}StateLoaded({{required this.obj}});\n"
            f"    @override\n"
            f"    List<Object> get props => [obj];\n"
            f"}}\n"
        )
    
    def stateerror(self,)->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"class {nombre}StateError extends {nombre}State {{\n"
            f"    final String message;\n"
            f"    const {nombre}StateError({{required this.message}});\n"
            f"    @override\n"
            f"    List<Object> get props => [message];\n"
            f"}}\n"
        )
    
    def statesuccess(self,)->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"class {nombre}StateSuccess extends {nombre}State {{\n"
            f"    final String? message;\n"
            f"    final dynamic obj;\n"
            f"    const {nombre}StateSuccess({{required this.obj, this.message}});\n"
            f"    @override\n"
            f"    List<Object> get props => [obj];\n"
            f"}}\n"
        )