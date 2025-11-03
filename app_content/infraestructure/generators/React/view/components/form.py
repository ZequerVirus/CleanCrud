from app_content.domain.entities.model_entity import ModelEntity
import os

class ReactForm:
    def __init__(self) -> None:
        pass

    def execute(self, model: ModelEntity, basepath: str,):
        ''' Generate the files for the model '''
        nombre = f"{model.nombre[0].capitalize()}{model.nombre[1:]}"
        path = os.path.join(basepath, "presentation", "views", f"{nombre}")
        os.makedirs(path, exist_ok=True)
        filepath = os.path.join(path, f"{model.nombre}_form.tsx")
        try:
            with open(filepath, "w") as f:
                f.write(f"{self.__imports(model=model, nombre=nombre, basepath=basepath)}\n")
                f.write(f"{self.__interface(model=model, nombre=nombre, basepath=basepath)}\n")
                f.write(f"{self.__form(model=model, nombre=nombre, basepath=basepath)}\n")
                f.write(f"export default {nombre}Form;\n")
        except Exception as e:
            raise Exception(e)
        
    def __imports(self, model: ModelEntity, nombre: str, basepath:str)->str:
        ''' Generate the imports for the file '''
        return (
            f"import {{useState, useEffect}} from 'react';\n"
            f"import type {{ {nombre}Entity }} from '../../../domain/entities/{model.nombre}_entity';\n"
        )
    
    def __interface(self, model: ModelEntity, nombre: str, basepath:str)->str:
        ''' Generate the interface for the file'''
        return (
            f"type {nombre}FormProps = {{\n"
            f"  initial{nombre}?: {nombre}Entity;\n"
            f"  onSubmit: (value: any|{nombre}Entity) => void;\n"
            f"  onCancel: () => void;\n"
            f"}}\n"
        )
    
    def __form(self, model: ModelEntity, nombre: str, basepath:str)->str:
        ''' Generate the form for the file'''
        return (
            f"function {nombre}Form({{initial{nombre}, onSubmit, onCancel}}: {nombre}FormProps) {{\n"
            f"    const [value, setValue] = useState<{nombre}Entity>(\n"
            f"        initial{nombre} ||\n"
            f"        {{\n"
            f"{(',\n').join([f'        {field.nombre}: {f"{self.__empty(field.tipo)}" if field.nombre != "id" else "null"}' for field in model.fields])}\n"
            f"        }}\n"
            f"    );\n"
            f"\n"
            f"useEffect(() => {{\n"
            f"  if (initial{nombre}) {{\n"
            f"    setValue(initial{nombre});\n"
            f"  }}\n"
            f"}}, [initial{nombre}]);\n"
            f"\n"
            f"const handleChange = (e: React.ChangeEvent<HTMLFieldElement | HTMLSelectElement>) => {{\n"
            f"  const {{name, value}} = e.target;\n"
            f"  setValue({{...value, [name]: value}});\n"
            f"}}\n"
            f"\n"
            f"const handleSubmit = (e: React.FormEvent) => {{\n"
            f"  e.preventDefault();\n"
            f"  if ({(' || \n').join([f'!value.{field.nombre
                                    if field.tipo != 'string' else f"{field.nombre}.trim()"}' 
                                    for field in model.fields 
                                    if field.nombre != 'id' and not field.tipo.__contains__('null')])}){{\n"
            f"    alert(\"Todos los campos son obligatorios\");\n"
            f"    return;\n"
            f"  }}\n"
            f"onSubmit(value);\n"
            f"}};\n"
            f"\n"
            f"return (\n"
            f"{self.__formbody(model=model, nombre=nombre, basepath=basepath)}\n"
            f");\n"
            f"}}\n"
        )
    
    def __formbuttons(self, model: ModelEntity, basepath:str)->str:
        return (
            f"<div className=\"d-flex justify-content-end gap-2\">\n"
            f"{{onCancel && (<button type=\"button\" className=\"btn btn-outline-secondary\" onClick={{\"onCancel\"}}>Cancelar</button>)}}\n"
            f"<button type=\"submit\" className=\"btn btn-primary\" onClick={{()=>handleSubmit(value)}}>{{initial{model.nombre}? \"Editar {model.nombre}\": \"Crear {model.nombre}\"}}</button>\n"
            f"</div>\n"
        )
    
    def __formbody(self, model: ModelEntity, nombre: str, basepath:str)->str:
        return (
            f"<form className=\"p-4 border rounded shadow-sm bg-light\" onSubmit={{\"handleSubmit\"}}>\n"
            f"<h5 className=\"mb-3\">{{initial{model.nombre}? \"Editar {model.nombre}\": \"Crear {model.nombre}\"}}</h5>\n"
            f"{('\n').join([f'{self.__field(model=model, basepath=basepath, name=field.nombre, typefield=field.tipo)}' 
                            for field in model.fields if field.nombre != 'id'])}\n"
            f"{self.__formbuttons(model=model, basepath=basepath)}\n"
            f"</form>\n"
        )
    
    def __empty(self, field: str)->str:
        match field:
            case "string":
                return "''"
            case "number":
                return "0"
            case "boolean":
                return "false"
            case "Date":
                return "new Date()"
            case "array":
                return "[]"
            case "object":
                return "{}"
            case _:
                return "null"
            
    def __field(self, model: ModelEntity, basepath: str, name:str, typefield:str)->str:
        match typefield:
            case "string":
                match name:
                    case "phone" | "telefono":
                        return f"<PhoneField onChange={{handleChange}} value={{value.{name if not typefield.__contains__('null') else f'{name}??{self.__empty(typefield)}'}}} name=\"{name}\" label=\"{name}\" placeholder=\"{name}\" {'required={{true}}' if not typefield.__contains__('null') else ''} />"
            
                    case "email":
                        return f"<EmailField onChange={{handleChange}} value={{value.{name if not typefield.__contains__('null') else f'{name}??{self.__empty(typefield)}'}}}/>"
            
                    case "password":
                        return f"<PasswordField onChange={{handleChange}} value={{value.{name if not typefield.__contains__('null') else f'{name}??{self.__empty(typefield)}'}}}/>"
            
                    case _:
                        if name.lower().__contains__('date') or name.__contains__('fecha'):
                            return f"<DateField name={{{name}}} onChange={{handleChange}} value={{value.{name if not typefield.__contains__('null') else f'{name}??{self.__empty(typefield)}'}}} label=\"{name}\" placeholder=\"{name}\" {'required={{true}}' if not typefield.__contains__('null') else ''}/>"
                        return f"<TextField onChange={{handleChange}} value={{value.{name if not typefield.__contains__('null') else f'{name}??{self.__empty(typefield)}'}}} label=\"{name}\" placeholder=\"{name}\" {'required={{true}}' if not typefield.__contains__('null') else ''}/>"
            
            case "number":
                return f"<NumberField name={{{name}}} onChange={{handleChange}} value={{value.{name if not typefield.__contains__('null') else f'{name}??{self.__empty(typefield)}'}}} label=\"{name}\" placeholder=\"{name}\" {'required={{true}}' if not typefield.__contains__('null') else ''}/>"
            
            case "boolean":
                return f"<SelectedField name={{{name}}} onChange={{handleChange}} value={{value.{name if not typefield.__contains__('null') else f'{name}??{self.__empty(typefield)}'}}} label=\"{name}\" placeholder=\"{name}\" options=[{{label: 'Si', value: true}}, {{label: 'No', value: false}}] {'required={{true}}' if not typefield.__contains__('null') else ''}/>"
            
            case "Date":
                return f"<DateField name={{{name}}} onChange={{handleChange}} value={{value.{name if not typefield.__contains__('null') else f'{name}??{self.__empty(typefield)}'}}} label=\"{name}\" placeholder=\"{name}\" {'required={{true}}' if not typefield.__contains__('null') else ''}/>"
            
            case "array":
                return f"<SelectedField name={{{name}}} onChange={{handleChange}} value={{value.{name if not typefield.__contains__('null') else f'{name}??{self.__empty(typefield)}'}}} label=\"{name}\" placeholder=\"{name}\" options=[] {'required={{true}}' if not typefield.__contains__('null') else ''}/>"
            
            case "object":
                return f"<SelectedField name={{{name}}} onChange={{handleChange}} value={{value.{name if not typefield.__contains__('null') else f'{name}??{self.__empty(typefield)}'}}} label=\"{name}\" placeholder=\"{name}\" options=[] {'required={{true}}' if not typefield.__contains__('null') else ''}/>"
            
            case _:
                return f"<TextField name={{{name}}} onChange={{handleChange}} value={{value.{name if not typefield.__contains__('null') else f'{name}??{self.__empty(typefield)}'}}} label=\"{name}\" placeholder=\"{name}\" {'required={{true}}' if not typefield.__contains__('null') else ''}/>"
            