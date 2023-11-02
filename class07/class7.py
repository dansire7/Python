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
                        # (1,2) : 'Pakistan' hashable error tupples
                        # [1,3,3] : 'Pakistan', # hashable error list
                        # {2,3}: 'Pakistan' # hshable error set
                        }
# dictionary of data will show data like an object.

pprint.pprint(data)
print(data['name']) # python will return value against key 'name'
print(data[0]) # python will return value as Pakistan against key '0', 0 is the key not the index no.
