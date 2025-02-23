# Generated by Django 4.2.11 on 2025-02-21 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='NAME', max_length=255)),
                ('ful_name', models.CharField(db_column='FUL_NAME', max_length=255)),
                ('representative_name', models.CharField(db_column='REPRESENTATIVE_NAME', max_length=255)),
                ('representative_last_name', models.CharField(db_column='REPRESENTATIVE_LAST_NAME', max_length=255)),
                ('address', models.CharField(db_column='ADDRESS', max_length=255)),
                ('inn', models.BigIntegerField(db_column='INN')),
                ('kpp', models.BigIntegerField(db_column='KPP')),
                ('industry', models.CharField(db_column='INDUSTRY', max_length=255)),
                ('phone', models.BigIntegerField(db_column='PHONE')),
                ('email', models.CharField(db_column='EMAIL', max_length=255)),
                ('revenue', models.BigIntegerField(db_column='REVENUE')),
            ],
            options={
                'db_table': 'company',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='NAME', max_length=255)),
                ('last_name', models.CharField(db_column='LAST_NAME', max_length=255)),
                ('gender', models.CharField(db_column='GENDER', max_length=255)),
                ('source', models.CharField(db_column='SOURCE', max_length=255)),
                ('phone', models.BigIntegerField(db_column='PHONE')),
                ('email', models.CharField(db_column='EMAIL', max_length=255)),
                ('person_age', models.IntegerField(blank=True, db_column='PERSON_AGE', null=True)),
                ('person_income', models.BigIntegerField(blank=True, db_column='PERSON_INCOME', null=True)),
                ('person_home_ownership', models.BigIntegerField(blank=True, db_column='PERSON_HOME_OWNERSHIP', null=True)),
                ('person_emp_length', models.FloatField(blank=True, db_column='PERSON_EMP_LENGTH', null=True)),
                ('loan_grade', models.CharField(blank=True, db_column='LOAN_GRADE', max_length=255, null=True)),
                ('cb_person_cred_hist_length', models.BigIntegerField(blank=True, db_column='CB_PERSON_CRED_HIST_LENGTH', null=True)),
                ('cb_person_default_on_file', models.IntegerField(blank=True, db_column='CB_PERSON_DEFAULT_ON_FILE', null=True)),
            ],
            options={
                'db_table': 'contact',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CrmDeal',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(db_column='TITLE', max_length=255)),
                ('loan_amount', models.BigIntegerField(db_column='LOAN_AMOUNT')),
                ('stage', models.CharField(db_column='STAGE', max_length=255)),
                ('source', models.CharField(blank=True, db_column='SOURCE', max_length=255, null=True)),
                ('comment', models.TextField(blank=True, db_column='COMMENT', null=True)),
                ('date_closed', models.DateField(blank=True, db_column='DATE_CLOSED', null=True)),
                ('result', models.IntegerField(blank=True, db_column='RESULT', null=True)),
                ('profit', models.BigIntegerField(blank=True, db_column='PROFIT', null=True)),
                ('loan_duration', models.BigIntegerField(blank=True, db_column='LOAN_DURATION', null=True)),
                ('loan_status', models.BigIntegerField(blank=True, db_column='LOAN_STATUS', null=True)),
            ],
            options={
                'db_table': 'crm_deal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LandingRate',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(db_column='TITLE', max_length=255)),
                ('rate', models.FloatField(db_column='RATE')),
                ('loan_intent', models.CharField(db_column='LOAN_INTENT', max_length=255)),
            ],
            options={
                'db_table': 'landing_rate',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('count_month', models.IntegerField(db_column='COUNT_MONTH')),
                ('count_contact', models.IntegerField(db_column='COUNT_CONTACT')),
                ('count_company', models.IntegerField(db_column='COUNT_COMPANY')),
                ('money_turnover', models.BigIntegerField(db_column='MONEY_TURNOVER')),
                ('comment', models.TextField(blank=True, db_column='COMMENT', null=True)),
            ],
            options={
                'db_table': 'statement',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='NAME', max_length=255)),
                ('last_name', models.CharField(db_column='LAST_NAME', max_length=255)),
                ('email', models.CharField(db_column='EMAIL', max_length=255)),
                ('password', models.CharField(db_column='PASSWORD', max_length=255)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
