# Generated by Django 2.2.6 on 2019-10-24 22:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('JJE_Main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaiverClaim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claim_start', models.DateTimeField(default=django.utils.timezone.now)),
                ('add_player', models.CharField(max_length=255)),
                ('add_LW', models.BooleanField(default=False)),
                ('add_C', models.BooleanField(default=False)),
                ('add_RW', models.BooleanField(default=False)),
                ('add_D', models.BooleanField(default=False)),
                ('add_G', models.BooleanField(default=False)),
                ('add_Util', models.BooleanField(default=False)),
                ('add_IR', models.BooleanField(default=False)),
                ('drop_player', models.CharField(max_length=255)),
                ('drop_LW', models.BooleanField(default=False)),
                ('drop_C', models.BooleanField(default=False)),
                ('drop_RW', models.BooleanField(default=False)),
                ('drop_D', models.BooleanField(default=False)),
                ('drop_G', models.BooleanField(default=False)),
                ('drop_Util', models.BooleanField(default=False)),
                ('drop_IR', models.BooleanField(default=False)),
                ('over_claim_id', models.IntegerField(default=0)),
                ('overclaimed', models.BooleanField(default=False)),
                ('cancelled', models.BooleanField(default=False)),
                ('claim_message', models.TextField(blank=True)),
                ('yahoo_team', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='waiver_team', to='JJE_Main.YahooTeam')),
            ],
            options={
                'ordering': ['-claim_start'],
            },
        ),
    ]
