from faker import Faker
fake = Faker()
import random
from .models import *
from django.db.models import Sum

def create_student_marks(n):
    try:
        student_obj = Student.objects.all()
        for student in student_obj:
            subject_obj = Subjects.objects.all()
            for subject in subject_obj:
                SubjectsMarks.objects.create(
                    student = student,
                    subject = subject,
                    marks = random.randint(25,100)
                )


    except Exception as e:
        print(e)




def seed_db(n=10)-> None:
    try:
        for i in range(0, n):
            student_id = f'STU-{random.randint(100, 999)}'
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(18,30)
            student_address = fake.address()

            student_id_obj = StudentID.objects.create(student_id = student_id)

            Student.objects.create(
                student_id = student_id_obj,
                student_name = student_name,
                student_email = student_email,
                student_age = student_age,
                student_address = student_address
            )

    except Exception as e:
        print(e)


def generate_report_card():
    # current_rank = -1
    ranks = Student.objects.annotate(marks = Sum('studentmark__marks')).order_by('-marks')

    i = 1

    for rank in ranks:
        ReportCard.objects.create(
            student = rank,
            student_rank = i
        )
        i += 1