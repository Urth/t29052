from django.test import TestCase

from .models import Question

class TestPoll(TestCase):
    databases = ['default', 'security']

    def test_first_poll(self):
        assert Question.objects.all().exists()
