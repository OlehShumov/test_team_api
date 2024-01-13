from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from team.models import Team


class TeamApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        Team.objects.create(name="Team 1")
        Team.objects.create(name="Team 2")

    def test_get_teams(self):
        response = self.client.get("/api/team/teams/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        teams_name = [team["name"] for team in response.data]
        self.assertEqual(
            sorted(teams_name), ["Team 1", "Team 2"]
        )

    def test_post_teams(self):
        response = self.client.post(
            "/api/team/teams/",
            {"name": "Team 3"},
        )
        db_teams = Team.objects.all()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_invalid_teams(self):
        response = self.client.get("/api/team/teams/1001/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_teams(self):
        response = self.client.put(
            "/api/team/teams/1/",
            {"name": "Team 3"},
        )
        team_pk_1 = Team.objects.get(pk=1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            [
                team_pk_1.name,
            ],
            ["Team 3"],
        )

    def test_delete_teams(self):
        response = self.client.delete(
            "/api/team/teams/1/",
        )
        db_team_id_1 = Team.objects.filter(id=1)
        self.assertEqual(db_team_id_1.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_teams(self):
        response = self.client.delete(
            "/api/team/teams/1000/",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
