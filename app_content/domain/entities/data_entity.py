from dataclasses import dataclass

@dataclass(kw_only=True)
class FieldEntity:
    '''
    Entidad del campo
    nombre : str -> Nombre del campo, ejm: id
    tipo : str -> Tipo del campo, ejm: int
    '''
    nombre: str
    tipo: str
    