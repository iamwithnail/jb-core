# Generated by Django 2.0.8 on 2018-08-22 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('pdf_agreement', models.URLField()),
                ('rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.TextField()),
                ('street_address', models.CharField(max_length=30)),
                ('town', models.CharField(max_length=30)),
                ('postcode', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cscs_card_number', models.IntegerField()),
                ('cscs_card_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Hirer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30)),
                ('company_number', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('postcode', models.TextField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('rate', models.IntegerField()),
                ('rate_type', models.IntegerField(choices=[(1, 'Hourly'), (2, 'Daily'), (3, 'Weekly'), (4, '4 Weekly'), (5, 'Monthly'), (6, 'Annually')])),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('skill_code', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ContractorContactDetails',
            fields=[
                ('contactdetails_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.ContactDetails')),
                ('field', models.TextField()),
                ('name', models.TextField()),
            ],
            bases=('core.contactdetails',),
        ),
        migrations.CreateModel(
            name='HirerContactDetails',
            fields=[
                ('contactdetails_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.ContactDetails')),
                ('invoice_contact', models.EmailField(max_length=254)),
            ],
            bases=('core.contactdetails',),
        ),
        migrations.AddField(
            model_name='role',
            name='skills',
            field=models.ManyToManyField(to='core.Skill'),
        ),
        migrations.AddField(
            model_name='location',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Role'),
        ),
        migrations.AddField(
            model_name='contractor',
            name='skills',
            field=models.ManyToManyField(to='core.Skill'),
        ),
        migrations.AddField(
            model_name='agreement',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Hirer'),
        ),
        migrations.AddField(
            model_name='contractor',
            name='contact',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.ContractorContactDetails'),
        ),
    ]
