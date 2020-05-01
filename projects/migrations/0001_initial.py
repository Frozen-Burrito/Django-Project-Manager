# Generated by Django 3.0.2 on 2020-04-24 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('project_type', models.CharField(choices=[('Website', 'Website'), ('Mobile App', 'Mobile App'), ('Web App', 'Web App'), ('Videogame', 'Videogame'), ('3D Model', '3D Model')], max_length=50)),
                ('date_created', models.DateField()),
                ('team', models.BooleanField()),
                ('tags', models.CharField(choices=[('Django', 'Django'), ('Unity', 'Unity'), ('React', 'React'), ('Blender', 'Blender'), ('Flutter', 'Flutter')], max_length=50)),
                ('summary', models.CharField(max_length=200)),
                ('about_project', models.CharField(max_length=500)),
                ('deploy_link', models.URLField()),
            ],
        ),
    ]
