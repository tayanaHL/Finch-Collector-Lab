# Generated by Django 4.1.7 on 2023-03-13 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_finch_created_at_finch_updated_at_feeding'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeding',
            name='finch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedings', to='main_app.finch'),
        ),
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('finches', models.ManyToManyField(related_name='toys', to='main_app.finch')),
            ],
        ),
    ]
