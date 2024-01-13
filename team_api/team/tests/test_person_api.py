from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from team.models import Person, Team
from team.serializers import PersonSerializer, TeamSerializer, PersonDetailSerializer, TeamDetailSerializer


class PersonAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name="Test Team")
        self.person = Person.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            team=self.team,
        )
        self.valid_payload = {
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com",
            "team": self.team.id,
        }
        self.invalid_payload = {
            "first_name": "",
            "last_name": "Doe",
            "email": "jane.doe@example.com",
            "team": self.team.id,
        }

    def test_get_person_list(self):
        response = self.client.get("/api/team/people/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        serialized_data = PersonSerializer(instance=self.person).data
        self.assertEqual(response.data, [serialized_data])

    def test_create_person(self):
        response = self.client.post("/api/team/people/", data=self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.count(), 2)

    def test_create_person_invalid_data(self):
        response = self.client.post("/api/team/people/", data=self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_person_detail(self):
        response = self.client.get(f"/api/team/people/{self.person.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_data = PersonDetailSerializer(instance=self.person).data
        self.assertEqual(response.data, serialized_data)

    def test_update_person(self):
        updated_data = {"first_name": "Updated",
                        "last_name": "Doe",
                        "email": "john.doe@example.com",
                        "team": f"{self.team.id}"}
        response = self.client.put(f"/api/team/people/{self.person.id}/", data=updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.person.refresh_from_db()
        self.assertEqual(self.person.first_name, "Updated")

    def test_delete_person(self):
        response = self.client.delete(f"/api/team/people/{self.person.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Person.objects.count(), 0)
