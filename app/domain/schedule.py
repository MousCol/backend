from datetime import time

from typing import List

from utils.dataclass_classmethods import FromDictMixin
import dataclasses

@dataclasses.dataclass
class Schedule(FromDictMixin):
    id : int = 0
    barbery_id : int = 0
    day : str = None
    start : time = None
    end : time = None

@dataclasses.dataclass
class ScheduleList(FromDictMixin):
    data : List[Schedule] = dataclasses.field(default_factory=dict)