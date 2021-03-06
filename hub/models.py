from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User


class Tag(models.Model):
    tag = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.tag

class Tutorial(models.Model):

    DIFFICULTY = (
                ('Beginner', 'Beginner'),
                ('Intermediate', 'Intermediate'),
                ('Advanced', 'Advanced')
    )

    LANGUAGE   = (
                ('Korean', 'Korean'),
                ('English', 'English')
    )

    FORMAT     = (
                ('Video', 'Video'),
                ('Article', 'Article')
    )

    title                     = models.CharField(max_length=150)
    instructor                = models.CharField(max_length=150)
    link                      = models.URLField(max_length=2000)
    last_updated              = models.DateField(max_length=100)
    duration                  = models.CharField(max_length=100)
    description               = models.TextField(max_length=2000)
    thumbnail                 = models.CharField(max_length=500, null=True, blank=True)
    video                     = models.CharField(max_length=500, null=True, blank=True)
    language                  = models.CharField(max_length=100, choices=LANGUAGE)
    difficulty                = models.CharField(max_length=100, choices=DIFFICULTY)
    format                    = models.CharField(max_length=100, choices=FORMAT)
    tags                      = models.ManyToManyField(Tag)

    topic                     = models.CharField(max_length=50, null=True, blank=True) #incase tags doesn't work
    image                     = models.ImageField(null=True, blank=True)
    #likes
    #slug = models.SlugField()

    class Meta:
        ordering              = ('-last_updated',)

    def __str__(self):
        return str(self.title) + ' | ' + str(self.instructor)

    def get_absolute_url(self):
        """returns url from product"""
        return reverse("hub:product", kwargs={  #to the product url (name=product)
            "pk": self.pk
        })

    def get_add_to_curriculum_url(self):
        """returns url to function add item to curriculum in views"""
        return reverse("hub:add-to-curriculum", kwargs={
            "pk": self.pk
        })

    def get_remove_from_curriculum_url(self):
        """returns url to function remove item from curriculum in views"""
        return reverse("hub:remove-from-curriculum", kwargs={
            "pk": self.pk
        })

class Curriculum(models.Model):
    topic                     = models.CharField(max_length=30, null=True, blank=True)
    date_created              = models.DateTimeField(auto_now_add=True, null=True)
    goal                      = models.TextField(max_length=550, null=True, blank=True, default='What are your study goals?')
    note                      = models.CharField(max_length=500, null=True, blank=True)
    user                      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tutorial                  = models.ManyToManyField(Tutorial, blank=True)

    def __str__(self):
        return str(self.user) + ' | ' + str(self.topic)

    # def get_absolute_url(self):
    #     return reverse('curriculum-summary', args=(str(self.id)))


class Profile(models.Model):
    user                      = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    bio                       = models.TextField(max_length=1000)
    profile_pic               = models.ImageField(null=True, blank=True, upload_to="images/profile")
    fb_url                    = models.CharField(max_length=150, null=True, blank=True)
    ig_url                    = models.CharField(max_length=150, null=True, blank=True)
    blog_url                  = models.CharField(max_length=150, null=True, blank=True)
    goal                      = models.TextField(max_length=150, null=True, blank=True, default='What are your study goals?')

    def __str__(self):
        return str(self.user)