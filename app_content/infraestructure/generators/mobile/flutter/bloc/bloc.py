import os
from app_content.application.interface.mobile.bloc import Bloc
from app_content.application.interface.generator import Generator

class FlutterBloc(Bloc, Generator):
    def execute(self,):
        ''' Generate the files for the model '''
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        path = os.path.join(self.basepath, "infraestructure", "blocs", f"{self.model.nombre}")
        os.makedirs(path, exist_ok=True)

        file_path = os.path.join(path, f"{self.model.nombre}_bloc.dart")
        try:
            with open(file_path, 'w') as f:
                # f.write(f"{self.flutterimports()}\n")
                f.write(f"{self.blocclass()}\n")
        except Exception as e:
            raise Exception(e)
        
    def flutterimports(self,)->str:
        return (
            f"import 'package:bloc/bloc.dart';\n"
            f"import 'package:equatable/equatable.dart';\n"
            f"import 'package:lib/infraestructure/blocs/{self.model.nombre}/{self.model.nombre}_event.dart';\n"
            f"import 'package:lib/infraestructure/blocs/{self.model.nombre}/{self.model.nombre}_state.dart';\n"
        )
    
    def blocclass(self,)->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"class {nombre}Bloc extends Bloc<{nombre}Event, {nombre}State> {{\n"
            f"    final {nombre}UseCase uc;\n"
            f"    {nombre}Bloc({{{nombre}UseCase? uc}}) : uc = uc ?? {nombre}UseCase(gateway: ApiGateway()), super({nombre}StateInitial()) {{\n"
            f"        on<{nombre}EventLoad>(_onLoad);\n"
            f"        on<{nombre}EventCreate>(_onCreate);\n"
            f"        on<{nombre}EventUpdate>(_onUpdate);\n"
            f"        on<{nombre}EventDelete>(_onDelete);\n\n"
            f"    }}\n"
            f"{self.get()}\n"
            f"{self.create()}\n"
            f"{self.update()}\n"
            f"{self.delete()}\n"
            f"}}\n"
        )
    
    def get(self, )->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"    Future<void> _onLoad({nombre}EventLoad event, Emitter<{nombre}State> emit) async {{\n"
            f"        emit(const {nombre}StateLoading());\n"
            f"        try {{\n"
            f"            emit({nombre}StateLoading());\n"
            f"            final list = await uc.get(id:event.id);\n"
            f"            emit({nombre}StateLoaded(obj:list));\n"
            f"        }} catch (e) {{\n"
            f"            emit({nombre}StateError(message:e.toString()));\n"
            f"        }}\n"
            f"    }}\n"
        )
    
    def create(self, )->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        campos = [field for field in self.model.fields if field.nombre != 'id']
        return (
            f"    Future<void> _onCreate({nombre}EventCreate event, Emitter<{nombre}State> emit) async {{\n"
            f"        emit(const {nombre}StateLoading());\n"
            f"        try {{\n"
            f"            emit({nombre}StateLoading());\n"
            f"            final obj = await uc.post({(', ').join([f'{field.nombre}: event.{field.nombre}' for field in campos])});\n"
            f"            emit({nombre}StateSuccess(obj:obj));\n"
            f"        }} catch (e) {{\n"
            f"            emit({nombre}StateError(message:e.toString()));\n"
            f"        }}\n"
            f"    }}\n"
        )
    
    def update(self, )-> str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"    Future<void> _onUpdate({nombre}EventUpdate event, Emitter<{nombre}State> emit) async {{\n"
            f"        emit(const {nombre}StateLoading());\n"
            f"        try {{\n"
            f"            emit({nombre}StateLoading());\n"
            f"            final obj = await uc.put(id: event.id, payload: event.payload);\n"
            f"            emit({nombre}StateSuccess(obj:obj));\n"
            f"        }} catch (e) {{\n"
            f"            emit({nombre}StateError(message:e.toString()));\n"
            f"        }}\n"
            f"    }}\n"
        )
    
    def delete(self, )-> str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"    Future<void> _onDelete({nombre}EventDelete event, Emitter<{nombre}State> emit) async {{\n"
            f"        emit(const {nombre}StateLoading());\n"
            f"        try {{\n"
            f"            emit({nombre}StateLoading());\n"
            f"            final obj = await uc.delete(id: '${{event.id}}');\n"
            f"            emit({nombre}StateSuccess(obj:null, message: obj['success']));\n"
            f"        }} catch (e) {{\n"
            f"            emit({nombre}StateError(message:e.toString()));\n"
            f"        }}\n"
            f"    }}\n"
        )