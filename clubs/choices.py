from django.db import models


class StatusChoice(models.IntegerChoices):
    Free = 1, 'Свободно'
    Busy = 2, 'Занято'
    Under_repair = 3, 'В данный момент компьютер находится на тех-обслуживании'