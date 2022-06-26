from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import TemplateView


class ProtendTemplateView(PermissionRequiredMixin, TemplateView):
    permission_required = 'is_superuser'

    def get_template_names(self):
        return ['protend/' + self.kwargs['page'] + '.html']
