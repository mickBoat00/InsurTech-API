# Generated by Django 4.2.3 on 2023-07-29 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auto_insurance', '0002_alter_autopolicydocument_mileage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoCoverageDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_liability_per_person', models.PositiveIntegerField(blank=True, help_text='Amount paid per person involved', null=True)),
                ('total_body_liability', models.PositiveIntegerField(blank=True, help_text='Total amount for all parties involved', null=True)),
                ('property_damage_liability', models.PositiveIntegerField(blank=True, help_text='Total amount paid for other party propert damage.', null=True)),
                ('comprehensive', models.BooleanField(default=False, help_text='Non collision incident ie theft, fire, vandalism')),
                ('collision', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('auto_documents', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auto_insurance.autopolicydocument')),
            ],
        ),
    ]