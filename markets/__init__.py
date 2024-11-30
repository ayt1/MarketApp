import inspect
from .a101 import A101
from .bim import BIM
from .happy_center import HappyCenter
from .sok import Sok
from .watsons import Watsons
from .onur import Onur

# Automatically collect all classes from this module
__all__ = [name for name, obj in globals().items() if inspect.isclass(obj)]