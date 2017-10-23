from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User

from agenda.models import Agenda
from agenda.models import Usuario

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')
class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('nome', 'iduser')


class AgendaSerializer(serializers.HyperlinkedModelSerializer):
    iduser = UsuarioSerializer(many=False) #tem que ser o mesmo nome que ta no model
    class Meta:
        model = Agenda
        fields = ('compromisso','descricao','privado','institucional','iduser')


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'is_staff')

