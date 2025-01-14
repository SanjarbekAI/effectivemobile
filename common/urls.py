from django.urls import path

from common.views import HomePageTemplateView

app_name = 'common'

urlpatterns = [
    path('', HomePageTemplateView.as_view(), name='home')
]
