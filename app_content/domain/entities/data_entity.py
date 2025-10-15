from dataclasses import dataclass

@dataclass(kw_only=True)
class FieldEntity:
    nombre: str
    tipo: str
    