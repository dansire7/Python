# =============Union type==================
from typing import Union, Optional

percentage : Union[int, float] = 7.0

print(percentage)

# You can also use union like mentioned below
grade : str | None | int= 27

#===================Optional type=============

grade1 :Optional [str] = None
grade1  = "string"
grade1 = 2 # this will generate error

# ===================Type Alias===================

from typing import Union

alphanum = Union [str, int] 

user_id : alphanum = 23.7 # Error Generated

print(user_id)
