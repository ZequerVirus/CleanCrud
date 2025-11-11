from app_content.domain.entities.model_entity import ModelEntity
import os
from app_content.application.interface.special.bloc import Bloc

class FlutterBloc(Bloc):
    def execute(self, model: ModelEntity, basepath: str,):
        ''' Generate the files for the model '''
        nombre = f"{model.nombre[0].capitalize()}{model.nombre[1:]}"
        path = os.path.join(basepath, "infraestructure", "blocs", f"{model.nombre}")
        os.makedirs(path, exist_ok=True)

        file_path = os.path.join(path, f"{model.nombre}_bloc.dart")
        try:
            with open(file_path, 'w') as f:
                # f.write(f"{self.flutterimports(model=model, nombre=nombre)}\n")
                f.write(f"{self.blocclass(model=model, nombre=nombre)}\n")
        except Exception as e:
            raise Exception(e)
        
    def flutterimports(self, model: ModelEntity, nombre:str)->str:
        return (
            f"import 'package:bloc/bloc.dart';\n"
            f"import 'package:equatable/equatable.dart';\n"
            f"import 'package:lib/infraestructure/blocs/{model.nombre}/{model.nombre}_event.dart';\n"
            f"import 'package:lib/infraestructure/blocs/{model.nombre}/{model.nombre}_state.dart';\n"
        )
    
    def blocclass(self, model: ModelEntity, nombre:str)->str:
        return (
            f"class {nombre}Bloc extends Bloc<{nombre}Event, {nombre}State> {{\n"
            f"    final {nombre}UseCase uc;\n"
            f"    {nombre}Bloc({{{nombre}UseCase? uc}}) : uc = uc ?? {nombre}UseCase(gateway: ApiGateway()), super({nombre}StateInitial()) {{\n"
            f"        on<{nombre}EventLoad>(_onLoad);\n"
            f"        on<{nombre}EventCreate>(_onCreate);\n"
            f"        on<{nombre}EventUpdate>(_onUpdate);\n"
            f"        on<{nombre}EventDelete>(_onDelete);\n\n"
            f"    }}\n"
            f"{self.get(model=model, nombre=nombre)}\n"
            f"{self.create(model=model, nombre=nombre)}\n"
            f"{self.update(model=model, nombre=nombre)}\n"
            f"{self.delete(model=model, nombre=nombre)}\n"
            f"}}\n"
        )
    
    def get(self, model: ModelEntity, nombre:str)->str:
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
    
    def create(self, model: ModelEntity, nombre:str)->str:
        campos = [field for field in model.fields if field.nombre != 'id']
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
    
    def update(self, model: ModelEntity, nombre: str)-> str:
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
    
    def delete(self, model: ModelEntity, nombre: str)-> str:
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