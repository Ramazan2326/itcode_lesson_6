# itcode_lesson_6
1) models.Actor.objects.all()
<QuerySet [<Actor: Смит Уилл>, <Actor: Депп Джонни>, <Actor: Круз Пенелопа>, <Actor: Альба Идрис>, <Actor: Добронравов Федор>, <Actor: Хабенский Константин>, <Actor: Джоли Анджелина>, <Actor: Йоханссон Скарлетт>, <Actor: Безруков Сергей>]>
2) models.Movie.objects.all()
<QuerySet [<Movie: Пираты К. Моря>, <Movie: Кремниевая Долина>, <Movie: Ламборгини>, <Movie: Кунг-Фу Панда>, <Movie: Звездные воины>, <Movie: Чемпион мира>]>
3) models.Actor.objects.first()
<Actor: Смит Уилл>
4) models.Actor.objects.last()
<Actor: Безруков Сергей>
5) models.Movie.objects.first()
<Movie: Пираты К. Моря>
6) models.Movie.objects.last()
<Movie: Чемпион мира>
7) models.Actor.objects.filter(has_oscar=True).all()
<QuerySet [<Actor: Смит Уилл>, <Actor: Депп Джонни>]>
8) models.Movie.objects.filter(genre="fantasy").all()
<QuerySet [<Movie: Пираты К. Моря>]>
9) models.Actor.objects.exclude(has_oscar=True).all()
<QuerySet [<Actor: Круз Пенелопа>, <Actor: Альба Идрис>, <Actor: Добронравов Федор>, <Actor: Хабенский Константин>, <Actor: Джоли Анджелина>, <Actor: Йоханссон Скарлетт>, <Actor: Безруков Сергей>]>
10) models.Movie.objects.exclude(genre="drama").all()
<QuerySet [<Movie: Пираты К. Моря>, <Movie: Кремниевая Долина>, <Movie: Кунг-Фу Панда>, <Movie: Звездные воины>]>
11) models.Actor.objects.order_by("salary").all()
<QuerySet [<Actor: Альба Идрис>, <Actor: Круз Пенелопа>, <Actor: Депп Джонни>, <Actor: Добронравов Федор>, <Actor: Йоханссон Скарлетт>, <Actor: Смит Уилл>, <Actor: Хабенский Константин>, <Actor: Безруков Сергей>, <Actor: Джоли Анджелина>]>
12) models.Movie.objects.order_by("premiere").all()
<QuerySet [<Movie: Пираты К. Моря>, <Movie: Звездные воины>, <Movie: Кунг-Фу Панда>, <Movie: Кремниевая Долина>, <Movie: Чемпион мира>, <Movie: Ламборгини>]>
13) models.Actor.objects.exclude(has_oscar=False).order_by("first_name").all()
<QuerySet [<Actor: Депп Джонни>, <Actor: Смит Уилл>]>
14) models.Actor.objects.filter(salary__gt = 500).all()
<QuerySet [<Actor: Смит Уилл>, <Actor: Добронравов Федор>, <Actor: Хабенский Константин>, <Actor: Джоли Анджелина>, <Actor: Йоханссон Скарлетт>, <Actor: Безруков Сергей>]>
15) models.Actor.objects.filter(salary__lte = 500).all()
<QuerySet [<Actor: Депп Джонни>, <Actor: Круз Пенелопа>, <Actor: Альба Идрис>]>
16) models.Movie.objects.filter(premiere__year__lt = 2008).all()
<QuerySet [<Movie: Пираты К. Моря>, <Movie: Звездные воины>]>
17) models.Movie.objects.filter(premiere__day__gte = 15).all()
<QuerySet [<Movie: Пираты К. Моря>, <Movie: Ламборгини>, <Movie: Чемпион мира>]>
18) models.Movie.objects.filter(premiere__month__lte = 10).all()
<QuerySet [<Movie: Пираты К. Моря>, <Movie: Кремниевая Долина>, <Movie: Кунг-Фу Панда>, <Movie: Звездные воины>]>
19) models.Actor.objects.filter(first_name__contains="а")
<QuerySet [<Actor: Круз Пенелопа>, <Actor: Хабенский Константин>, <Actor: Джоли Анджелина>, <Actor: Йоханссон Скарлетт>]>
20) models.Movie.objects.filter(title__contains="Л")
<QuerySet [<Movie: Ламборгини>]>
21) models.Movie.objects.filter(title__contains="а").count()
5
22) models.Movie.objects.filter(title__contains="а").exclude(genre="drama").count()
3
23) models.Movie.objects.filter(title="Ламборгини").exists()
True
24) models.Movie.objects.filter(title="Феррари").exists()
False
25) models.Actor.objects.filter(salary__gt = 200).exists()
True