from app_content.application.interface.fieldmapper import FieldType

class DjangoFieldType(FieldType):
    PYTHON_FIELDS = {
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
            "HStoreField": "dict",      # PostgreSQL key-python_type
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
    def __init__(self):
        self.types = {}

    def topythonfield(self):
        self.types = self.PYTHON_FIELDS.copy()

    def toreactfield(self,):
        react_types = {
            "str": "string",
            "int": "number",
            "float": "number",
            "bool": "boolean",
            "datetime": "string",
            "date": "string",
            "time": "string",
            "timedelta": "string",
            "bytes": "string",
            "uuid": "string",
            "dict": "object",
            "list": "array",
        }

        self.types = {
            django_type: react_types.get(python_type, "any")
            for django_type, python_type in self.PYTHON_FIELDS.items()
        }

    def toflutterfield(self, ):
        flutter_types = {
            "str": "String",
            "int": "int",
            "float": "double",
            "bool": "bool",
            "datetime": "DateTime",
            "date": "DateTime",
            "time": "DateTime",
            "timedelta": "DateTime",
            "bytes": "String",
            "uuid": "String",
            "dict": "Map<String, dynamic>",
            "list": "List<dynamic>",
        }

        self.types = {
            django_type: flutter_types.get(python_type, "dynamic")
            for django_type, python_type in self.PYTHON_FIELDS.items()
        }



