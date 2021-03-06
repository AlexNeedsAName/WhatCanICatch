# Generated by Django 3.0.4 on 2020-03-29 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fish', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='southern',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='fish',
            name='size',
            field=models.CharField(choices=[('t', 'Tiny'), ('s', 'Small'), ('T', 'Long & Thin'), ('m', 'Medium'), ('f', 'Fin'), ('l', 'Large'), ('L', 'Very Large'), ('H', 'Huge'), ('F', 'Huge with Fin')], max_length=1),
        ),
    ]
