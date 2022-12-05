from datetime import datetime

from typing import List

from utils.dataclass_classmethods import FromDictMixin
import dataclasses

@dataclasses.dataclass
class Booking(FromDictMixin):
    id : int = 0
    barber_id : int = 0
    user_id : int = 0
    start : datetime = None
    end : datetime = None

@dataclasses.dataclass
class BookingsList(FromDictMixin):
    data : List[Booking] = dataclasses.field(default_factory=dict)