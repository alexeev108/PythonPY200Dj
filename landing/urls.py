from django.urls import path

from landing.views import TemplView

app_name = 'landing'

urlpatterns = [
    path('', TemplView.as_view(), name='post_landing'),
    # TODO добавьте здесь маршрут для вашего обработчика отображения страницы приложения landing
]