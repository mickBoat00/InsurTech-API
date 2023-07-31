# Generated by Django 4.2.3 on 2023-07-31 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoPolicyDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=50)),
                ('year', models.PositiveIntegerField()),
                ('vin', models.CharField(max_length=17, unique=True)),
                ('usage', models.CharField(max_length=50)),
                ('mileage', models.PositiveIntegerField()),
                ('rating', models.PositiveIntegerField(blank=True, null=True)),
                ('verified', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auto_documents', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AutoCoverageDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_liability_per_person', models.PositiveIntegerField(blank=True, help_text='Amount paid per person involved', null=True)),
                ('total_body_liability', models.PositiveIntegerField(blank=True, help_text='Total amount for all parties involved', null=True)),
                ('property_damage_liability', models.PositiveIntegerField(blank=True, help_text='Total amount paid for other party propert damage.', null=True)),
                ('comprehensive', models.BooleanField(default=False, help_text='Non collision incident ie theft, fire, vandalism')),
                ('collision', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('auto_documents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_insurance.autopolicydocument')),
            ],
        ),
    ]
