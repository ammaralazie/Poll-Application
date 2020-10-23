from django.db import models

class Poll(models.Model):
    question=models.TextField(verbose_name="Question")
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option1_count=models.IntegerField(default=0)
    option2_count=models.IntegerField(default=0)
    option3_count=models.IntegerField(default=0)
    
    @property
    def total(self):
        sum =self.option1_count+self.option2_count+self.option3_count
        return sum