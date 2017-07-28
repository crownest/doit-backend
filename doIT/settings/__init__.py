# Standard Library
import getpass

# Local Django
from doIT.settings.base import *


if getpass.getuser() in ['root']:
    from doIT.settings.prod import *
elif getpass.getuser() in ['vagrant', 'ubuntu', 'doit']:
    from doIT.settings.staging import *
else:
    from doIT.settings.dev import *
