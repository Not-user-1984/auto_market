from django.db import models


class Mark(models.Model):
    """
    Модель для хранения информации о марках автомобилей.
    """
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Model(models.Model):
    """
    Модель для хранения информации о моделях автомобилей.
    """
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    generation = models.IntegerField()
    modification_name = models.CharField(max_length=100)
    modification_id = models.IntegerField()
    configuration_id = models.IntegerField()
    tech_param_id = models.IntegerField()
    body_type = models.CharField(max_length=100)
    years = models.CharField(max_length=100)
    complectations = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.mark.name} - {self.name} ({self.modification_name})"
