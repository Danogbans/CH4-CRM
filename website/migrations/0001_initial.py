# Generated by Django 4.2 on 2023-04-21 09:59

from django.db import migrations, models    


class Migration(migrations.Migration): 

    initial = True

    dependencies = [
    ] 

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),   
                ('creation_date', models.DateTimeField(auto_now_add=True)), 
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=20)),
            ],
        ),
    ]
