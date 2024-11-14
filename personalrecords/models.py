from django.db import models
from django.contrib.auth.models import User

class PersonalRecord(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
        related_name='personal_records')
    exercise = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    reps = models.IntegerField()
    date_achieved = models.DateField()
    notes = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ['owner', 'exercise']
        ordering = ['-date_achieved']

    def __str__(self):
        return f"{self.owner.username} - {self.exercise} PR"
