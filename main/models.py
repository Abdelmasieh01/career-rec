from django.db import models

class Cretificate(models.Model):
    name = models.CharField(max_length=150, verbose_name='الجهة المقدم منها الشهادة')
    date = models.DateField(verbose_name='تاريخ الشهادة')
    text = models.CharField(max_length=1000, verbose_name='نص الشهادة')

    def __str__(self):
        return self.name + ' ' + str(self.date)

class Acheivement(models.Model):
    name = models.CharField(max_length=150, verbose_name='اسم الإنجاز')
    date = models.DateField(verbose_name='تاريخ الإنجاز')
    text = models.CharField(max_length=1000, verbose_name='نص الإنجاز')

    def __str__(self):
        return self.name + ' ' + str(self.date)

class Workshop(models.Model):
    name = models.CharField(max_length=150, verbose_name='اسم الورشة')
    text = models.CharField(max_length=1000, verbose_name='تفاصيل عن الورشة', blank=True)

    def __str__(self):
        return self.name

class Visit(models.Model):
    name = models.CharField(max_length=150, verbose_name='اسم الزيارة')
    date = models.DateField(verbose_name='تاريخ الزيارة')
    text = models.CharField(max_length=1000, verbose_name='تفاصيل عن الزيارة', blank=True)

    def __str__(self):
        return self.name + ' ' + str(self.date)

class Medical(models.Model):
    name = models.CharField(max_length=150, verbose_name='اسم الخطة العلاجية')
    date = models.DateField(verbose_name='تاريخ الخطة العلاجية')
    text = models.CharField(max_length=1000, verbose_name='تفاصيل عن الخطة العلاجية', blank=True)

    def __str__(self):
        return self.name + ' ' + str(self.date)