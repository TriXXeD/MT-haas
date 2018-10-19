from django.db import models


class Plant(models.Model):
    name = models.CharField(max_length=50)
    humidity = models.FloatField()
    humid_min = models.FloatField()
    last_watered = models.DateTimeField()

    def __str__(self):
        return self.name

    def needs_water(self):
        if self.humidity < self.humid_min:
            return True
        return False


class LightGroup(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class LightBulb(models.Model):
    belongs_to_group = models.ForeignKey(LightGroup, on_delete=models.CASCADE)
    intensity = models.IntegerField(default=0)

    def __str__(self):
        return 'bulb in: ' + self.belongs_to_group.name
