from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField(auto_now_add=True, blank=True)
    end_date = models.DateField(null=True)

    class Meta:
        db_table = 'Projects'

    def __str__(self):
        return self.name


class Assignment(models.Model):
    project = models.ForeignKey('Project')
    employee = models.ForeignKey('sm_employees.Employee', null=True, blank=True)
    description = models.TextField()
    position = models.ForeignKey('sm_employees.Position')
    start_date = models.DateField(auto_now_add=True, blank=True)
    # end_date = models.DateField()
    need_skills = models.ManyToManyField("sm_skills.Skill", db_table='AssignmentsSkills')

    class Meta:
        db_table = 'ProjectAssignments'

    def __str__(self):
        return "{}: {}".format(self.project.name, self.id)

