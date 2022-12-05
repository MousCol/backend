from utils.dataclass_classmethods import FromDictMixin
import dataclasses

@dataclasses.dataclass
class User(FromDictMixin):
    id : int = 0
    first_name : str = None
    last_name : str = None
    email : str = None
    password : str = None
    phone : str = None
    status : str = None