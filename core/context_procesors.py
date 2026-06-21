from django.conf import settings


def notification_ms(request):
    """
    Disponibiliza as configurações do microsserviço de notificação
    em todos os templates.
    """

    context = {
        'NOTIFICATION_MS_URL' : settings.NOTIFICATION_MS_URL,
        'NOTIFICATION_MS_API_KEY': settings.NOTIFICATION_MS_API_KEY,
    }

    if request.user.is_authenticated:
        context['NOTIFICATION_USER_ID'] = request.user.id

    return context