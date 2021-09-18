

from mymodule import sayhi, __version__

# Вы могли бы также использовать:
# from mymodule import *
# Это импортирует все публичные имена, такие как sayhi,
# но не импортирует __version__,
# потому что оно начинается с двойного подчёркивания


sayhi()
print('Версия', __version__)
