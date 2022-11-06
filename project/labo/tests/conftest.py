from pytest_factoryboy import register
from labo.tests.factories import UserFactory
from labo.tests.factories import ItemFactory
from labo.tests.factories import AppointmentFactory


register(UserFactory)
register(ItemFactory)
register(AppointmentFactory)
