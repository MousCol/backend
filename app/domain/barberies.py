from typing import List

from utils.dataclass_classmethods import FromDictMixin
import dataclasses

@dataclasses.dataclass
class Barbery(FromDictMixin):
    id : int = 0
    title : str = None
    location : str = None
    stars : str = None
    url : str = None
    longitude : float = 0.0
    latitude : float = 0.0
    city : str = None

@dataclasses.dataclass
class BarberiesList(FromDictMixin):
    data : List[Barbery] = dataclasses.field(default_factory=dict)