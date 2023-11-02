from typing import Dict,  Union, Optional
import pprint 

# Created type

Key = Union[str, int]
Value = Union [str, int, float, list, dict, tuple, set] # you should not use any or else system will generate error if any un-hashable data type has been used.

# Dict is based on key and its value

#          key, value  Dictionary identifier is values will be in curly brackets
data: Dict[Key, Value] = {'fname':'Abdul Hameed',
                        'name':"Danish Ghani",
                        'education':"MSCS",
                         0 : 'Pakistan',
                         'abc': (1,2),#  tuples can be added in value
                         'xyc': [1,3,3], # list can be added in value
                          'axy': {2,3}, # set can be added in value
                         'abcd': {'a': '2', 'b' : '8'} # dict can be added in value
                        }
# dictionary of data will show data like an object.

methods : list[str]=[m for m in dir(data) if "__" not in m]
print(methods)