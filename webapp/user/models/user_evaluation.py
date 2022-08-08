from django.db import models
from config.models import BaseModel
from django.core.validators import MaxValueValidator, MinValueValidator

from dealing.models import Dealing
from user.models import User


class UserEvaluation(BaseModel):

    class Meta:
        db_table = 'user_evaluations'
        verbose_name = 'UserEvaluation'
        verbose_name_plural = 'UserEvaluations'

        constraints = [
            models.UniqueConstraint(
                fields=['user', 'dealing'],
                name='unique user dealing',
            )
        ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='유저'
    )
    dealing = models.ForeignKey(
        Dealing,
        on_delete=models.CASCADE,
        verbose_name='거래 내역'
    )
    rate = models.IntegerField(
        verbose_name='점수',
        null=False,
        validators=[
            MaxValueValidator(5, message='점수는 5까지 설정할 수 있습니다.'),
            MinValueValidator(1, message='점수는 0보다 커야 합니다.')
        ],
    )
