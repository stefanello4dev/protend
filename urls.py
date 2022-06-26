from django.urls import path

from protend.views import ProtendTemplateView

urlpatterns = [
    path('<slug:page>.html', ProtendTemplateView.as_view(template_name='protend/index.html')),
]
