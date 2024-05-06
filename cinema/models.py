from django.db import models


class Movie(models.Model):
    CHOICES = (
        ('fantasy', 'Фэнтези'),
        ('adventures', 'Приключения'),
        ('action', 'Боевик'),
        ('drama', 'Драма'),
        ('thriller', 'Триллер'),
        ('comedy', 'Комедия'),
    )
    title = models.CharField('Название', max_length=20, blank=False, unique=True)  # Должно быть заполненным
    genre = models.CharField('Жанр', choices=CHOICES, max_length=20, blank=True)  # Может быть пустым
    premiere = models.DateField('Дата премьеры')
    description = models.TextField('Описание фильма', max_length=500, blank=True)
    poster = models.ImageField('Постер', upload_to='posters', blank=True)

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'

    def __str__(self):
        return self.title


class Actor(models.Model):
    first_name = models.CharField('Имя', max_length=20, blank=False)
    last_name = models.CharField('Фамилия', max_length=20, blank=False)
    nickname = models.CharField('Прозвище', max_length=20, blank=True)
    salary = models.DecimalField('Зарплата', max_digits=5, decimal_places=2, blank=True)
    profile_image = models.ImageField('Фото', upload_to='profile_images', blank=True)
    has_oscar = models.BooleanField('Лауреат Оскара', default=False, blank=False)

    class Meta:
        verbose_name = 'актер'
        verbose_name_plural = 'актеры'

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
