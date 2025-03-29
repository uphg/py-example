__version__ = '1.0.0'
__author__ = 'Jack'

from .moduleB import y
from . import moduleB

__all__ = ['moduleB', 'y']
print('packageA/__init__.py: Hello, World!')
