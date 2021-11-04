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
    number_phone = models.CharField('Номер телефона', max_length=255)
    address = models.TextField('Адрес кинотеатра')

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
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, verbose_name='Кинотеар')
    number = models.PositiveIntegerField('Номер зала')
    count_seats = models.PositiveIntegerField('Количество мест')

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
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, verbose_name='Зал',)
    number = models.PositiveIntegerField('Место')
    available = models.BooleanField("Свобдно")

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
    title = models.CharField('Название фильма', max_length=255)
    description = models.TextField('Описание')

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
    release_date = models.CharField('Год выпуска', max_length=255)
    country = models.CharField('Страна', max_length=255)
    duration = models.CharField('Продолжительность фильма', max_length=255)

    def __str__(self):
        return self.title


class CinemaManager(models.Manager):

    def f(self):
        pass
