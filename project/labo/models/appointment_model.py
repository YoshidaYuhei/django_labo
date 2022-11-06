from django.db import models
from labo.models.category_model import Category
from labo.models.user_model import User
from labo.models.item_model import Item

PAYMENT_METHODS = [
    ('Store', 'コンビニ決済'),
    ('Card', 'コンビニ決済'),
    ('QR', 'バーコード決済'),
]

class Appointment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    item_id = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    payment_method = models.CharField(max_length=30, choices=PAYMENT_METHODS)
    payment_deadline = models.CharField(max_length=30)
    schedule = models.CharField(max_length=30)
    
    class Meta:
        db_table = "appointments"
    