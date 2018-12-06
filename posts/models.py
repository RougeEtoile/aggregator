from django.db import models

# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=30)
    twitterID = models.CharField(max_length=30, blank=True)
    instaID = models.CharField(max_length=30, blank=True)
    def __str__(self):
        return "{}\ntwitter:{}\nInstagram:{}".format(self.username ,self.twitterID, self.instaID)

class twitterPost(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    text = models.CharField(max_length=500, blank=True)
    created_at = models.IntegerField(default=0)
    def __str__(self):
        return "{}\n{}".format(self.text, self.created_at)

class instaPost(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    text = models.CharField(max_length=500, blank=True)
    created_at = models.IntegerField(default=0)
    def __str__(self):
        return "{}\n{}".format(self.text, self.created_at)

class selfPost(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    text = models.CharField(max_length=500, blank=True)
    created_at = models.IntegerField(default=0)
    def __str__(self):
        return "{}\n{}".format(self.text, self.created_at)
