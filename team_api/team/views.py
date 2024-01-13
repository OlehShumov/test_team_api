from rest_framework.viewsets import ModelViewSet


from .models import Team, Person
from .serializers import (
    TeamSerializer,
    TeamListSerializer,
    PersonSerializer,
    PersonListSerializer,
    PersonDetailSerializer,
    TeamDetailSerializer,
)


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return TeamListSerializer
        elif self.action == "retrieve":
            return TeamDetailSerializer
        return TeamSerializer


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.select_related("team")
    serializer_class = PersonSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return PersonListSerializer
        elif self.action == "retrieve":
            return PersonDetailSerializer
        return PersonSerializer
