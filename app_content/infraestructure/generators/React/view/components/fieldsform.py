from app_content.domain.entities.model_entity import ModelEntity

class ReactFieldForm:
    def __init__(self) -> None:
        pass

    def textfield(self, model:ModelEntity, basepath: str,)->str:
        return (
            f"{self.__textfieldprops()}\n"
            f"export const TextField = (\n"
            f"  {{label, name, value, placeholder, required, onChange}}: TextFieldProps) => (\n"
            f"<div className=\"mb-3\">\n"
            f"<label htmlFor={{name}} className=\"form-label fw-semibold\">\n"
            f"{{label}}\n"
            f"</label>\n"
            f"<input\n"
            f"type=\"text\"\n"
            f"className=\"form-control\"\n"
            f"id={{name}}\n"
            f"name={{name}}\n"
            f"value={{value}}\n"
            f"onChange={{onChange}}\n"
            f"placeholder={{placeholder}}\n"
            f"required={{required}}\n"
            f"/>\n"
            f"</div>\n"
            f");\n"
            # f"export default TextField;\n"

        )
    
    def __textfieldprops(self,)->str:
        return (
            f"type TextFieldProps = {{\n"
            f"  label: string;\n"
            f"  name: string;\n"
            f"  value: string;\n"
            f"  placeholder?: string;\n"
            f"  required?: boolean;\n"
            f"  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;\n"
            f"}}\n"
        )
    
    def numberfield(self, model: ModelEntity, basepath: str)->str:
        return (
            f"{self.__numberfieldprops()}\n"
            f"export const NumberField = (\n"
            f"  {{label, name, value, min, max, step, onChange}}: NumberFieldProps) => (\n"
            f"<div className=\"mb-3\">\n"
            f"<label htmlFor={{name}} className=\"form-label fw-semibold\">\n"
            f"{{label}}\n"
            f"</label>\n"
            f"<input\n"
            f"type=\"number\"\n"
            f"className=\"form-control\"\n"
            f"id={{name}}\n"
            f"name={{name}}\n"
            f"value={{value}}\n"
            f"min={{min}}\n"
            f"max={{max}}\n"
            f"step={{step}}\n"
            f"onChange={{onChange}}\n"
            f"/>\n"
            f"</div>\n"
            f");\n"
            # f"export default NumberField;\n"
        )

    def __numberfieldprops(self)->str:
        return (
            f"type NumberFieldProps = {{\n"
            f"  label: string;\n"
            f"  name: string;\n"
            f"  value: number;\n"
            f"  min?: number;\n"
            f"  max?: number;\n"
            f"  step?: number;\n"
            f"  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;\n"
            f"}};\n"
        )

    def emailfield(self, model: ModelEntity, basepath: str)->str:
        return (
            f"{self.__emailfieldprops()}\n"
            f"export const EmailField = ({{ value, onChange }}: EmailFieldProps) => (\n"
            f"<div className=\"mb-3\">\n"
            f"<label htmlFor=\"email\" className=\"form-label fw-semibold\">Correo electrónico</label>\n"
            f"<input\n"
            f"type=\"email\"\n"
            f"className=\"form-control\"\n"
            f"id=\"email\"\n"
            f"name=\"email\"\n"
            f"value={{value}}\n"
            f"onChange={{onChange}}\n"
            f"placeholder=\"usuario@correo.com\"\n"
            f"required\n"
            f"/>\n"
            f"</div>\n"
            f");\n"
            # f"export default EmailField;\n"
        )

    def __emailfieldprops(self)->str:
        return (
            f"type EmailFieldProps = {{\n"
            f"  value: string;\n"
            f"  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;\n"
            f"}};\n"
        )
    
    def passwordfield(self, model: ModelEntity, basepath: str)->str:
        return (
            f"{self.__passwordfieldprops()}\n"
            f"export const PasswordField = ({{ value, onChange }}: PasswordFieldProps) => (\n"
            f"<div className=\"mb-3\">\n"
            f"<label htmlFor=\"password\" className=\"form-label fw-semibold\">Contraseña</label>\n"
            f"<input\n"
            f"type=\"password\"\n"
            f"className=\"form-control\"\n"
            f"id=\"password\"\n"
            f"name=\"password\"\n"
            f"value={{value}}\n"
            f"onChange={{onChange}}\n"
            f"placeholder=\"••••••••\"\n"
            f"required\n"
            f"/>\n"
            f"</div>\n"
            f");\n"
            # f"export default PasswordField;\n"
        )

    def __passwordfieldprops(self)->str:
        return (
            f"type PasswordFieldProps = {{\n"
            f"  value: string;\n"
            f"  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;\n"
            f"}};\n"
        )
    
    def selectedfield(self, model: ModelEntity, basepath: str)->str:
        return (
            f"{self.__selectedfieldprops()}\n"
            f"export const SelectedField = ({{label, name, value, options, required, onChange}}: SelectedFieldProps) => (\n"
            f"<div className=\"mb-3\">\n"
            f"<label htmlFor={{name}} className=\"form-label fw-semibold\">\n"
            f"{{label}}\n"
            f"</label>\n"
            f"<select\n"
            f"className=\"form-select\"\n"
            f"id={{name}}\n"
            f"name={{name}}\n"
            f"value={{value}}\n"
            f"onChange={{onChange}}\n"
            f"required={{required}}\n"
            f">\n"

            f"<option value=\"\">Seleccione una opción</option>\n"
            f"{{options.map((option) => (\n"
            f"  <option key={{option.value}} value={{option.value}}>\n"
            f"    {{option.label}}\n"
            f"  </option>\n"
            f"))}}\n"

            f"</select>\n"
            f"</div>\n"
            f");\n"
            # f"export default SelectedField;\n"
        )

    def __selectedfieldprops(self)->str:
        return (
            f"type SelectedFieldProps = {{\n"
            f"label: string;\n"
            f"name: string;\n"
            f"value: string;\n"
            f"options:{{label:string, value:string}}[];\n"
            f"required?: boolean;\n"
            f"onChange: (e: React.ChangeEvent<HTMLSelectElement>) => void;\n"
            f"}};\n"
        )
    
    def textareafield(self, model: ModelEntity, basepath:str)->str:
        return (
            f"{self.__textareafieldprops()}\n"
            f"export const TextareaField = ({{label, name, value, rows, placeholder, required, onChange}}: TextareaFieldProps) => (\n"
            f"<div className=\"mb-3\">\n"
            f"<label htmlFor={{name}} className=\"form-label fw-semibold\">\n"
            f"{{label}}\n"
            f"</label>\n"
            f"<textarea\n"
            f"className=\"form-control\"\n"
            f"id={{name}}\n"
            f"name={{name}}\n"
            f"value={{value}}\n"
            f"rows={{rows}}\n"
            f"placeholder=\"{{placeholder}}\"\n"
            f"required={{required}}\n"
            f"onChange={{onChange}}\n"
            f"/>\n"
            f"</div>\n"
        )
    
    def __textareafieldprops(self)->str:
        return (
            f"type TextareaFieldProps = {{\n"
            f"  label: string;\n"
            f"  name: string;\n"
            f"  value: string;\n"
            f"  rows?: number;\n"
            f"  placeholder?: string;\n"
            f"  required?: boolean;\n"
            f"  onChange: (e: React.ChangeEvent<HTMLTextAreaElement>) => void;\n"
            f"}}\n"
        )
    
    def checkboxfield(self, model: ModelEntity, basepath: str)->str:
        return (
            f"{self.__checkboxfieldprops()}\n"
            f"export const CheckboxField = ({{label, name, checked, onChange}}: CheckboxFieldProps) => (\n"
            f"<div className=\"form-check mb-3\">\n"
            f"<input\n"
            f"type=\"checkbox\"\n"
            f"className=\"form-check-input\"\n"
            f"id={{name}}\n"
            f"name={{name}}\n"
            f"checked={{checked}}\n"
            f"onChange={{onChange}}\n"
            f"/>\n"
            f"<label className=\"form-check-label fw-semibold\" htmlFor={{name}}>\n"
            f"{{label}}\n"
            f"</label>\n"
            f"</div>\n"
            f")\n"
    )

    def __checkboxfieldprops(self)->str:
        return (
            f"type CheckboxFieldProps = {{\n"
            f"  label: string;\n"
            f"  name: string;\n"
            f"  checked: boolean;\n"
            f"  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;\n"
            f"}}\n"
        )

    def datefield(self, model: ModelEntity, basepath: str)->str:
        return (
            f"{self.__datefieldprops()}\n"
            f"export const DateField = ({{label, name, value, min, max, required, onChange}}: DateFieldProps) => (\n"
            f"<div className=\"mb-3\">\n"
            f"<label htmlFor={{name}} className=\"form-label fw-semibold\">\n"
            f"{{label}}\n"
            f"</label>\n"
            f"<input\n"
            f"type=\"date\"\n"
            f"className=\"form-control\"\n"
            f"id={{name}}\n"
            f"name={{name}}\n"
            f"value={{value}}\n"
            f"min={{min}}\n"
            f"max={{max}}\n"
            f"required={{required}}\n"
            f"onChange={{onChange}}\n"
            f"/>\n"
            f"</div>\n"
            f")\n"
        )

    def __datefieldprops(self)->str:
        return (
            f"type DateFieldProps = {{\n"
            f"  label: string;\n"
            f"  name: string;\n"
            f"  value: string;\n"
            f"  min?: string;\n"
            f"  max?: string;\n"
            f"  required?: boolean;\n"
            f"  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;\n"
            f"}}\n"
        )

    def filefield(self, model: ModelEntity, basepath: str)->str:
        return (
            f"{self.__filefieldprops()}\n"
            f"export const FileField = ({{label, name, accept, required, onChange}}: FileFieldProps) => (\n"
            f"<div className=\"mb-3\">\n"
            f"<label htmlFor={{name}} className=\"form-label fw-semibold\">\n"
            f"{{label}}\n"
            f"</label>\n"
            f"<input\n"
            f"type=\"file\"\n"
            f"className=\"form-control\"\n"
            f"id={{name}}\n"
            f"name={{name}}\n"
            f"accept={{accept}}\n"
            f"required={{required}}\n"
            f"onChange={{onChange}}\n"
            f"/>\n"
            f"</div>\n"
            f")\n"
        )

    def __filefieldprops(self)->str:
        return (
            f"type FileFieldProps = {{\n"
            f"  label: string;\n"
            f"  name: string;\n"
            f"  accept?: string;\n"
            f"  required?: boolean;\n"
            f"  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;\n"
            f"}}\n"
        )

    def radiogroupfield(self, model: ModelEntity, basepath: str)->str:
        return (
            f"{self.__radiogroupfieldprops()}\n"
            f"export const RadioGroupField = ({{label, name, value, options, onChange}}: RadioGroupFieldProps) => (\n"
            f"<div className=\"mb-3\">\n"
            f"<label className=\"form-label fw-semibold d-block\">\n"
            f"{{label}}\n"
            f"</label>\n"
            f"{{options.map((opt) => (\n"
            f"<div className=\"form-check\" key={{opt.value}}>\n"
            f"<input\n"
            f"className=\"form-check-input\"\n"
            f"type=\"radio\"\n"
            f"id={{`${{name}}-${{opt.value}}`}}\n"
            f"name={{name}}\n"
            f"value={{opt.value}}\n"
            f"checked={{value === opt.value}}\n"
            f"onChange={{onChange}}\n"
            f"/>\n"
            f"<label className=\"form-check-label\" htmlFor={{`${{name}}-${{opt.value}}`}}>\n"
            f"{{opt.label}}\n"
            f"</label>\n"
            f"</div>\n"
            f"))}}\n"
            f"</div>\n"
            f")\n"
        )

    def __radiogroupfieldprops(self)->str:
        return (
            f"type RadioOption = {{\n"
            f"  label: string;\n"
            f"  value: string;\n"
            f"}};\n"
            f"\n"
            f"type RadioGroupFieldProps = {{\n"
            f"  label: string;\n"
            f"  name: string;\n"
            f"  value: string;\n"
            f"  options: RadioOption[];\n"
            f"  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;\n"
            f"}}\n"
        )
