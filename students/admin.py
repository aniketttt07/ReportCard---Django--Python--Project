from django.contrib import admin
from .models import StudentID,Student,Subjects,SubjectsMarks,ReportCard
from django.db.models import Sum
# Register your models here.
admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Subjects)

class SubjectsMarksAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'marks']
    list_filter = ('student', 'subject')

admin.site.register(SubjectsMarks,SubjectsMarksAdmin)

@admin.register(ReportCard)
class ReportCardAdmin(admin.ModelAdmin):
    list_display = ['student','student_rank','total_marks', 'report_date']
    ordering = ['student_rank']


    def total_marks(self, obj):
        subject_marks = SubjectsMarks.objects.filter(student = obj.student)
        marks = subject_marks.aggregate(marks = Sum('marks'))
        # print()
        return marks['marks']


