# zmienne globalne, definicje funkcji w podmodułach
# domyślne exporty
# import innych modulów

#import my_module.sub_module1, my_module.sub_module2
from . import sub_module2, sub_module1

print(f'Hello from {__name__}')