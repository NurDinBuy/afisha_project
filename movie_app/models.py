from django.db import models


# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def movie_count(self):
        return self.movie_set.all().count()


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.FloatField()
    director = models.ForeignKey(to=Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def reviews(self):
        review = Review.objects.filter(movie=self)
        return [{'text'} for i in review]

    @property
    def rating(self):
        p = 0

        for i in self.reviews.all():
            p += int(i.stars)
        try:
            ans = p / self.reviews.all().count()
            return ans
        except ZeroDivisionError:
            ans = p / 1
            return ans


CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)


class Review(models.Model):
    text = models.CharField(max_length=255)
    movie = models.ForeignKey(to=Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(default=1, choices=CHOICES, null=True)

    def __str__(self):
        return self.text
