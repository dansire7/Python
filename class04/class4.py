from typing import Any

names : list[str] = ['shahrukh', 'salman', 'amir','saif', 6, 2.5] 
# here number and integers were added by type is generating error.

names1: list [Any] = ['shahrukh', 'salman', 'amir','saif', 6, 2.5]
# here number and integers were added but not generating error as type Any has been used.