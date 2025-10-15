from dataclasses import dataclass
from typing import Optional

@dataclass
class ModelDTOInput:
    name: str
    fields: list
    abstract: bool

@dataclass
class ModelDTOOutput:
    model: Optional[dict]
    message: Optional[str]
    success: bool

    

