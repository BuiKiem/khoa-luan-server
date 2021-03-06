# Generated by Django 2.2.5 on 2019-09-19 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line', models.CharField(max_length=100)),
                ('raw', models.CharField(max_length=200)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='address.District')),
            ],
            options={
                'verbose_name_plural': 'Adresses',
                'ordering': ('district', 'address_line'),
            },
        ),
    ]
