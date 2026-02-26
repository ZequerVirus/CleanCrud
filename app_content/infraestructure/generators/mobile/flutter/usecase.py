from app_content.application.interface.backend.usecase import UseCase
import os
from app_content.application.interface.generator import Generator

class FlutterUseCase(UseCase, Generator):
    def execute(self, ):
        ''' Generate the files for the model '''
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        path = os.path.join(self.basepath, "application", "usecases")
        os.makedirs(path, exist_ok=True)

        file_path = os.path.join(path, f"{self.model.nombre}_usecase.dart")
        try:
            with open(file_path, 'w') as f:
                # f.write(f"{self.flutterimports()}\n")
                f.write(f"{self.usecaseclass()}\n")
        except Exception as e:
            raise Exception(e)
        
    def flutterimports(self, )->str:
        return (
            f"import 'package:lib/domain/usecases/{self.model.nombre}/{self.model.nombre}_usecase.dart';\n"
            f"import 'package:lib/infraestructure/blocs/{self.model.nombre}/{self.model.nombre}_event.dart';\n"
            f"import 'package:lib/infraestructure/blocs/{self.model.nombre}/{self.model.nombre}_state.dart';\n"
            f"import 'package:lib/infraestructure/blocs/{self.model.nombre}/{self.model.nombre}_bloc.dart';\n"
        )
    
    def usecaseclass(self, )->str:
        return (
            f"class {self.model.nombre}UseCase {{\n"
            f"  final Gateway gateway;\n"
            f"  {self.model.nombre}UseCase({{required this.gateway}});\n\n"
            f"  {self.get()}\n"
            f"  {self.create()}\n"
            f"  {self.update()}\n"
            f"  {self.delete()}\n"
            f"}}\n"
        )

    def get(self,)->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"Future<List<{nombre}Entity?>> get({{String? id}}) async {{\n"
            f"    try{{\n"
            f"    final response = await gateway.get(path:'{nombre.lower()}/${{id ?? \"\"}}');\n"
            f"    final obj = response['obj'];\n"
            f"    if (obj != null || obj.isNotEmpty) {{\n"
            f"        if (obj is List) {{\n"
            f"            return obj.map((e) => {nombre}Entity.fromJson(e)).toList();\n"
            f"        }}\n"
            f"        return [{nombre}Entity.fromJson(obj)];\n"
            f"    }}\n"
            f"    return [];\n"
            f"    }} catch (e) {{\n"
            f"     return [];\n"
            f"    }}\n"
            f"}}\n"
        )
    
    def create(self,)->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        campos = [field for field in self.model.fields if field.nombre != 'id']
        return (
            f"Future<{nombre}Entity?> post({{{(', ').join([f'required {field.tipo} {field.nombre}' \
            if not field.tipo.__contains__('?') else f'{field.tipo} {field.nombre}' for field in campos])}}}) async {{\n"
            f"    try {{\n"
            f"    final response = await gateway.post(path:'{nombre.lower()}/', body:{{{(', ').join([f'\'{field.nombre}\': {field.nombre}' for field in campos])}}});\n"
            f"    final obj = response['obj'];\n"
            f"    if (obj == null || obj.isEmpty) {{\n"
            f"        throw Exception('Error creando {self.model.nombre}: ${{obj}}');}}\n"
            f"    return {nombre}Entity.fromJson(obj);\n"
            f"    }} catch (e) {{\n"
            f"    throw Exception('Error creando {self.model.nombre}: ${{e}}');\n"
            f"    }}\n"
            f"}}\n" 
        )
    
    def update(self,)->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"Future<{nombre}Entity?> put({{required String id, required Map<String, dynamic> payload}}) async {{\n"
            f"    try{{\n"
            f"    final response = await gateway.put(path:'{nombre.lower()}/', body:{{'id': id, ...payload}});\n"
            f"    final obj = response['obj'];\n"
            f"    if (obj == null || obj.isEmpty) {{\n"
            f"        throw Exception('Error actualizando {self.model.nombre}: ${{obj}}');}}\n"
            f"        return {nombre}Entity.fromJson(obj);\n"
            f"    }} catch (e) {{\n"
            f"    throw Exception('Error actualizando {self.model.nombre}: ${{e}}');\n"
            f"    }}\n"
            f"}}\n"
        )
    
    def delete(self,)->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"Future<Map<String, dynamic>> delete({{required String id}}) async {{\n"
            f"    try{{\n"
            f"    final response = await gateway.delete(path:'{nombre.lower()}/?id=${{id}}');\n"
            f"    return response;\n"
            f"    }} catch (e) {{\n"
            f"    throw Exception('Error eliminando {self.model.nombre}: ${{e}}');\n"
            f"    }}\n"
            f"}}\n"
        )