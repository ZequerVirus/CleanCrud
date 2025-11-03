from app_content.domain.entities.model_entity import ModelEntity
import os

class ReactUseCase:
    def __init__(self) -> None:
        pass

    def execute(self, model: ModelEntity, basepath: str,):
        ''' Generate the Use Case for the file '''
        nombre = f"{model.nombre[0].capitalize()}{model.nombre[1:]}"
        path = os.path.join(basepath, "application", "usecases")
        os.makedirs(path, exist_ok=True)
        filepath = os.path.join(path, f"{model.nombre}_uc.ts")
        try:
            with open(filepath, "w") as f:
                f.write(f"{self.__imports(model=model, nombre=nombre,)}\n")
                f.write(f"{self.__usecase(model=model, nombre=nombre)}\n")
        except Exception as e:
            raise Exception(e)
        
    def __imports(self, model: ModelEntity, nombre: str,):
        return (f"import {{{nombre}Entity}} from '../../domain/entities/{model.nombre}_entity';")
    
    def __usecase(self, model: ModelEntity, nombre: str,)->str:
        return (
            f"export class {nombre}UseCase {{\n"
            f"  api: Gateway;\n"
            f"  constructor(api: Gateway) {{\n"
            f"    this.api = api;\n"
            f"  }}\n"
            f"\n"
            f"{self.__get(model=model, nombre=nombre)}\n"
            f"{self.__create(model=model, nombre=nombre)}\n"
            f"{self.__update(model=model, nombre=nombre)}\n"
            f"{self.__delete(model=model, nombre=nombre)}\n"
            f"}}\n"
            )
    
    def __get(self, model: ModelEntity, nombre: str,)->str:
        return (
            f"async get(id?:string): Promise<any>{{\n"
            f"  try {{\n"
            f"    const response = await this.api.get(`{nombre.lower()}/${{id??''}}`);\n"
            f"    if (response.status < 200 || response.status > 299 ){{throw Error(`Error obteniendo {model.nombre}`)}}\n"
            f"    if (Array.isArray(response.obj)) {{\n"
            f"      return response.obj.map((item: Record<string, any>) => {{\n"
            f"        return new {nombre}Entity(\n"
            f"{',\n'.join([f"          item.{field.nombre}" for field in model.fields])});\n"
            f"        }});\n"
            f"    }} else\n{{"
            f"      return [];\n"
            f"    }} }} catch (error) {{\n"
            f"      throw Error(`Error obteniendo {model.nombre}: ${{error}}`);\n"
            f"    }}\n"
            f"  }}\n"
        )
    
    def __create(self, model: ModelEntity, nombre: str,)->str:
        return (
            f"async create(data:any):Promise<any> {{\n"
            f"try{{\n"
            f"const response = await this.api.post(`{nombre.lower()}`, {{\n"
            f"{',\n'.join([f"          {field.nombre}: data.{field.nombre}" for field in model.fields])}\n"
            f"        }});\n"
            f"if (response.status < 200 || response.status > 299 ){{throw Error(`Error creando {model.nombre}`)}}\n"
            f"if (Array.isArray(response.created)) {{\n"
            f"  return response.created.map((item: Record<string, any>) => {{\n"
            f"    return new {nombre}Entity(\n"
            f"{',\n'.join([f"          item.obj.{field.nombre}" for field in model.fields])});\n"
            f"    }});\n"
            f"  }}\n"
            f"  return new {nombre}Entity(\n"
            f"{',\n'.join([f"          response.obj.{field.nombre}" for field in model.fields])});\n"
            f"  }}catch(error){{\n"
            f"    throw Error(`Error creando {model.nombre}: ${{error}}`);\n"
            f"  }}\n"
            f"}}\n"
        )
    
    def __update(self, model: ModelEntity, nombre: str,)->str:
        return (
            f"async update(id:string, data:any):Promise<any> {{\n"
            f"try{{\n"
            f"const response = await this.api.put(`{nombre.lower()}`, id, {{\n"
            f"{',\n'.join([f"          '{field.nombre}': data.{field.nombre}" for field in model.fields])}\n"
            f"        }});\n"
            f"if (response.status < 200 || response.status > 299 ){{throw Error(`Error actualizando {model.nombre}`)}}\n"
            f"if (Array.isArray(response.obj)) {{\n"
            f"  return response.obj.map((item: Record<string, any>) => {{\n"
            f"    return new {nombre}Entity(\n"
            f"{',\n'.join([f"          item.obj.{field.nombre}" for field in model.fields])});\n"
            f"}});\n"
            f"  }}\n"
            f"  return new {nombre}Entity(\n"
            f"{',\n'.join([f"          response.obj.{field.nombre}" for field in model.fields])});\n"
            f"    }}catch(error){{\n"
            f"      throw Error(`Error actualizando {model.nombre}: ${{error}}`);\n"
            f"    }}\n"
            f"  }}\n"
        )
    
    def __delete(self, model: ModelEntity, nombre:str)->str:
        return (
            f"async delete(id:string):Promise<any> {{\n"
            f"try{{\n"
            f"  const response = await this.api.delete(`{nombre.lower()}/${{id}}`);\n"
            f"  if (response.status < 200 || response.status > 299 ){{throw Error(`Error eliminando {model.nombre}`)}}\n"
            f"  return response;\n"
            f"}}catch(error){{\n"
            f"  throw Error(`Error eliminando {model.nombre}: ${{error}}`);\n"
            f"}}\n"
            f"}}\n"
        )