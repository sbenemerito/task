from django.db import models
from django.db.models import Q


class ModelA(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ModelB(models.Model):
    name = models.CharField(max_length=50)
    related_a = models.ForeignKey(ModelA, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ModelC(models.Model):
    name = models.CharField(max_length=50)
    related_a = models.ForeignKey(ModelA, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MainModel(models.Model):
    name = models.CharField(max_length=50)
    model_a = models.ManyToManyField(ModelA, blank=True)
    model_b = models.ManyToManyField(ModelB, blank=True)
    model_c = models.ManyToManyField(ModelC, blank=True)

    def __str__(self):
        return self.name