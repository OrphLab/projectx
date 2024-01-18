from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
import shortuuid



class Talent(AbstractUser):
    #talentcard = models.OneToOneField(TalentCard, on_delete=models.CASCADE, null=False, blank=False)
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    profile_slug = models.SlugField(max_length=100, unique=True ,null=True, blank=True)

        
@receiver(pre_save, sender=Talent)
def pre_save_userprofile(sender, instance, **kwargs):
    if not instance.profile_slug:
        instance.profile_slug = shortuuid.uuid()[:20]


        
        
"""

+---------------+          +-----------------+
| AbstractUser  |          |    TalentCard   |
|---------------|          |-----------------|
| talentcard    |<---------| industry        |
| profile_picture|         | origin_country  |
| profile_slug   |         | relocation_countries |
|                |         | open_to_relocation|
+----------------+         | expertice       |
                           | skills          |
                           | linkedin        |
                           | github          |
                           | personal_website|
                           | summary         |
                           +-----------------+
                                  |
                                  | 
                                  V
                        +------------------+
                        |      Country     |
                        |------------------|
                        | country_code     |
                        +------------------+

"""        