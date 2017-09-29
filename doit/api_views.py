# Third-Party
from djoser.views import LoginView as _LoginView

# Local Django
from doit.serializers import LoginSerializer


class LoginView(_LoginView):
    serializer_class = LoginSerializer
