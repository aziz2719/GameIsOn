from django.db import models
from datetime import timedelta
from django.core.validators import MinValueValidator, MaxValueValidator

class ComputerClub(models.Model):
    computer_club = models.CharField('Компьютерные клубы', max_length=100)
    
    class Meta:
        verbose_name = 'Компьютерный клуб'
        verbose_name_plural = 'Компьютерные клубы'

    def __str__(self):
        return self.computer_club


class Announcement(models.Model):
    computer_club = models.ForeignKey('clubs.ComputerClub', models.CASCADE, related_name='announcement_computer_club', null=True)
    news = models.CharField('Новости', max_length=255)
    text = models.TextField('Текст')
    image = models.FileField('Изображение', upload_to='announcement_image/', blank=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.news


class Club(models.Model):
    computer_club = models.ForeignKey('clubs.ComputerClub', models.CASCADE, related_name='club_computer_club', null=True)
    club = models.CharField('Клуб', max_length=100)
    address = models.CharField('Адрес', max_length=255)
    phone = models.CharField('Телефон', max_length=30)
    seat = models.PositiveSmallIntegerField('Мест')

    class Meta:
        verbose_name = 'Клуб'
        verbose_name_plural = 'Клубы'

    def __str__(self):
        return self.club


class Table(models.Model):
    club = models.ForeignKey('clubs.Club', models.CASCADE, related_name='club_table', null=True)
    place_number = models.IntegerField('Номер места')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return f'{self.place_number}'


class Reservation(models.Model):
    computer_club = models.ForeignKey('clubs.Club', models.CASCADE, related_name='club_reservation', null=True)
    seats = models.ForeignKey('clubs.Table', models.CASCADE, related_name='seats_reservation', null=True)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='owner_reservation', null=True)
    time = models.DateTimeField('Введите время бронирования')
    time1 = models.DateTimeField('Время окончания бронирования', blank=True, null=True)
    using_time = models.PositiveSmallIntegerField('Введите на сколько часов вы садитесь', validators=[MinValueValidator(1,message='Меньше 1 нельзя!'),\
    MaxValueValidator(10,message='Больше 10 нельзя!')])

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирование'
    
    def __str__(self):
        return f'{self.computer_club } {self.seats } {self.time } {self.using_time } {self.time1 } {self.owner }'

    def save(self, *args, **kwargs):
        time = self.time
        time += timedelta(hours=self.using_time)
        self.time1 = time
        super(Reservation, self).save()


class PriceList(models.Model):
    club = models.ForeignKey('clubs.Club', models.CASCADE, related_name='price_list', null=True)
    image = models.FileField('Фото', upload_to = 'price_list_images')

    class Meta:
        verbose_name = 'Прайс лист'
        verbose_name_plural = 'Прайс листы'
    

class Game(models.Model):
    club = models.ForeignKey('clubs.Club', models.CASCADE, related_name='game_list', null=True)
    game = models.CharField('Название игры', max_length=255)
    
    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
    
    def __str__(self):
        return self.game


class ClubRules(models.Model):
    club = models.ForeignKey('clubs.Club', models.CASCADE, related_name='club_rules_list', null=True)
    club_rules = models.CharField('Название правила клуба', max_length=255)
    text = models.TextField('Текст')

    class Meta:
        verbose_name = 'Правило'
        verbose_name_plural = 'Правила'
    
    def __str__(self):
        return self.club_rules


class GameAccessoriesSpecification(models.Model):
    club = models.ForeignKey('clubs.Club', models.CASCADE, related_name='game_accessories_specification_list', null=True)
    game_accessories_specification = models.CharField('Девайс', max_length=255)
    text = models.TextField('Описание характеристики девайса')

    class Meta:
        verbose_name = 'Девайс'
        verbose_name_plural = 'Девайсы'
    
    def __str__(self):
        return self.game_accessories_specification


class ClubImage(models.Model):
    club = models.ForeignKey('clubs.Club', models.CASCADE, related_name='club_image', null=True)
    image = models.FileField('Фото', upload_to = 'club_images')