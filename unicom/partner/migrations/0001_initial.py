# Generated by Django 2.0 on 2017-12-13 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('creditor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationForCreditor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
                ('phone', models.CharField(max_length=50)),
                ('passport', models.CharField(max_length=50)),
                ('credit_score', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='applicationforcreditor',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partner.Client'),
        ),
        migrations.AddField(
            model_name='applicationforcreditor',
            name='requested_credit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='creditor.Credit'),
        ),
    ]