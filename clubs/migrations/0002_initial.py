# Generated by Django 3.2.4 on 2021-06-12 10:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clubs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner_reservation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reservation',
            name='seats',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seats_reservation', to='clubs.table'),
        ),
        migrations.AddField(
            model_name='pricelist',
            name='club',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='price_list', to='clubs.club'),
        ),
        migrations.AddField(
            model_name='gameaccessoriesspecification',
            name='club',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='game_accessories_specification_list', to='clubs.club'),
        ),
        migrations.AddField(
            model_name='game',
            name='club',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='game_list', to='clubs.club'),
        ),
        migrations.AddField(
            model_name='clubrules',
            name='club',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='club_rules_list', to='clubs.club'),
        ),
        migrations.AddField(
            model_name='clubimage',
            name='club',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='club_image', to='clubs.club'),
        ),
        migrations.AddField(
            model_name='club',
            name='computer_club',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='club_computer_club', to='clubs.computerclub'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='computer_club',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='announcement_computer_club', to='clubs.computerclub'),
        ),
    ]
