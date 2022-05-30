from django.db import models

# Create your models here.

GENDERS = [
    ('M', 'Male'),
    ('F', 'Female'),
]


class Student(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    middle_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    gender = models.CharField(max_length=255, null=False, blank=False)
    contact_number = models.CharField(max_length=15)
    address = models.TextField(blank=False, null=False)
    admit_date = models.DateField(blank=False, null=False)
    course = models.CharField(max_length=255, null=False, blank=False)
    year = models.PositiveSmallIntegerField(null=False, blank=False)
    section = models.PositiveSmallIntegerField(null=False, blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} of {self.course_section}"

    @property
    def course_section(self):
        return f"{self.course} {self.year}-{self.section}"
