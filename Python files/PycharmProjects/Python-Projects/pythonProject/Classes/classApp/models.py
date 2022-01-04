from django.db import models
# import models from django database

#creating a model class called djangoClasses
class djangoClasses(models.Model):
    # adding the attributes to the djangoClasses model
    Title = models.CharField(max_length=60, default="", blank=True, null=False)
    CourseNumber = models.IntegerField(blank=True, null=False)
    InstructorName = models.CharField(max_length=60, default="", blank=True, null=False)
    Duration = models.FloatField(blank = True, null=False)

    objects = models.Manager()

    # When open database the object is shown by its title
    def __str__(self):
        return self.Title


# Create your models here.
