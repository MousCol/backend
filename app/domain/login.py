from utils.dataclass_classmethods import FromDictMixin
import dataclasses

@dataclasses.dataclass
class Login(FromDictMixin):
    email : str = None
    password : str = None