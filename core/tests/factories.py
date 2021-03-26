import pytz
from factory import Faker, PostGenerationMethodCall, SubFactory
from factory.django import DjangoModelFactory

from core.models import User, Note, Patient


class UserFactory(DjangoModelFactory):
    username = Faker('user_name')
    password = PostGenerationMethodCall('set_password', 'password')
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    email = Faker('email')

    class Meta:
        model = User


class PatientFactory(DjangoModelFactory):
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    email = Faker('email')

    class Meta:
        model = Patient


class NoteFactory(DjangoModelFactory):
    patient = SubFactory(PatientFactory)
    nutritionist = SubFactory(UserFactory)
    description = Faker('bs')
    date = Faker('date_time', tzinfo=pytz.UTC)

    class Meta:
        model = Note
