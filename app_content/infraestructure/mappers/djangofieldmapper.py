from app_content.application.interface.fieldmapper import FieldMapper
from pathlib import Path
import re
from app_content.domain.entities.data_entity import FieldEntity

class DjangoFieldMapper(FieldMapper):

    def execute(self, model_name:str, model_path:str,)-> list[FieldEntity]:
        FIELD_TYPE_MAP = {
            # 🔸 Básicos
            "AutoField": "int",
            "BigAutoField": "int",
            "SmallAutoField": "int",
            "CharField": "str",
            "TextField": "str",
            "SlugField": "str",
            "IntegerField": "int",
            "SmallIntegerField": "int",
            "PositiveIntegerField": "int",
            "PositiveSmallIntegerField": "int",
            "BigIntegerField": "int",
            "FloatField": "float",
            "DecimalField": "float",
            "BooleanField": "bool",
            "NullBooleanField": "bool",
            "DateTimeField": "datetime",
            "DateField": "date",
            "TimeField": "time",
            "DurationField": "timedelta",
            "BinaryField": "bytes",
            "UUIDField": "uuid",

            # 🔸 Archivos y URLs
            "FileField": "str",
            "ImageField": "str",
            "FilePathField": "str",
            "URLField": "str",
            "EmailField": "str",
            "GenericIPAddressField": "str",
            "IPAddressField": "str",

            # 🔸 JSON y otros
            "JSONField": "dict",
            "ArrayField": "list",       # PostgreSQL Array
            "HStoreField": "dict",      # PostgreSQL key-value
            "CICharField": "str",       # PostgreSQL case-insensitive
            "CIEmailField": "str",
            "CITextField": "str",
            "JSONBField": "dict",       # PostgreSQL JSONB

            # 🔸 GeoDjango (si usas GIS)
            "PointField": "dict",       # podría ser coordenadas
            "PolygonField": "dict",
            "LineStringField": "dict",
            "GeometryField": "dict",
            "RasterField": "dict",

            # 🔸 Relaciones
            "ForeignKey": "int",        # generalmente el ID
            "OneToOneField": "int",
            "ManyToManyField": "list",
            "ManyToOneRel": "list",     # relaciones inversas
            "ManyToManyRel": "list",

            # 🔸 Otros especiales
            "PositiveBigIntegerField": "int",
            "CharTextField": "str",     # custom user fields
        }

        
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
                name, django_type, args = field_match.groups()
                py_type = FIELD_TYPE_MAP.get(django_type, "unknown")
                is_optional = "null=True" in args or "blank=True" in args
                if is_optional:
                    py_type = f"{py_type} | None"
                fields.append(FieldEntity(nombre=name, tipo=py_type))

        return fields
