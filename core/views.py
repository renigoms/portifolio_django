from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from core.models import Profile
from core.serializers import ProfileSerializer


# Create your views here.


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """
            Em vez de buscar pelo pk da URL, busca pelo usuário logado.
            Se o perfil não existir, cria um vazio automáticamente.
        """
        profile, created = Profile.objects.get_or_create(
            user=self.request.user,
            defaults={'name': self.request.user.username}
        )

        return profile

