from django.db import models

class Questions(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published', null=True, blank=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = "Questions"


class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name_plural = "Choices"
