import os
from app_content.application.interface.generator import Generator

class ReactHook(Generator):
    def __init__(self):
        pass

    def execute(self,):
        ''' Generate the hook for the file'''
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        path = os.path.join(self.basepath, "presentation", "views", f"{nombre}")
        os.makedirs(path, exist_ok=True)
        filepath = os.path.join(path, f"{self.model.nombre}_hook.ts")
        try:
            with open(filepath, "w") as f:
                f.write(f"{self.__imports()}\n")
                f.write(f"{self.__hookprops()}\n")
                f.write(f"{self.__hook()}\n")

        except Exception as e:
            raise Exception(e)
        
    def __imports(self, )->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"import {{ useState, useEffect }} from 'react';\n"
            f"import {{ {nombre}UseCase }} from '../../../application/usecases/{self.model.nombre}_uc';\n"
            f"import {{ {nombre}Entity }} from '../../../domain/entities/{self.model.nombre}_entity';\n"
            f"import {{ APIGateway }} from '../../../infraestructure/services/APIGateway';\n"
        )
    
    def __hookprops(self, )->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"type {nombre}HookProps = {{\n"
            f"  items: {nombre}Entity[],\n"
            f"  loading: boolean,\n"
            f"  message: string,\n"
            f"  filtered: {nombre}Entity[],\n"
            f"}};\n"
        )
    
    def __hook(self, )->str:
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"export const {nombre}Hook = () => {{\n"
            f"  const [state, setState] = useState<{nombre}HookProps>({{\n"
            f"    items: [],\n"
            f"    loading: false,\n"
            f"    message: '',\n"
            f"    filtered: [],\n"
            f"  }});\n"
            f"  const uc = new {nombre}UseCase(new APIGateway());\n"
            f"{self.__load()}\n"
            f"{self.__create()}\n"
            f"{self.__update()}\n"
            f"{self.__delete()}\n"
            f"{self.__search()}\n"
            
            f"  useEffect(() => {{\n"
            f"    loadItems();\n"
            f"  }}, []);\n"

            f"  return {{ ...state, handleCreate, handleUpdate, handleDelete, handleSearch, }};\n"
            f"}};\n"
        )
    
    def __load(self, ):
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"  const loadItems = async () => {{\n"
            f"    setState(prev => ({{ ...prev, loading: true, message: '' }}));\n"
            f"    try {{\n"
            f"      const response = await uc.get();\n"
            f"      if (!response){{\n"
            f"        throw Error(`Error obteniendo {self.model.nombre}`);\n"
            f"      }}\n"
            f"        const objs = response;\n"
            f"        setState(prev => ({{ ...prev, items: objs, filtered: objs,}}));\n"
            f"    }} catch (error) {{\n"
            f"      setState(prev => ({{ ...prev, message: `Error obteniendo {self.model.nombre}: ${{error}}` }}));\n"
            f"    }} finally {{\n"
            f"      setState(prev => ({{ ...prev, loading: false }}));\n"
            f"    }}\n"
            f"  }};\n"
        )
    
    def __create(self, ):
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"  const handleCreate = async (data: any) => {{\n"
            f"    setState(prev => ({{ ...prev, loading: true, message: '' }}));\n"
            f"    try {{\n"
            f"      const response = await uc.create(data);\n"
            f"      if (!response){{\n"
            f"        throw Error(`Error creando {self.model.nombre}`);\n"
            f"      }}\n"
            f"      setState(prev => ({{ ...prev, message: \"{nombre} creado\"}}));\n"
            f"      await loadItems();\n"
            f"    }} catch (error) {{\n"
            f"      throw Error(`Error creando {self.model.nombre}: ${{error}}`);\n"
            f"    }} finally {{\n"
            f"      setState(prev => ({{ ...prev, loading: false }}));\n"
            f"    }}\n"
            f"  }};\n"
        )
    
    def __update(self, ):
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"  const handleUpdate = async (id: string, data: any) => {{\n"
            f"    setState(prev => ({{ ...prev, loading: true, message: '' }}));\n"
            f"    try {{\n"
            f"      const response = await uc.update(id, data);\n"
            f"      if (!response){{\n"
            f"        throw Error(`Error actualizando {self.model.nombre}`);\n"
            f"      }}\n"
            f"      setState(prev => ({{ ...prev, message: \"{nombre} actualizado\",}}));\n"
            f"      await loadItems();\n"
            f"    }} catch (error) {{\n"
            f"      throw Error(`Error actualizando {self.model.nombre}: ${{error}}`);\n"
            f"    }} finally {{\n"
            f"      setState(prev => ({{ ...prev, loading: false }}));\n"
            f"    }}\n"
            f"  }};\n"
        )
    
    def __delete(self, ):
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"  const handleDelete = async (id: string) => {{\n"
            f"    setState(prev => ({{ ...prev, loading: true, message: '' }}));\n"
            f"    try {{\n"
            f"      const response = await uc.delete(id);\n"
            f"      if (!response){{\n"
            f"        throw Error(`Error eliminando {self.model.nombre}`);\n"
            f"      }}\n"
            f"      setState(prev => ({{ ...prev, message: \"{nombre} eliminado\",}}));\n"
            f"      await loadItems();\n"
            f"    }} catch (error) {{\n"
            f"      throw Error(`Error eliminando {self.model.nombre}: ${{error}}`);\n"
            f"    }} finally {{\n"
            f"      setState(prev => ({{ ...prev, loading: false }}));\n"
            f"    }}\n"
            f"  }};\n"
        )
    
    def __search(self, ):
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"  const handleSearch = (value: string) => {{\n"
            f"    if (!value){{\n"
            f"      setState(prev => ({{ ...prev, filtered: state.items }}));\n"
            f"      return;\n"
            f"    }}\n"
            f"    const lower=value.toLowerCase();\n"
            f"    const filtered = state.items.filter((item: {nombre}Entity) => {{\n"
            f"      return {(' ||\n').join([f'item.{field.nombre if field.tipo.__contains__('null') else f'{field.nombre}?'}.toString().toLowerCase().includes(lower)' for field in self.model.fields])};\n"
            f"    }});\n"
            f"    setState(prev => ({{ ...prev, filtered: filtered }}));\n"
            f"  }};\n"
        )