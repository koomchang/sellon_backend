# Generated by Django 4.0.6 on 2022-08-09 02:13

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dealing', '0004_alter_dealing_product_alter_dealing_product_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='DealingEvaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='추가된 일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정된 일시')),
                ('rate', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5, message='점수는 5까지 설정할 수 있습니다.'), django.core.validators.MinValueValidator(1, message='점수는 0보다 커야 합니다.')], verbose_name='점수')),
                ('dealing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dealing.dealing', verbose_name='거래 내역')),
                ('evaluated_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='evaluated_user', to=settings.AUTH_USER_MODEL, verbose_name='평가 받는 유저')),
                ('evaluator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='evaluator', to=settings.AUTH_USER_MODEL, verbose_name='평가 하는 유저')),
            ],
            options={
                'verbose_name': 'DealingEvaluation',
                'verbose_name_plural': 'DealingEvaluations',
                'db_table': 'dealing_evaluations',
            },
        ),
        migrations.AddConstraint(
            model_name='dealingevaluation',
            constraint=models.UniqueConstraint(fields=('evaluated_user', 'dealing'), name='unique_evaluated_user_dealing'),
        ),
    ]
