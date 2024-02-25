from django.shortcuts import render
from django.views import generic


class HomeView(generic.TemplateView):
    template_name = 'catalog/homepage.html'
    extra_context = {
        'title': 'Домашняя страницая'
    }

class ContactsView(generic.TemplateView):
    template_name = 'contacts.html'
    extra_context = {
        'title': 'Контакты'
    }

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        print(f'User {name}, with {phone}, send message: {message}')
        return render(request, self.template_name)