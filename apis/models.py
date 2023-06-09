from django.db import models

class gnod(models.Model):
    درجة = models.CharField(max_length=64, verbose_name ="الدرجة")
    اسم = models.CharField(max_length=64, verbose_name ="الإســـــم")
    رقم_عسكرى = models.CharField(max_length=64, primary_key=True, verbose_name="الرقم العسكرى")
    صورة_شخصية = models.ImageField(upload_to ='profiles/gnod', default="../media/profiles/no-profile.png")

    class Meta:
        verbose_name = "جندى"
        verbose_name_plural  = "قوة الجنود "

    def __str__(self):
        return self.اسم
    

class dobat(models.Model):
    رتبة = models.CharField(max_length=64, verbose_name ="الرتبة")
    اسم = models.CharField(max_length=64, verbose_name ="الإســـــم")
    رقم_الأقدمية = models.CharField(max_length=64, primary_key=True, verbose_name="رقم الأقدمية")
    صورة_شخصية = models.ImageField(upload_to ='profiles/dobat', default="../media/profiles/no-profile.png")

    class Meta:
        verbose_name = "ضابط"
        verbose_name_plural  = "قوة الضباط "

    def __str__(self):
        return self.اسم

class dobat_saf(models.Model):
    درجة = models.CharField(max_length=64, verbose_name ="الدرجة")
    اسم = models.CharField(max_length=64, verbose_name ="الإســـــم")
    رقم_عسكرى = models.CharField(max_length=64, primary_key=True, verbose_name="الرقم العسكرى")
    صورة_شخصية = models.ImageField(upload_to ='profiles/dobat_saf', default="../media/profiles/no-profile.png")

    class Meta:
        verbose_name = "ضابط صف"
        verbose_name_plural  = "قوة ضباط الصف "

    def __str__(self):
        return self.اسم
    