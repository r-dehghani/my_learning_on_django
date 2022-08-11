from django.test import TestCase
from django.contrib.auth.password_validation import validate_password
from django.conf import settings


class MyLearningOnDjangoConfigTest(TestCase):
    def test_SECRET_KEY_strength(self):
        secret_key = settings.SECRET_KEY
        try:
            is_strong = validate_password(secret_key)
        except Exception as e:
            msg = "weak password for secret key"
            self.fail(msg)
