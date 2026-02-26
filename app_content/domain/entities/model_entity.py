from dataclasses import dataclass
from typing import Optional
from app_content.domain.entities.data_entity import FieldEntity

@dataclass(kw_only=True)
class ModelEntity():
    '''
    Model Entity
    Es una entidad de un model de Django.
    nombre : str -> Nombre de la entidad, ejm: User
    fields : list[FieldEntity] -> Campos de la entidad, ejm: id, name, etc
    abstract : bool -> Indica si la entidad es abstracta, ejm: True
    '''
    nombre : str
    fields : list[FieldEntity]
    abstract : Optional[bool] = None

    def __str__(self):
        return self.nombre