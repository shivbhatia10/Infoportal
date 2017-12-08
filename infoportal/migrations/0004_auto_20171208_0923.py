# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-08 03:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infoportal', '0003_remove_post_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='catagory',
            field=models.CharField(choices=[('School Wide', 'School Wide'), ('Environmental Initiatives', 'Environmental Initiatives'), ('Interschool Events', 'Interschool Events'), ('Intraschool Events', 'Intraschool Events'), ('Social Projects', 'Social Projects'), ('Sports', 'Sports')], default='School Wide', max_length=30),
        ),
        migrations.AddField(
            model_name='post',
            name='society',
            field=models.CharField(choices=[('All Societies', 'All Societies'), ('Computer', 'Computer'), ('Dance', 'Dance'), ('Drama', 'Drama'), ('Economics', 'Economics'), ('Maths', 'Maths'), ('MUN', 'MUN'), ('Music', 'Music'), ('Photography', 'Photography'), ('Quiz', 'Quiz'), ('Science', 'Science')], default='All Societies', max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='house',
            field=models.CharField(choices=[('All Houses', 'All Houses'), ('Srishti', 'Srishti'), ('Sagar', 'Sagar'), ('Vasundhara', 'Vasundhara'), ('Himgiri', 'Himgiri')], default='All Houses', max_length=30),
        ),
    ]
