# Generated by Django 2.2.24 on 2022-02-15 12:53

from django.db import migrations
from ..models import Flat
import phonenumbers


def normalize_phone_nums(apps, schema_editor):
    flats = Flat.objects.all()
    for flat in flats:
        parsed_phone_num = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(parsed_phone_num):
            flat.owner_pure_phone = '+' + str(parsed_phone_num.country_code) + str(parsed_phone_num.national_number)
        else:
            flat.owner_pure_phone = None

        flat.save()



class Migration(migrations.Migration):
    dependencies = [
        ('property', '0009_auto_20220215_1551'),
    ]

    operations = [
        migrations.RunPython(normalize_phone_nums)
    ]
