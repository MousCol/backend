from typing import List

from utils.dataclass_classmethods import FromDictMixin
import dataclasses

from .services import Service

@dataclasses.dataclass
class Barber(FromDictMixin):
    id : int = 0
    barbery_id : int = 0
    first_name : str = None
    last_name : str = None
    stars : str = None
    url : str = None
    city : str = None
    services : List[Service] = dataclasses.field(default_factory=dict)

@dataclasses.dataclass
class BarbersList(FromDictMixin):
    data : List[Barber] = dataclasses.field(default_factory=dict)