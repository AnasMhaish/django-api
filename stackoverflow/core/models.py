from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s: %s' % (self.username, self.email)

class Question(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    authorId = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)   

    def __str__(self):
        return '%s: %s' % (self.title, self.body)        

class Answer(models.Model):
    questionId = models.ForeignKey(Question, on_delete=models.CASCADE)
    authorId = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    score = models.PositiveSmallIntegerField()  
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Answer: %s' % (self.body)  