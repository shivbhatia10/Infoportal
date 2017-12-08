# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-08 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infoportal', '0008_auto_20171208_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('SchoolWide', 'SchoolWide'), ('EnvironmentalInitiatives', 'EnvironmentalInitiatives'), ('InterschoolEvents', 'InterschoolEvents'), ('IntraschoolEvents', 'IntraschoolEvents'), ('SocialProjects', 'SocialProjects'), ('Sports', 'Sports')], default='SchoolWide', max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='house',
            field=models.CharField(choices=[('AllHouses', 'AllHouses'), ('Srishti', 'Srishti'), ('Sagar', 'Sagar'), ('Vasundhara', 'Vasundhara'), ('Himgiri', 'Himgiri')], default='AllHouses', max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='society',
            field=models.CharField(choices=[('AllSocieties', 'AllSocieties'), ('Computer', 'Computer'), ('Dance', 'Dance'), ('Drama', 'Drama'), ('Economics', 'Economics'), ('Maths', 'Maths'), ('MUN', 'MUN'), ('Music', 'Music'), ('Photography', 'Photography'), ('Quiz', 'Quiz'), ('Science', 'Science')], default='AllSocieties', max_length=30),
        ),
    ]
