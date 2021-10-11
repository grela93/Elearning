from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponseRedirect
from rest_framework.decorators import api_view
from .models import Major, StudentCourse, Subject, Course, Comment
from user.models import Student, Teacher
from quiz.models import Quiz
from .forms import CourseForm
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import datetime


# Create your views here.

majors = Major.objects.all()
context = {'majors': majors}

# @decorators.login_required(login_url='/home/')
@api_view(['GET'])
def subject_list(request, id):
    if request.session.has_key('user_id'):
        name = request.session['name']
        context['name'] = name
        context['avatar'] = request.session['avatar']

        major_name = Major.objects.get(pk=id)
        context['major_name'] = major_name

        subjects = Subject.objects.filter(major__exact=id)
        context['subjects'] = subjects
        return render(request, 'student/subjects.html', context)
    
    return render(request, 'login/login.html', {'msg': ''})


# @decorators.login_required(login_url='/home/')
@api_view(['GET'])
def course_list(request, id):
    if request.session.has_key('user_id'):
        name = request.session['name']
        context['name'] = name
        context['avatar'] = request.session['avatar']
        
        sub_name = Subject.objects.get(pk=id) # Ten mon hoc
        context['sub_name'] = sub_name

        subjects = Subject.objects.filter(major__exact=sub_name.major) # Cac mon hoc khac cung nganh
        context['subjects'] = subjects

        courses = Course.objects.filter(subject__exact=id) # Cac bai hoc trong cung 1 mon
        context['courses'] = courses
        return render(request, 'student/courses.html', context)

    return render(request, 'login/login.html', {'msg': ''})
    

def search(request):
    if request.session.has_key('user_id'):
        name = request.session['name']
        context['name'] = name
        context['avatar'] = request.session['avatar']

        if request.method == 'POST':
            search = request.POST['searchCourse']
            subjects = Subject.objects.filter(name__contains=search)
            context['subjects'] = subjects

            courses = Course.objects.filter(name__contains=search)
            context['courses'] = courses

            quizzes = Quiz.objects.filter(name__contains=search)
            context['quizzes'] = quizzes

            return render(request, 'student/search.html', context)
        else:
            subjects = Subject.objects.all()
            context['subjects'] = subjects

            courses = Course.objects.all()
            context['courses'] = courses

            quizzes = Quiz.objects.all()
            context['quizzes'] = quizzes

            return render(request, 'student/search.html', context)

    return render(request, 'login/login.html', {'msg': ''})


@api_view(['GET', 'POST'])
def course_detail(request, id):
    if request.session.has_key('user_id'):
        name = request.session['name']
        context['name'] = name
        context['avatar'] = request.session['avatar']

        student = Student.objects.get(name__iexact=name)
        course = Course.objects.get(pk=id)
        context['course'] = course

        if request.method == "POST":
            body = request.POST['body']
            cmt = Comment(student=student, course=course, body=body)
            cmt.save()
            return HttpResponseRedirect(request.path)

        return render(request, 'student/course_detail.html', context)

    return render(request, 'login/login.html', {'msg': ''})


def save_student_course(request, id):
    if request.is_ajax():
        data = dict(request.POST.lists())

        data.pop('csrfmiddlewaretoken')

        student = Student.objects.get(pk=request.session['student_id'])
        course = Course.objects.get(pk=id)
        StudentCourse.objects.get_or_create(student=student, course=course)

        return JsonResponse(data)


def history_courses(request):
    if request.session.has_key('user_id'):
        name = request.session['name']
        context['name'] = name
        context['avatar'] = request.session['avatar']

        student = Student.objects.get(name__iexact=name)
        history_courses = student.history_study.all()
        context['history_courses'] = history_courses

        return render(request, 'student/history_course.html', context)

    return render(request, 'login/login.html', {'msg': ''})


def history_quizzes(request):
    if request.session.has_key('user_id'):
        name = request.session['name']
        context['name'] = name
        context['avatar'] = request.session['avatar']

        student = Student.objects.get(name__iexact=name)
        history_quizzes = student.quiz_result.all()
        context['history_quizzes'] = history_quizzes

        return render(request, 'student/history_quizzes.html', context)

    return render(request, 'login/login.html', {'msg': ''})


contextTeacher = {}
def teacher_manage_course(request):
    if request.session.has_key('user_id'):
        teacher = Teacher.objects.get(pk=request.session['teacher_id'])
        courses = teacher.courses.all()

        contextTeacher['courses'] = courses
        contextTeacher['name'] = teacher.name
        contextTeacher['avatar'] = teacher.avatar.url
        
        return render(request, 'teacher/manage_course.html', contextTeacher)

    return render(request, 'login/login.html', {'msg': ''})


def teacher_get_course_json(request, id):
    course = Course.objects.get(pk=id)
    name = course.name
    description = course.description
    body = course.body
    return JsonResponse({
        'name': name,
        'description': description,
        'body': body
    })

@csrf_protect
def teacher_add_course(request):
    if request.session.has_key('user_id'):
        teacher = Teacher.objects.get(pk=request.session['teacher_id'])
        
        contextTeacher['name'] = teacher.name
        contextTeacher['avatar'] = teacher.avatar.url

        if request.method == 'POST':
            form = CourseForm(request.POST, request.FILES)
            if form.is_valid():
                subject = Subject.objects.get(pk=request.POST['subject'])
                name = request.POST['name']
                description = request.POST['description']
                body = request.POST['body']
                if request.FILES.get('pdf'):
                    pdf = request.FILES.get('pdf')
                else:
                    pdf = ''
                if request.FILES.get('video'):
                    video = request.FILES.get('video')
                else:
                    video = ''

                Course.objects.create(subject=subject, teacher=teacher, name=name, description=description, body=body, pdf=pdf,video=video)

                contextTeacher['form'] = form
                return render(request, 'teacher/add_course.html', contextTeacher)
        else:
            form = CourseForm
            contextTeacher['form'] = form
        return render(request, 'teacher/add_course.html', contextTeacher)
        

    return render(request, 'login/login.html', {'msg': ''})


@csrf_protect
def teacher_modify_course(request, id):
    if request.session.has_key('user_id'):
        teacher = Teacher.objects.get(pk=request.session['teacher_id'])
        course = Course.objects.get(pk=id)
        contextTeacher['course_id'] = id
        
        contextTeacher['name'] = teacher.name
        contextTeacher['avatar'] = teacher.avatar.url

        if request.method == 'POST':
            form = CourseForm(request.POST, request.FILES)
            print('post')
            # subject = Subject.objects.get(pk=request.POST['subject'])
            course.name = request.POST['name']
            course.description = request.POST['description']
            course.body = request.POST['body']
            if request.FILES.get('pdf'):
                course.pdf = request.FILES.get('pdf')
            if request.FILES.get('video'):
                course.video = request.FILES.get('video')
            course.save()

            contextTeacher['form'] = form
            return HttpResponseRedirect(request.path)
        else:
            form = CourseForm
            contextTeacher['form'] = form
        return render(request, 'teacher/modify_course.html', contextTeacher)

    return render(request, 'login/login.html', {'msg': ''})


def teacher_del_course(request, id):
    if request.session.has_key('user_id'):
        teacher = Teacher.objects.get(pk=request.session['teacher_id'])
        courses = teacher.courses.all()

        contextTeacher['courses'] = courses
        contextTeacher['name'] = teacher.name
        contextTeacher['avatar'] = teacher.avatar.url

        course = Course.objects.get(pk=id)
        course.delete()
        
        return render(request, 'teacher/manage_course.html', contextTeacher)

    return render(request, 'login/login.html', {'msg': ''})


def teacher_view_course(request, id):
    if request.session.has_key('user_id'):
        teacher = Teacher.objects.get(pk=request.session['teacher_id'])
        course = Course.objects.get(pk=id)

        contextTeacher['course'] = course
        contextTeacher['name'] = teacher.name
        contextTeacher['avatar'] = teacher.avatar.url

        return render(request, 'teacher/view_course.html', contextTeacher)

    return render(request, 'login/login.html', {'msg': ''})
    

def cmt_json(request, id):
    cmt = Comment.objects.filter(course=id)
    cmt_ = list(cmt.values())
    cmts = []
    for c in cmt_:
        comment = {}
        if c['student_id']:
            student = Student.objects.get(pk=c['student_id'])
            comment['student_name'] = student.name
        else:
            teacher = Teacher.objects.get(pk=c['teacher_id'])
            comment['teacher_name'] = teacher.name

        comment['body'] = c['body']
        comment['created_at'] = (c['created_at']).strftime('%Y/%m/%d %H:%M:%S')
        cmts.append(comment)
    
    return JsonResponse(cmts, safe=False)


def save_cmt(request, id):
    if request.is_ajax():
        data = request.POST
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')
        body = data_['body'][0]

        if body != '':
            try:
                student = Student.objects.get(pk=request.session['student_id'])
                course = Course.objects.get(pk=id)

                Comment.objects.create(student=student, course=course, body=body)

                return JsonResponse({
                    'studentName': student.name,
                    'body': body,
                    'time': datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
                })
            except:
                pass

            try:
                teacher = Teacher.objects.get(pk=request.session['teacher_id'])
                course = Course.objects.get(pk=id)

                Comment.objects.create(teacher=teacher, course=course, body=body)

                return JsonResponse({
                    'teacherName': teacher.name,
                    'body': body,
                    'time': datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
                })
            except:
                pass
        
        else:
             return JsonResponse({
                'studentName': '',
                'body': body,
                'time': datetime.datetime.now().strftime('%Y/%M/%d %H:%M:%S')
            })