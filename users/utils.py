from django.contrib.auth.models import User
import random
import string

def create_guest_user():
    username = 'guest_' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    password = User.objects.make_random_password()
    guest_user = User.objects.create_user(username=username, password=password)
    return guest_user