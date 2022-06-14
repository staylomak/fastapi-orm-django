from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Campaign(models.Model):
    campaign_code = models.IntegerField(null=True)
    name = models.CharField(unique=True, db_index=True, max_length=150)
    AS400Promotion = models.IntegerField(default=9998)
    days = models.CharField(max_length=7, default='1111111')
    type = models.IntegerField(default=99)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    is_valid = models.BooleanField(default=False)
    priority = models.PositiveSmallIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)