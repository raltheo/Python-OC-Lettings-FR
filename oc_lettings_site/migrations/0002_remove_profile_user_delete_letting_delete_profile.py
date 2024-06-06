# Generated by Django 5.0.6 on 2024-06-06 14:54

from django.db import migrations

def transfer_data(apps, schema_editor):
    Letting = apps.get_model('oc_lettings_site', 'Letting')
    New_Letting = apps.get_model('lettings', 'Letting')
    
    Profile = apps.get_model('oc_lettings_site', 'Profile')
    New_Profile = apps.get_model('profiles', 'Profile')

    for letting in Letting.objects.using('default').all():
        
        new_letting = New_Letting.objects.create(
            
            title=letting.title,
            addresses=letting.address,
            
        )
        
        new_letting.save()

    for profile in Profile.objects.using('default').all():
        
        new_profile = New_Profile.objects.create(
            
            user=profile.user,
            favorite_city=profile.favorite_city,
            
        )
        
        new_profile.save()

class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(transfer_data),
        migrations.DeleteModel(
            name='Letting',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]