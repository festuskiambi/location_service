# Generated by Django 2.1.3 on 2019-04-25 09:35

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0006_auto_20190408_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiletype',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, help_text='Timestamp when the SiteProfile was created (automatically set, ISO format).'),
        ),
        migrations.AlterField(
            model_name='profiletype',
            name='edit_date',
            field=models.DateTimeField(auto_now=True, help_text='Timestamp when the SiteProfile was last modified (automatically set, ISO format).'),
        ),
        migrations.AlterField(
            model_name='profiletype',
            name='name',
            field=models.CharField(help_text='Name of the ProfileType.', max_length=255),
        ),
        migrations.AlterField(
            model_name='profiletype',
            name='organization_uuid',
            field=models.UUIDField(db_index=True, help_text='ID of the organization that has access to the ProfileType.', verbose_name='Organization UUID'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='address_line1',
            field=models.CharField(blank=True, help_text="First line of the SiteProfile's address, like street and number.", max_length=255, verbose_name='Address line 1'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='address_line2',
            field=models.CharField(blank=True, help_text="Second line of the SiteProfile's address", max_length=255, verbose_name='Address line 2'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='address_line3',
            field=models.CharField(blank=True, help_text="Third line of the SiteProfile's address", max_length=255, verbose_name='Address line 3'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='address_line4',
            field=models.CharField(blank=True, help_text="Fourth line of the SiteProfile's address", max_length=255, verbose_name='Address line 4'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='city',
            field=models.CharField(blank=True, help_text='City where the SiteProfile is located', max_length=85),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='country',
            field=django_countries.fields.CountryField(blank=True, help_text='two-char ISO code', max_length=2),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, help_text='Timestamp when the SiteProfile was created (set automatically, ISO format)'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='edit_date',
            field=models.DateTimeField(auto_now=True, help_text='Timestamp when the SiteProfile was last modified (set automatically, ISO format)'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=16, default=Decimal('0.00'), help_text='Latitude coordinates of the SiteProfile (decimal format)', max_digits=25),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=16, default=Decimal('0.00'), help_text='Longitude coordinates of the SiteProfile (decimal format)', max_digits=25),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='name',
            field=models.CharField(blank=True, help_text='Name of the SiteProfile.', max_length=255),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='notes',
            field=models.TextField(blank=True, help_text='Textual notes for the SiteProfile'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='organization_uuid',
            field=models.UUIDField(db_index=True, help_text='UUID of the organization that has access to the SiteProfile', verbose_name='Organization UUID'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='postcode',
            field=models.CharField(blank=True, help_text='Postal code where the SiteProfile is located', max_length=20),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='profiletype',
            field=models.ForeignKey(blank=True, help_text='UUID of the related ProfileType of the SiteProfile.', null=True, on_delete=django.db.models.deletion.CASCADE, to='location.ProfileType'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='UUID of the SiteProfile.', primary_key=True, serialize=False),
        ),
    ]
