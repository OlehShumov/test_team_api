from rest_framework.viewsets import ModelViewSet


from .models import Team, Person
from .serializers import (
    TeamSerializer,
    TeamListSerializer,
    PersonSerializer,
    PersonListSerializer,
)


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return TeamListSerializer
        return TeamSerializer


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.select_related("team")
    serializer_class = PersonSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return PersonListSerializer
        return PersonSerializer
