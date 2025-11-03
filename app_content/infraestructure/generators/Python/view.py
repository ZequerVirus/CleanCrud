from app_content.domain.entities.model_entity import ModelEntity
import os
from app_content.application.interface.view import View

class PythonView(View):
    def execute(self, model: ModelEntity, basepath: str,):
        ''' Generate the files for the model '''
        nombre = f"{model.nombre[0].capitalize()}{model.nombre[1:]}"
        path = os.path.join(basepath, "presentation", "views")
        os.makedirs(path, exist_ok=True)

        file_path = os.path.join(path, f"{model.nombre}_view.py")
        try:
            with open(file_path, "w") as f:
                f.write(f"from {basepath.replace('/','.')}.application.usecases.{model.nombre}_usecase import {nombre}UseCase\n")
                f.write(f"from {basepath.replace('/','.')}.infraestructure.repositories.django{model.nombre}_repository import Django{nombre}Repository\n")
                f.write(f"from rest_framework.views import APIView\n")
                f.write(f"from rest_framework.response import Response\n")
                f.write(f"from rest_framework import status\n")
                f.write(f"from rest_framework.permissions import AllowAny\n\n")

                f.write(f"class {nombre}View(APIView):\n")
                f.write(f"    permission_classes = [AllowAny]\n")
                f.write(f"    def __init__(self):\n")
                f.write(f"        pass\n\n")

                f.write(f"{self.get(model=model, nombre=nombre)}\n")
                f.write(f"{self.post(model=model, nombre=nombre)}\n")
                f.write(f"{self.put(model=model, nombre=nombre)}\n")
                f.write(f"{self.delete(model=model, nombre=nombre)}\n")
        except Exception as e:
            raise Exception(e)
        
    def post(self,model: ModelEntity, nombre:str):
        campos = []
        for field in model.fields:
            if field.nombre != 'id':
                campos.append(field)

        return (
            f"    def post(self, request):\n"
            f"        if not request.data:\n"
            f"             return Response({{\"error\": \"No se recibieron datos\"}}, status=status.HTTP_400_BAD_REQUEST)\n"
            f"        obj_crud = {nombre}UseCase(repository=Django{nombre}Repository())\n"
            f"        data = request.data\n"
            f"        if isinstance(data, list):\n"
            f"            created = []\n"
            f"            failed = []\n"
            f"            for idx, item in enumerate(data):\n"
            f"                try:\n"
            f"                    obj = obj_crud.create({(','.join([f'{field.nombre}=item.get(\"{field.nombre}\")' for field in campos]))})\n"
            f"                    if obj:\n"
            f"                        created.append({{'index': idx, 'obj': obj.__dict__}})\n"
            f"                    else:\n"
            f"                        failed.append({{'index': idx, 'error': 'No se pudo crear el registro'}})\n"
            f"                except Exception as e:\n"
            f"                    failed.append({{'index': idx, 'error': str(e)}})\n"
            f"            if created and not failed:\n"
            f"                return Response({{'created': created}}, status=status.HTTP_201_CREATED)\n"
            f"            elif created and failed:\n"
            f"                multi_status = getattr(status, 'HTTP_207_MULTI_STATUS', status.HTTP_200_OK)\n"
            f"                return Response({{'created': created, 'failed': failed}}, status=multi_status)\n"
            f"            else:\n"
            f"                return Response({{'failed': failed}}, status=status.HTTP_400_BAD_REQUEST)\n"
            f"        try:\n"
            f"            obj = obj_crud.create({", ".join([f'{field.nombre}=data.get(\'{field.nombre}\')' for field in campos])})\n"
            f"            return Response({{'obj': obj.__dict__}}, status=status.HTTP_201_CREATED)\n"
            f"        except Exception as e:\n"
            f"            return Response({{'error': str(e)}}, status=status.HTTP_400_BAD_REQUEST)\n"
            
        )
    
    def get(self, model: ModelEntity, nombre:str):
        return (
            f"    def get(self, request, id=None):\n"
            f"        obj_crud = {nombre}UseCase(repository=Django{nombre}Repository())\n"
            f"        try:\n"
            f"            query_params = request.query_params.dict()\n"
            f"            if id:\n"
            f"                query_params['id'] = id\n"
            f"            obj = obj_crud.get(**query_params)\n"
            f"            if isinstance(obj, list):\n"
            f"                data = [item.__dict__ for item in obj]\n"
            f"            else:\n"
            f"                data = obj.__dict__\n"
            f"            return Response({{'obj': data}}, status=status.HTTP_200_OK)\n"
            f"        except Exception as e:\n"
            f"            return Response({{'error': str(e)}}, status=status.HTTP_404_NOT_FOUND)\n"
        )

    def put(self,model: ModelEntity, nombre:str):
        return (
            f"    def put(self, request):\n"
            f"        if not request.data:\n"
            f"             return Response({{\"error\": \"No se recibieron datos\"}}, status=status.HTTP_400_BAD_REQUEST)\n"
            f"        obj_crud = {nombre}UseCase(repository=Django{nombre}Repository())\n"
            f"        data = {{}}\n"
            f"        for key, value in request.data.items():\n"
            f"            if key != 'id':\n"
            f"                data[key] = value\n"
            f"        try:\n"
            f"            obj = obj_crud.update(request.data.get('id'), **data)\n"
            f"            return Response({{'obj': obj.__dict__}}, status=status.HTTP_200_OK)\n"
            f"        except Exception as e:\n"
            f"            return Response({{'error': str(e)}}, status=status.HTTP_400_BAD_REQUEST)\n"
        )
    
    def delete(self, model: ModelEntity, nombre:str):
        return (
            f"    def delete(self, request, id=None):\n"
            f"        obj_crud = {nombre}UseCase(repository=Django{nombre}Repository())\n"
            f"        try:\n"
            f"            if not id:\n"
            f"                id = request.query_params.get('id')\n"
            f"            obj = obj_crud.delete(id=id)\n"
            f"            if obj:\n"
            f"                return Response({{'success': obj}}, status=status.HTTP_200_OK)\n"
            f"            return Response({{'success': obj}}, status=status.HTTP_200_OK)\n"
            f"        except Exception as e:\n"
            f"            return Response({{'error': str(e)}}, status=status.HTTP_400_BAD_REQUEST)\n"
        )
        