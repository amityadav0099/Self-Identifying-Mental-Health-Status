from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    text = models.CharField(max_length=255)

    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)

    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=1)
    score3 = models.IntegerField(default=2)
    score4 = models.IntegerField(default=3)

    def __str__(self):
        return self.text


class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_score = models.IntegerField()
    category = models.CharField(max_length=50)
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
