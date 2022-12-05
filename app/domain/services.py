from typing import List
from datetime import time

from utils.dataclass_classmethods import FromDictMixin
import dataclasses

@dataclasses.dataclass
class Service(FromDictMixin):
    id : int = 0
    barber_id_id : int = 0
    name : str = None
    cost : float = 0.0
    span : time = None

@dataclasses.dataclass
class ServicesList(FromDictMixin):
    data : List[Service] = dataclasses.field(default_factory=dict)