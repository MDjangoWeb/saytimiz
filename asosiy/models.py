from django.db import models

# Create your models here.


class Portfolio(models.Model):
    ish_nomi = models.CharField(max_length=100)
    toifa = models.CharField(max_length=500)
    rasm = models.ImageField(upload_to='rasmlar/portfolio_rasm')
    izox = models.TextField()
    joylashuv_text = models.CharField(max_length=10)
    joylashuv_rasm = models.CharField(max_length=10)

    def __str__(self):
        
        return self.ish_nomi+"__" + self.joylashuv_text

class Mijoz(models.Model):
    ism = models.CharField(max_length=50)
    familya = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    email = models.EmailField()
    telefon = models.CharField(max_length=15)
    rasm = models.ImageField(upload_to='rasmlar/profil_pic')


class MijozFikr(models.Model):
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    fikr = models.TextField()

class Jamoa(models.Model):
    ism = models.CharField(max_length=50)
    familya = models.CharField(max_length=50)
    soha = models.CharField(max_length=50)
    rasm = models.ImageField(upload_to='rasmlar/jamoa_rasm')
    # izox = models.TextField()

    def __str__(self):
       return self.ism


class Maqola(models.Model):
    sarlavha = models.CharField(max_length=100)
    matn = models.TextField()
    rasm = models.ImageField(upload_to='rasmlar/maqola_rasm')

    def __str__(self):
        return self.sarlavha + "id_" +  str(id)

class Aloqa(models.Model):
    ism = models.CharField(max_length=100)
    email = models.EmailField()
    sarlavha = models.CharField(max_length=500)
    matn = models.TextField()


class YangiliklargaYozilish(models.Model):
    e_pochta = models.CharField(max_length=300)


class Murojat(models.Model):
    ism = models.CharField(max_length=100)
    email = models.EmailField()
    mavzu = models.CharField(max_length=100)
    matn = models.TextField()

    def __str__(self):
        return self.ism + " || mavzu:" + self.mavzu