from django.db import models

class StudentID(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self):
        return self.student_id

class Student(models.Model):
    student_id = models.OneToOneField(StudentID,related_name='studentid',on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()

    def __str__(self):
        return self.student_name

    # class Meta:
    #     ordering = ['student_name']
        

class Subjects(models.Model):
    subject = models.CharField(max_length=50)

    def __str__(self):
        return self.subject
    
class SubjectsMarks(models.Model):
    student = models.ForeignKey(Student, related_name='studentmark', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student} {self.subject}"

    class Meta:
        unique_together = ['student', 'subject']
    


class ReportCard(models.Model):
    student = models.ForeignKey(Student,related_name='reportcard', on_delete=models.CASCADE)
    student_rank = models.IntegerField()
    report_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['student_rank','report_date']