from django.db import models

# Create your models here.


class Skill(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        db_table = 'Skills'


class SkillHistory(models.Model):
    SOURCES = (
        ('0', 'Unknown'),
        ('1', 'Training'),
        ('2', 'Project experience'),
    )

    skill = models.ForeignKey('Skill')
    employee = models.ForeignKey('sm_employees.Employee')
    source_type = models.CharField(max_length=2)

    class Meta:
        db_table = 'SkillHistory'
