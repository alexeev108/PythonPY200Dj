from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from landing.forms import TemplateForm


class TemplView(View):
    def get(self, request):
        return render(request, 'landing/index.html')

    def post(self, request):
        received_data = request.POST  # Приняли данные в словарь
        form = TemplateForm(received_data)
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]  # Получение IP
        else:
            ip = request.META.get('REMOTE_ADDR')  # Получение IP

        user_agent = request.META.get('HTTP_USER_AGENT')
        if form.is_valid():
            data = form.cleaned_data
            data.update(ip=ip, user_agent=user_agent)
            return JsonResponse(data=data,
                                json_dumps_params={"indent": 4, "ensure_ascii": False})
        return render(request, 'landing/index.html', context={'form': form})
