from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    # pwd = models.CharField("비밀번호", max_length=20, null=True)
    name = models.CharField("이름", max_length=20, null=True)
    score = models.IntegerField("점수", default=0)


class Game(models.Model):
    status = models.IntegerField("상태")
    rule = [
        "숫자가 더 작은 사람이 대결에서 이깁니다",
        "숫자가 더 큰 사람이 대결에서 이깁니다",
    ]
    attackerId = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="attacker"
    )
    attackerCard = models.IntegerField("공격자 카드", default=0)
    defenderId = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="defender"
    )
    defenderCard = models.IntegerField("방어자 카드", default=0)
    winner = models.IntegerField("승리자", null=True, default = 0)
