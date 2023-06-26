from django.db import models


class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='hotel_media/')
    has_perking = models.BooleanField(default=True)
    has_wifi = models.BooleanField(default=True)
    has_pool = models.IntegerField(choices=((1, 'Да'), (2, 'Нет')), default='Нет')
    stars = models.IntegerField(choices=((1, '1 звезд'), (2, '2 звезд'), (3, '3 звезд'), (4, '4 звезд'), (5, '5 звезд')), default=1)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ApartmentType(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.IntegerField(choices=((1, 'на два человека'), (2, 'на два и более человек'),
                                        (3, 'на четыре и более человек')), default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return self.hotel.name
