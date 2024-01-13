from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    email = models.EmailField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="people")

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

