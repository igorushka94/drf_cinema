from django.db import models


class City(models.Model):
    """
    Модель Город
    """
    title = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.title


class Cinema(models.Model):
    """
    Модель Кинотеарт
    address - адрес
    """
    city = models.ForeignKey(City, verbose_name='Город', on_delete=models.CASCADE)
    number_phone = models.CharField(max_length=255, verbose_name='Номер телефона')
    address = models.TextField(verbose_name='Адрес кинотеатра')

    class Meta:
        verbose_name = 'Кинотеатр'
        verbose_name_plural = 'Кинотеатры'

    def __str__(self):
        return f'Кинотеатр в городе {self.city.title}'


class Hall(models.Model):
    """
    Модель Зал
    number - номер зала
    count_seats - количество сидений
    """
    cinema = models.ForeignKey(Cinema, verbose_name='Кинотеар', on_delete=models.CASCADE)
    number = models.PositiveIntegerField(verbose_name='Номер зала')
    count_seats = models.PositiveIntegerField(verbose_name='Количество мест')

    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'

    def __str__(self):
        return f'Зал №{self.number}'


class Seat(models.Model):
    """
    Модель Место
    available - авободно или нет
    """
    hall = models.ForeignKey(Hall, verbose_name='Зал', on_delete=models.CASCADE)
    number = models.PositiveIntegerField(verbose_name='Место')
    available = models.BooleanField(verbose_name="Свобдно")

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return f'Место №{self.number}'


class AbstractFilm(models.Model):
    """
    Абстрактная модель Фильма
    title - Название фильма
    description - Описание
    """
    title = models.CharField(max_length=255, verbose_name='Название фильма')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        abstract = True
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Film(AbstractFilm):
    """
    Модель фильм
    duration - длительность фильма
    release_date - год выпуска
    country - страна
    """
    release_date = models.CharField(max_length=255, verbose_name='Год выпуска')
    country = models.CharField(max_length=255, verbose_name='Страна')
    duration = models.CharField(max_length=255, verbose_name='Продолжительность фильма')

    def __str__(self):
        return self.title


class CinemaManager(models.Manager):

    def f(self):
        pass
