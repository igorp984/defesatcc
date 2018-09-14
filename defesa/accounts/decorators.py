from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from .models import Perfil

def acesso(tipo):
    def nivel(function):
        actual_decorator = user_passes_test(
            valida_perfil(tipo),
            login_url='core:home',
            redirect_field_name=REDIRECT_FIELD_NAME
        )
        if function:
            return actual_decorator(function)
        return actual_decorator
    return nivel


def valida_perfil(tipo):
    def valida(user):
        p = Perfil()
        print(tipo == p.get_perfil(user.perfil))
        if tipo == p.get_perfil(user.perfil):
            return True
        else:
            return False
    return valida

