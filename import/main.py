import sys
print(sys.path, end='\n\n')

sys.path.append('/Users/shaun/dev_python/import')
print(sys.path, end='\n\n')

import superman
print(superman.name)
