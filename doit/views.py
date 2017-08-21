# Django
from django.conf import settings
from django.views.static import serve
from django.views.generic import View


class DocumentationView(View):

    def get(self, request, path='index.html', **kwargs):
        return serve(
            request, path, document_root=settings.DOCUMENTATION_ROOT, **kwargs
        )
