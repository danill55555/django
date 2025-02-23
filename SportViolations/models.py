from django.db import models
from django.contrib.auth.models import User
from datetime import date

ROLE_CHOICES = [
    ('admin', 'Администратор'),
    ('trainer', 'Тренер'),
]


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=150)
    patronymic = models.CharField(max_length=150)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.surname} {self.patronymic}"

    @property
    def athlete_count(self):
        return Questionnaire.objects.filter(trainer=self).count()  # Подсчет спортсменов связанного тренера

class Questionnaire(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    qualification = models.TextField()
    experience = models.TextField()
    chronic_conditions = models.TextField()
    mother_height = models.TextField()
    dad_height = models.TextField()
    mother_sport = models.TextField()
    dad_sport = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)
    trainer = models.ForeignKey(Account, on_delete=models.CASCADE)  # Связь с аккаунтом тренера
    survey_id = models.AutoField(primary_key=True)  # Уникальный идентификатор анкеты
    is_created = models.BooleanField(default=False)  # Флаг создания анкеты

class Anthropometry(models.Model):
    student = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, related_name='anthropometry')
    height = models.FloatField(verbose_name='Рост')
    weight = models.FloatField(verbose_name='Масса')
    foot_length = models.FloatField(verbose_name='Длина стопы')
    shin_length = models.FloatField(verbose_name='Длина голени')
    thigh_length = models.FloatField(verbose_name='Длина бедра')
    arm_span = models.FloatField(verbose_name='Размах рук')
    waist_circumference = models.FloatField(verbose_name='Объем талии')
    hip_circumference = models.FloatField(verbose_name='Объем бедер')
    chest_circumference = models.FloatField(verbose_name='Окружность грудной клетки')

    is_created = models.BooleanField(default=False)  # Новое поле, которое будет True, если анкета была создана

class WristDynamometry(models.Model):
    student = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, related_name='wrist_dynamometry')
    left_hand = models.FloatField(verbose_name='Левая рука')
    right_hand = models.FloatField(verbose_name='Правая рука')


# class SpecificAbilities(models.Model):
#     student = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, related_name='specific_abilities')
#     rhythm_sense = models.FloatField(verbose_name='Чувство ритма')
#     musicality = models.FloatField(verbose_name='Музыкальность')
#     technique = models.FloatField(verbose_name='Техничность')
#     plasticity = models.FloatField(verbose_name='Пластичность')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    birth_date = models.DateField()

    def __str__(self):
        return self.user.username