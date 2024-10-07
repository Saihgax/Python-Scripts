""" 
Input: 2 cats and 3 dogs

"""

import re
s = "2 cats and 3 dogs"
print(re.findall("\d+", s))
