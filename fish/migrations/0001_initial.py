# Generated by Django 3.0.4 on 2020-03-28 04:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fish',
            fields=[
                ('name', models.CharField(max_length=19, primary_key=True, serialize=False)),
                ('location', models.CharField(choices=[('P', 'Pond'), ('S', 'Sea'), ('M', 'River (Mouth)'), ('R', 'River'), ('r', 'River/Pond'), ('c', 'River (Clifftop)'), ('p', 'Pier'), ('s', 'Sea (Rainy Days)')], max_length=1)),
                ('size', models.CharField(choices=[('t', 'Tiny'), ('s', 'Small'), ('T', 'Long & Thin'), ('m', 'Medium'), ('f', 'Medium with Fin'), ('l', 'Large'), ('L', 'Very Large'), ('H', 'Huge'), ('F', 'Huge with Fin')], max_length=1)),
                ('months', models.DecimalField(decimal_places=0, max_digits=4)),
                ('times', models.DecimalField(decimal_places=0, max_digits=18)),
                ('price', models.DecimalField(decimal_places=0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('caught', models.ManyToManyField(to='fish.Fish')),
            ],
        ),
    ]
