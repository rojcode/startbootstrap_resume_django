from django.db import models


class Awards(models.Model):
    awards = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Awards & Certifications"

    def __str__(self):
        return self.awards


class WorkFlow(models.Model):
    workflow = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.workflow


class Programing_Language(models.Model):
    lang = models.CharField(max_length=250,verbose_name="language or tech")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Programing language or tech"

    def __str__(self):
        return self.lang


class Education(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250,null=True)
    degree = models.CharField(max_length=250,null=True)
    GPA = models.CharField(max_length=12)
    time_line = models.CharField(max_length=250,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{}--{}'.format(self.title,self.GPA)


class Experience(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=300)
    des = models.TextField()
    time_line = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
        verbose_name = "Experience"

    def __str__(self):
        return '{}--{}--{}'.format(self.title,self.subtitle,self.time_line)


# Model for storing user information.
class Profile_cv(models.Model):
    avatar = models.ImageField(upload_to='Uploads/avatar/',blank=True)
    # Basic user information fields.
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    address = models.CharField(max_length=350)
    phone = models.CharField(max_length=250)
    email = models.EmailField()
    des = models.TextField()
    interests = models.TextField(null=True)
    # Social network links
    twitter = models.URLField()
    facebook = models.URLField()
    github = models.URLField()
    linked = models.URLField()
    # Time to build and time to update
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    # Experience
    experience = models.ManyToManyField(Experience,related_name='my_experience',blank=True)

    # Educations
    education = models.ManyToManyField(Education,related_name='my_education')

    # Skills
    lang = models.ManyToManyField(Programing_Language,related_name='my_language_programing',blank=True)
    workflow = models.ManyToManyField(WorkFlow,related_name='my_workflow',blank=True)

    # Awards
    awards = models.ManyToManyField(Awards,related_name='my_awards',blank=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "My profile"

    def __str__(self):
        return '{}--{}'.format(self.first_name,self.phone)


