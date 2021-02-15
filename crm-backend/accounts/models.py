from django.db import models



class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name



class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
