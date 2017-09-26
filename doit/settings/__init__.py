# Standard Library
import getpass

# Local Django
from doit.settings.base import *


if getpass.getuser() in ['root', 'apps']:
    from doit.settings.prod import *
elif getpass.getuser() in ['vagrant', 'ubuntu', 'doit']:
    from doit.settings.staging import *
else:
    from doit.settings.dev import *
