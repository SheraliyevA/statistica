
from django.db import models

# class Mahsulot(models.Model):
#     nomi = models.CharField(max_length=100)
#     xato_soni = models.IntegerField()

# class Xodim(models.Model):
#     ism = models.CharField(max_length=100)
#     familiya = models.CharField(max_length=100)

    
# class XodimMahsulot(models.Model):
#     xodim = models.ForeignKey(Xodim, related_name='mahsulotlar', on_delete=models.CASCADE)
#     mahsulot = models.ForeignKey(Mahsulot,related_name='mahsulotlar', on_delete=models.CASCADE)

class Ish_turi(models.Model):
    name = models.CharField(max_length=100)
    ish_id = models.CharField(max_length = 5, unique=True)
    def __str__(self):
        return self.name


class Bolim(models.Model):
    name = models.CharField(max_length=100)
    bulim_id = models.CharField(max_length = 5, unique=True)
    user = models.ForeignKey(Ish_turi, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Xodim(models.Model):
    JINS = [
            ('Erkak', 'Erkak'),
            ('Ayol', 'Ayol'),
            ('Null', 'Null'),
        ]
    gender = models.CharField(max_length=6, choices = JINS, null = True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    phone = models.CharField(max_length=13, unique=True)
    ish_turi = models.ManyToManyField(Ish_turi, related_name = 'ish_turi')
    id_raqam = models.CharField(max_length = 5, unique=True)
    bulim= models.ForeignKey(Bolim, on_delete = models.CASCADE, related_name = 'bolim')
    def __str__(self):
        return f'{self.id_raqam}/{self.first_name}/{self.last_name}'
    
class Maxsulot(models.Model):
    name = models.CharField(max_length=255)
    mahsulot_id = models.CharField(max_length = 5, unique=True)

    def __str__(self):
        return self.name


class Problem(models.Model):
    name = models.TextField()
    xato_id = models.CharField(max_length = 5, unique=True)

    def __str__(self):
        return self.name


class Hisobot(models.Model):
    xodim = models.ForeignKey(Xodim, on_delete=models.CASCADE, related_name='xodim')
    xato = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='problem', null=True, blank=True)
    izoh = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    mahsulot = models.ForeignKey(Maxsulot, on_delete=models.CASCADE, related_name = 'maxsulot')
    xato_soni = models.PositiveIntegerField(default=0)
    butun_soni = models.PositiveIntegerField(default=0)
    ish_vaqti = models.PositiveIntegerField(null=True)
    def __str__(self):
        return f'{self.xodim}/{self.xato}/{self.mahsulot}'