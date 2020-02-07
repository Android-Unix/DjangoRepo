from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length = 20)
    publication = models.DateTimeField()

    def __str__(self):
        return self.question


class Choice(models.Model):
    associatedQuestion = models.ForeignKey(Question , on_delete = models.CASCADE)
    choice_Question = models.TextField()
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return str(self.choice_Question + ' : ' + str(self.votes))
