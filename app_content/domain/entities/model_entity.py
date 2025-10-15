from dataclasses import dataclass
from typing import Optional
from app_content.domain.entities.data_entity import FieldEntity

@dataclass(kw_only=True)
class ModelEntity():
    nombre : str
    fields : list[FieldEntity]
    abstract : Optional[bool] = None

    def __str__(self):
        return self.nombre