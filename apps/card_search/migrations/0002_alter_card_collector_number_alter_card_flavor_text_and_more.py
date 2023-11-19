# Generated by Django 4.2.3 on 2023-11-12 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card_search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='collector_number',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='card',
            name='flavor_text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='card',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='card',
            name='oracle_text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='card',
            name='type_line',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cardset',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cardset',
            name='set_code',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='color',
            name='color',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='coloridentity',
            name='color_identity',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='gametype',
            name='game_type',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='keyword',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='layout',
            name='layout',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='legality',
            name='legality',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='manacost',
            name='mana_cost',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='rarity',
            name='rarity',
            field=models.CharField(max_length=255),
        ),
    ]