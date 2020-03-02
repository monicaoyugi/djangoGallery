from django.db import models

class Location(models.Model):
    place = models.CharField(max_length=255)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.place


class Category(models.Model):
    name = models.CharField(max_length=255)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='images/',null=True)
    image_name = models.CharField(max_length=255)
    image_description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def save_Image(self):
        self.save()

    def delete_Image(self):
        self.delete()

    @classmethod
    def display_all_images(cls):
        all_images = cls.objects.all()
        return all_images

    @classmethod
    def search_by_category(cls, category):
        images = cls.objects.filter(category__name =category)
        return images

    @classmethod
    def get_image_by_id(cls, id):
        return cls.objects.filter(id=id)


    @classmethod
    def filter_by_location(cls, location):
        image_location = Image.objects.filter(location__name=location).all()
        return image_location

    @classmethod
    def search_by_title(cls, search_term):
        news = cls.objects.filter(name__icontains=search_term)
        return news
        
    class Meta:
        ordering = ['image_name']