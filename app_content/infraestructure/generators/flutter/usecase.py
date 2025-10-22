from app_content.application.interface.usecase import UseCase
from app_content.domain.entities.model_entity import ModelEntity
import os

class FlutterUseCase(UseCase):
    def execute(self, model: ModelEntity, basepath: str,):
        ''' Generate the files for the model '''
        nombre = f"{model.nombre[0].capitalize()}{model.nombre[1:]}"
        path = os.path.join(basepath, "application", "usecases")
        os.makedirs(path, exist_ok=True)

        file_path = os.path.join(path, f"{model.nombre}_usecase.dart")
        try:
            with open(file_path, 'w') as f:
                f.write(f"{self.flutterimports(model=model, nombre=nombre)}\n")
                f.write(f"{self.usecaseclass(model=model, nombre=nombre)}\n")
        except Exception as e:
            raise Exception(e)
        
    def flutterimports(self, model:ModelEntity, nombre:str)->str:
        return (
            f"import 'package:lib/domain/usecases/{model.nombre}/{model.nombre}_usecase.dart';\n"
            f"import 'package:lib/infraestructure/blocs/{model.nombre}/{model.nombre}_event.dart';\n"
            f"import 'package:lib/infraestructure/blocs/{model.nombre}/{model.nombre}_state.dart';\n"
            f"import 'package:lib/infraestructure/blocs/{model.nombre}/{model.nombre}_bloc.dart';\n"
        )
    
    def usecaseclass(self, model:ModelEntity, nombre:str)->str:
        return (
            f"class {model.nombre}UseCase {{\n"
            f"  final Gateway gateway;\n"
            f"  {model.nombre}UseCase({{required this.gateway}});\n\n"
            f"  {self.get(model=model, nombre=nombre)}\n"
            f"  {self.create(model=model, nombre=nombre)}\n"
            f"  {self.update(model=model, nombre=nombre)}\n"
            f"  {self.delete(model=model, nombre=nombre)}\n"
            f"}}\n"
        )

    def get(self, model:ModelEntity, nombre:str)->str:
        return (
            f"Future<List<{nombre}?>> get({{Map<String, dynamic>? filters}}) async {{\n"
            f"    final urlfilter = filters?.entries.map((e) => '${{e.key}}=${{e.value}}').join('&');\n"
            f"    final response = await gateway.get('{nombre.lower()}/?${{urlfilter ?? ''}}');\n"
            f"    final obj = response['obj'];\n"
            f"    if (obj != null || obj.isNotEmpty) {{\n"
            f"        if (obj is List) {{\n"
            f"            return obj.map((e) => {nombre}.fromJson(e)).toList();\n"
            f"        }}\n"
            f"        return [{nombre}.fromJson(obj)];\n"
            f"    }}\n"
            f"    return [];\n"
            f"}}\n"
        )
    
    def create(self, model:ModelEntity, nombre:str)->str:
        campos = [field for field in model.fields if field.nombre != 'id']
        return (
            f"Future<Map<String, dynamic>> post({{{(', ').join([f'required {field.tipo} {field.nombre}' \
            if not field.tipo.__contains__('?') else f'{field.tipo} {field.nombre}' for field in campos])}}}) async {{\n"
            f"    final response = await gateway.post('{nombre.lower()}/', {{{(', ').join([f'\'{field.nombre}\': {field.nombre}' for field in campos])}}});\n"
            f"    return response;\n"
            f"}}\n" 
        )
    
    def update(self, model:ModelEntity, nombre:str)->str:
        return (
            f"Future<Map<String, dynamic>> put({{required String id, required Map<String, dynamic> payload}}) async {{\n"
            f"    final response = await gateway.put('{nombre.lower()}/', {{'id': id, ...payload}});\n"
            f"    return response;\n"
            f"}}\n"
        )
    
    def delete(self, model:ModelEntity, nombre:str)->str:
        return (
            f"Future<Map<String, dynamic>> delete({{required String id}}) async {{\n"
            f"    final response = await gateway.delete('{nombre.lower()}/?id=${{id}}');\n"
            f"    return response;\n"
            f"}}\n"
        )