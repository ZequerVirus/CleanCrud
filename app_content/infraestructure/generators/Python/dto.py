# from app_content.domain.entities.model_entity import ModelEntity
# import os

# class PythonDTO:
#     def __init__(self, model: ModelEntity, basepath: str,):
#         self.model = model
#         self.basepath = basepath
#         self.nombre = f"{model.nombre[0].capitalize()}{model.nombre[1:]}"

#     def execute(self, ):
#         ''' Generate the files for the model '''
#         path = os.path.join(self.basepath, "domain", "dtos")
#         os.makedirs(path, exist_ok=True)

#         file_path = os.path.join(path, f"{self.model.nombre}_dto.py")
#         try:
#             with open(file_path, "w") as f:
#                 f.write(f"from dataclasses import dataclass\n\n")
#                 f.write(f"@dataclass(kw_only=True)\n")
#                 f.write(f"class {self.nombre}DTOInput:\n")
#                 for field in self.model.fields:
#                     f.write(f"    {field.nombre}: {field.tipo}\n\n")
#                     # MODIFICAR PORQUE FALTA CODIFICAR EL OUTPUT
#         except Exception as e:
#             raise Exception(e)
    