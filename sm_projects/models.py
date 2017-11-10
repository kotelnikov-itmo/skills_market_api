from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        db_table = 'Projects'


class Assignment(models.Model):
    project = models.ForeignKey('Project')
    employee = models.ForeignKey('sm_employees.Employee', null=True, blank=True)
    description = models.TextField()
    position = models.ForeignKey('sm_employees.Position')
    start_date = models.DateField()
    end_date = models.DateField()
    need_skills = models.ManyToManyField("sm_skills.Skill", db_table='AssignmentsSkills')

    class Meta:
        db_table = 'ProjectAssignments'
