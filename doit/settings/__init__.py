# Standard Library
import getpass

# Local Django
from doit.settings.base import *


if getpass.getuser() in ['root']:
    from doit.settings.production import *
else:
    from doit.settings.staging import *
