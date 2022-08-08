# Generated by Django 4.0.6 on 2022-08-08 16:20

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dealing', '0002_remove_dealing_deleted_at'),
        ('user', '0005_delete_inventory'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserEvaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='추가된 일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정된 일시')),
                ('rate', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5, message='점수는 5까지 설정할 수 있습니다.'), django.core.validators.MinValueValidator(1, message='점수는 0보다 커야 합니다.')], verbose_name='점수')),
                ('dealing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealing.dealing', verbose_name='거래 내역')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='유저')),
            ],
            options={
                'verbose_name': 'UserEvaluation',
                'verbose_name_plural': 'UserEvaluations',
                'db_table': 'user_evaluations',
            },
        ),
        migrations.AddConstraint(
            model_name='userevaluation',
            constraint=models.UniqueConstraint(fields=('user', 'dealing'), name='unique user dealing'),
        ),
    ]
