from django.db import models


class Mobile(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)


    def __str__(self):
        return self.name

class Specification(models.Model):
    mobile_name = models.ForeignKey("Mobile", on_delete=models.CASCADE,)
    ram = models.CharField(max_length=20)
    camera = models.CharField(max_length=50)
    overview = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()    

    # def __str__(self):
    #     self.ram 

    # example of one to many 


# example of one to one relations

class Place(models.Model):
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,on_delete=models.CASCADE
    )    
    serve_pizza = models.CharField(max_length=10)

    def __str__(self):
        return str(self.place)


class Plublication(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=100)
    plublications = models.ManyToManyField(
        Plublication
    )

    def __str__(self):
        return self.headline