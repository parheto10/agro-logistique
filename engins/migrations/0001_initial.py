# Generated by Django 3.2.6 on 2021-11-18 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parametres', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chauffeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prenoms', models.CharField(blank=True, max_length=255, null=True)),
                ('contact1', models.CharField(max_length=255)),
                ('contact2', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'chauffeur',
                'verbose_name_plural': 'CHAUFFEURS',
                'ordering': ['nom'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('km_depart', models.PositiveIntegerField(default=0)),
                ('km_arrive', models.PositiveIntegerField(default=0)),
                ('distance', models.PositiveIntegerField(default=0)),
                ('motif', models.CharField(max_length=255)),
                ('responsable', models.CharField(max_length=255)),
                ('chauffeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engins.chauffeur')),
            ],
            options={
                'verbose_name': 'course',
                'verbose_name_plural': 'COURSES',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Moto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('MOTO', 'MOTO'), ('TRYCICLE', 'TRYCICLE')], max_length=255)),
                ('matricule', models.CharField(max_length=255)),
                ('prix_achat', models.PositiveIntegerField(default=0)),
                ('date_achat', models.DateField(blank=True, null=True)),
                ('mise_en_circulation', models.DateField(blank=True, null=True)),
                ('marque', models.CharField(blank=True, max_length=255, null=True)),
                ('model', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'vehicule',
                'verbose_name_plural': 'VEHICULES',
                'ordering': ['matricule'],
            },
        ),
        migrations.CreateModel(
            name='Vehicule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.CharField(max_length=255)),
                ('prix_achat', models.PositiveIntegerField(default=0)),
                ('date_achat', models.DateField(blank=True, null=True)),
                ('mise_en_circulation', models.DateField(blank=True, null=True)),
                ('marque', models.CharField(blank=True, max_length=255, null=True)),
                ('model', models.CharField(blank=True, max_length=255, null=True)),
                ('couleur', models.CharField(choices=[('BLANCHE', 'BLANCHE'), ('GRISE', 'GRISE'), ('NOIRE', 'NOIRE')], max_length=255)),
            ],
            options={
                'verbose_name': 'vehicule',
                'verbose_name_plural': 'VEHICULES',
                'ordering': ['matricule'],
            },
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_depart', models.DateField()),
                ('date_retours', models.DateField(blank=True, null=True)),
                ('nb_jour', models.PositiveIntegerField(default=0)),
                ('ville_depart', models.CharField(max_length=255)),
                ('km_depart', models.PositiveIntegerField(default=0)),
                ('km_arrive', models.PositiveIntegerField(default=0)),
                ('distance', models.PositiveIntegerField(default=0)),
                ('motif', models.CharField(max_length=255)),
                ('frais_location', models.PositiveIntegerField(default=0)),
                ('total_location', models.PositiveIntegerField(default=0)),
                ('chauffeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engins.chauffeur')),
                ('projet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametres.projet')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametres.responsable')),
                ('voiture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engins.vehicule')),
            ],
            options={
                'verbose_name': 'mission',
                'verbose_name_plural': 'MISSIONS',
                'ordering': ['-date_depart'],
            },
        ),
        migrations.CreateModel(
            name='Escale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localite', models.CharField(max_length=255)),
                ('date_arrivee', models.DateField()),
                ('km_depart', models.PositiveIntegerField(default=0)),
                ('km_arrive', models.PositiveIntegerField(default=0)),
                ('date_depart', models.DateField()),
                ('mission_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engins.mission')),
            ],
            options={
                'verbose_name': 'escale mission',
                'verbose_name_plural': 'ESCALES MISSIONS',
                'ordering': ['-date_arrivee'],
            },
        ),
        migrations.CreateModel(
            name='detail_mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(choices=[('CARBURANT', 'CARBURANT'), ('VIDANGE', 'VIDANGE'), ('REPARATION/ACHAT', 'REPARATION/ACHAT'), ('PEAGE', 'PEAGE'), ('LAVAGE', 'LAVAGE')], max_length=255)),
                ('qte_acheter', models.PositiveIntegerField(default=0)),
                ('prix_unitaire', models.PositiveIntegerField(default=0)),
                ('montant_total', models.PositiveIntegerField(default=0)),
                ('mission_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engins.mission')),
            ],
            options={
                'verbose_name': 'detail mission',
                'verbose_name_plural': 'DETAILS MISSIONS',
                'ordering': ['-mission_id__date_depart'],
            },
        ),
        migrations.CreateModel(
            name='Detail_Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(choices=[('CARBURANT', 'CARBURANT'), ('VIDANGE', 'VIDANGE'), ('REPARATION/ACHAT', 'REPARATION/ACHAT'), ('PEAGE', 'PEAGE'), ('LAVAGE', 'LAVAGE')], max_length=255)),
                ('qte_acheter', models.PositiveIntegerField(default=0)),
                ('prix_unitaire', models.PositiveIntegerField(default=0)),
                ('montant_total', models.PositiveIntegerField(default=0)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engins.course')),
            ],
            options={
                'verbose_name': 'detail course',
                'verbose_name_plural': 'DETAILS COURSES',
                'ordering': ['-course_id__date'],
            },
        ),
        migrations.AddField(
            model_name='course',
            name='voiture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engins.vehicule'),
        ),
    ]
