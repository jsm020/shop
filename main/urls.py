# urls.py

from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='shop/index.html'), name='index'),
    # Boshqa URL lar...
]
