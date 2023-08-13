from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q,Sum,Count

def table(request):
    
    
    # st = Student.objects.get(student_id__student_id = sid)
    # students = Student.objects.annotate(marks = Sum('studentmark__marks')).order_by('-marks')
    # rank = list(students).index(pk)+1
    # high_mark = Student.objects.filter(studentmark__marks__gt = 90)

    # count_subj_highmarks = high_mark.annotate(subj = Count('studentmark__subject'))

    # print(count_subj_highmarks)

    # student_rank = Student.objects.annotate(marks = Sum('studentmark__marks')).order_by('-marks')
    
    
  
    # for s in students:
    #     print(f"{s.student_name} : {s.marks}")
    # else:
    #     print('end')
    students = Student.objects.all()



    if request.GET.get('search'):
        students = Student.objects.filter(
            Q(student_name__icontains = request.GET.get('search')) |
            Q(student_email__icontains = request.GET.get('search')) |
            Q(student_id__student_id__icontains = request.GET.get('search')) |
            Q(student_age__icontains = request.GET.get('search')) |
            Q(student_address__icontains = request.GET.get('search'))
        
        
        )


    paginator = Paginator(students, 10)  # Show 10 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    starting_rank = (page_obj.number - 1) * paginator.per_page + 1
    for student in page_obj:
        student.rank = starting_rank
        starting_rank += 1

    context = {
        'students':page_obj,
        # 'strank':strank
    }
    return render(request,'table.html',context)

# from .seed import generate_report_card

def seemarks(request,sid):
    # generate_report_card()
    # st = Student.objects.get(student_id__student_id = sid)
    queryset = SubjectsMarks.objects.filter(student__student_id__student_id = sid)
    total = queryset.aggregate(total = Sum('marks'))
    students = Student.objects.annotate(marks = Sum('studentmark__marks')).order_by('-marks')

    # student_rank = list(students).index(st) + 1
    context = {
        # 'st':st,
        'queryset':queryset,
        'total':total,
        # 'student_rank':student_rank
    }
    return render(request, 'marks_detail.html', context)



