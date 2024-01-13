from rest_framework import serializers

from .models import Team, Person


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class TeamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"


class PersonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
