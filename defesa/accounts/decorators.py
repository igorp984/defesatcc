from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from .models import Perfil

def acesso(tipo):
    def nivel(function):
        actual_decorator = user_passes_test(
            valida_perfil,
            login_url='core:home',
            redirect_field_name=REDIRECT_FIELD_NAME
        )
        if function:
            return actual_decorator(function)
        return actual_decorator
    return nivel


def valida_perfil(user):
    p = Perfil()
    if user.perfil == p.get_perfil(user.perfil):
        return True
    else:
        return False

