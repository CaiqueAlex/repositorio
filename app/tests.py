from django.urls import path
from django.http import HttpRequest, JsonResponse
from django.template.loader import render_to_string
from . import views
from django.contrib.auth.views import LogoutView
from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
from app import views
from django.contrib.auth.models import User
from .termo import Termo, Feedback, InvalidAttempt
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import os
import json

class RegisterTestCase(TestCase):
    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        print("Register View...OK")

    def test_register_post(self):
        data = {'username': 'testuser', 'password1': 'testpassword', 'password2': 'testpassword'}
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 302)  # Redireciona após registro bem-sucedido
        print("Register Post...OK")


class LoginTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        print("Login View...OK")

    def test_login_post(self):
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, 302)  # Redireciona após login bem-sucedido
        print("Login Post...OK")


class GameTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_game_view(self):
        response = self.client.get(reverse('game'))
        self.assertEqual(response.status_code, 200)
        print("Game View...OK")


class PasswordResetTestCase(TestCase):
    def test_password_reset_view(self):
        response = self.client.get(reverse('reset_password'))
        self.assertEqual(response.status_code, 200)
        print("Password Reset View...OK")
