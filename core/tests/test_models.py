from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@xyz.com'
        password = 'test1234'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
    
    def test_new_user_email_normalized(self):
        email = 'test@XYZ.COM'
        user = get_user_model().objects.create_user(email, 'test1234')
        self.assertEqual(user.email, email.lower())
    
    def test_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test1234')
    
    def test_create_new_super_user(self):
        user= get_user_model().objects.create_superuser(
            'test@xyz.com',
            'test1234'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)