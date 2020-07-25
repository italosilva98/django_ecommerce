from django.views.generic.base import TemplateView



class HomePageView(TemplateView):

    template_name = "home_page.html"

    def get_context_data(self, **kwargs):
        context = {
            "title": "Página principal",
            "content": "Bem-vindo a página principal"
        }
        return context

class AboutPageView(TemplateView):

    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = {
            "title": "Página About",
            "content": "Bem-vindo a página About"
        }
        return context

class ContactPageView(TemplateView):

    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        context = {
            "title": "Página Contato",
            "content": "Bem-vindo a página de contato"
        }
        return context





