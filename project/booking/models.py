from django.db import models

class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title
    

class MenuItem(models.Model):
    title = models.CharField(max_length=225, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2 , db_index=True)
    featured = models.BooleanField(db_index=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.title


class Reservation(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        constraints  = [
            models.UniqueConstraint(fields=['date', 'time'], name='date and time')]