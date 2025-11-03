from app_content.application.interface.fieldmapper import FieldMapper
from pathlib import Path
import re
from app_content.domain.entities.data_entity import FieldEntity
from app_content.infraestructure.mappers.Django.fieldstype import DjangoFieldType

class DjangoFieldMapper(FieldMapper):

    def execute(self, model_name:str, model_path:str, language_to_map:str)-> list[FieldEntity]:
        FIELD_TYPE_MAP = self.field_type(language_to_map)
        
        path = Path(model_path)
        if not path.exists():
            raise FileNotFoundError(f"Model file {model_path} does not exist")
        
        content = path.read_text(encoding='utf-8')

        class_pattern = rf"class\s+{re.escape(model_name)}\s*\(.*\)\s*:"
        class_match = re.search(class_pattern, content)
        if not class_match:
            return []

        # 2️⃣ Tomar el bloque de código de la clase (basado en indentación)
        lines = content.splitlines()
        class_start = None
        class_indent = 0
        for i, line in enumerate(lines):
            if re.match(class_pattern, line):
                class_start = i
                class_indent = len(line) - len(line.lstrip())
                break

        if class_start is None:
            return []

        fields = []
        # Recorrer líneas siguientes con mayor indentación que la clase
        for line in lines[class_start + 1:]:
            stripped = line.lstrip()
            indent = len(line) - len(stripped)
            if indent <= class_indent or not stripped:
                break  # fin de la clase

            # Buscar asignaciones a campos de Django: nombre = models.Tipo(...)
            field_match = re.match(r"(\w+)\s*=\s*models\.(\w+)\((.*)\)", stripped)
            if field_match:
                fields.append(self.get_field(field_match=field_match, FIELD_TYPE_MAP=FIELD_TYPE_MAP, language_to_map=language_to_map))

        return fields
    
    def get_field(self, field_match, FIELD_TYPE_MAP, language_to_map):
        name, django_type, args = field_match.groups()
        match language_to_map:
            case 'python':
                py_type = FIELD_TYPE_MAP.get(django_type, "unknown")
                is_optional = "null=True" in args or "blank=True" in args
                if is_optional:
                    py_type = f"{py_type} | None"
            case 'flutter':
                py_type = FIELD_TYPE_MAP.get(django_type, "dynamic")
                is_optional = "null=True" in args or "blank=True" in args
                if is_optional:
                    py_type = f"{py_type}?"
            case 'react':
                py_type = FIELD_TYPE_MAP.get(django_type, "any")
                is_optional = "null=True" in args or "blank=True" in args
                if is_optional:
                    # py_type = f"{py_type} | undefined"
                    py_type = f"{py_type} | null"
            case _:
                raise Exception("Language not supported")
        return FieldEntity(nombre=name, tipo=py_type)
    
    def field_type(self, language_to_map):
        dft = DjangoFieldType()
        match language_to_map:
            case 'python':
                dft.topythonfield()
            case 'flutter':
                dft.toflutterfield()
            case 'react':
                dft.toreactfield()
            case _:
                raise Exception("Language not supported")
        return dft.types
