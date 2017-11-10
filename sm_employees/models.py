from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    is_active = models.BooleanField()
    recruited_date = models.DateField()
    positions = models.ManyToManyField('Position', through='PositionHistory')
    skills = models.ManyToManyField('sm_skills.Skill', through='sm_skills.SkillHistory')

    class Meta:
        db_table = 'Employees'


class Position(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'Positions'


class PositionHistory(models.Model):
    employee_id = models.ForeignKey('Employee')
    position_id = models.ForeignKey('Position')
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        db_table = 'PositionHistory'
