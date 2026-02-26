import os
from app_content.application.interface.generator import Generator

class ReactUseCase(Generator):
    def __init__(self) -> None:
        pass

    def execute(self,):
        ''' Generate the Use Case for the file '''
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        path = os.path.join(self.basepath, "application", "usecases")
        os.makedirs(path, exist_ok=True)
        filepath = os.path.join(path, f"{self.model.nombre}_uc.ts")
        try:
            with open(filepath, "w") as f:
                f.write(f"{self.__imports()}\n")
                f.write(f"{self.__usecase()}\n")
        except Exception as e:
            raise Exception(e)
        
    def __imports(self,):
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (f"import {{{nombre}Entity}} from '../../domain/entities/{self.model.nombre}_entity';")
    
    def __usecase(self,)->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"export class {nombre}UseCase {{\n"
            f"  api: Gateway;\n"
            f"  constructor(api: Gateway) {{\n"
            f"    this.api = api;\n"
            f"  }}\n"
            f"\n"
            f"{self.__get()}\n"
            f"{self.__create()}\n"
            f"{self.__update()}\n"
            f"{self.__delete()}\n"
            f"}}\n"
            )
    
    def __get(self,)->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"async get(id?:string): Promise<any>{{\n"
            f"  try {{\n"
            f"    const response = await this.api.get(`{nombre.lower()}/${{id??''}}`);\n"
            f"    if (response.status < 200 || response.status > 299 ){{throw Error(`Error obteniendo {self.model.nombre}`)}}\n"
            f"    if (Array.isArray(response.obj)) {{\n"
            f"      return response.obj.map((item: Record<string, any>) => {{\n"
            f"        return new {nombre}Entity(\n"
            f"{',\n'.join([f"          item.{field.nombre}" for field in self.model.fields])}, \
                item.created_at, item.updated_at, item.deleted_at);\n"
            f"        }});\n"
            f"    }} else\n{{"
            f"      return [];\n"
            f"    }} }} catch (error) {{\n"
            f"      throw Error(`Error obteniendo {self.model.nombre}: ${{error}}`);\n"
            f"    }}\n"
            f"  }}\n"
        )
    
    def __create(self,)->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"async create(data:any):Promise<any> {{\n"
            f"try{{\n"
            f"const response = await this.api.post(`{nombre.lower()}/`, {{\n"
            f"{',\n'.join([f"          {field.nombre}: data.{field.nombre}" for field in self.model.fields])}\n"
            f"        }});\n"
            f"if (response.status < 200 || response.status > 299 ){{throw Error(`Error creando {self.model.nombre}`)}}\n"
            f"if (Array.isArray(response.created)) {{\n"
            f"  return response.created.map((item: Record<string, any>) => {{\n"
            f"    return new {nombre}Entity(\n"
            f"{',\n'.join([f"          item.obj.{field.nombre}" for field in self.model.fields])});\n"
            f"    }});\n"
            f"  }}\n"
            f"  return new {nombre}Entity(\n"
            f"{',\n'.join([f"          response.obj.{field.nombre}" for field in self.model.fields])});\n"
            f"  }}catch(error){{\n"
            f"    throw Error(`Error creando {self.model.nombre}: ${{error}}`);\n"
            f"  }}\n"
            f"}}\n"
        )
    
    def __update(self,)->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"async update(id:string, data:any):Promise<any> {{\n"
            f"try{{\n"
            f"const response = await this.api.put(`{nombre.lower()}/`, id, {{\n"
            f"{',\n'.join([f"          '{field.nombre}': data.{field.nombre}" for field in self.model.fields])}\n"
            f"        }});\n"
            f"if (response.status < 200 || response.status > 299 ){{throw Error(`Error actualizando {self.model.nombre}`)}}\n"
            f"if (Array.isArray(response.obj)) {{\n"
            f"  return response.obj.map((item: Record<string, any>) => {{\n"
            f"    return new {nombre}Entity(\n"
            f"{',\n'.join([f"          item.obj.{field.nombre}" for field in self.model.fields])});\n"
            f"}});\n"
            f"  }}\n"
            f"  return new {nombre}Entity(\n"
            f"{',\n'.join([f"          response.obj.{field.nombre}" for field in self.model.fields])});\n"
            f"    }}catch(error){{\n"
            f"      throw Error(`Error actualizando {self.model.nombre}: ${{error}}`);\n"
            f"    }}\n"
            f"  }}\n"
        )
    
    def __delete(self,)->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"async delete(id:string):Promise<any> {{\n"
            f"try{{\n"
            f"  const response = await this.api.delete(`{nombre.lower()}/${{id}}`);\n"
            f"  if (response.status < 200 || response.status > 299 ){{throw Error(`Error eliminando {self.model.nombre}`)}}\n"
            f"  return response;\n"
            f"}}catch(error){{\n"
            f"  throw Error(`Error eliminando {self.model.nombre}: ${{error}}`);\n"
            f"}}\n"
            f"}}\n"
        )