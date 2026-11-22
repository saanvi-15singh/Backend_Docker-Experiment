import unittest
import requests

BASE_URL = "http://127.0.0.1:8000"


class StudentAPITests(unittest.TestCase):

    def test_home(self):
        response = requests.get(BASE_URL + "/")
        self.assertEqual(response.status_code, 200)
        print("Home route tested successfully")

    def test_health(self):
        response = requests.get(BASE_URL + "/health")
        self.assertEqual(response.status_code, 200)
        print("Health route tested successfully")

    def test_get_students(self):
        response = requests.get(BASE_URL + "/students")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        print("Get students tested successfully")

    def test_get_student(self):
        response = requests.get(BASE_URL + "/students/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["id"], 1)
        print("Get student by ID tested successfully")

    def test_add_student(self):
        data = {
            "name": "Rahul",
            "course": "Computer Science"
        }

        response = requests.post(BASE_URL + "/students", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "Rahul")
        print("Add student tested successfully")

    def test_update_student(self):
        data = {
            "name": "Rahul Updated",
            "course": "CSE"
        }

        response = requests.put(BASE_URL + "/students/1", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "Rahul Updated")
        print("Update student tested successfully")

    def test_delete_student(self):
        response = requests.delete(BASE_URL + "/students/2")
        self.assertEqual(response.status_code, 200)
        print("Delete student tested successfully")

    def test_invalid_student(self):
        response = requests.get(BASE_URL + "/students/999")
        self.assertEqual(response.status_code, 404)
        print("Invalid student test passed")


if __name__ == "__main__":
    unittest.main(verbosity=2)