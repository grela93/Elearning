from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http.response import JsonResponse
from course.models import Major, Subject, Course
from .models import Student, Teacher
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .forms import StudentForm, TeacherForm

# Create your views here.


majors = Major.objects.all()
new_subs = list(reversed(Subject.objects.all()))[:4]
context = {'majors': majors, 'new_subs': new_subs}

def student(request):
    username = ''
    if request.session.has_key('user_id'):
        student = Student.objects.get(student=request.session['user_id'])
        history_courses = list(reversed(student.history_study.all()))[:4]
        new_courses = list(reversed(Course.objects.all()))[:4]
        context['new_courses'] = new_courses
        context['history_courses'] = history_courses            
        context['name'] = student.name
        context['avatar'] = student.avatar.url
        return render(request, 'student/main.html', context)

    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            try:
                student = Student.objects.get(student=user.id)

                history_courses = list(reversed(student.history_study.all()))[:4]
                new_courses = list(reversed(Course.objects.all()))[:4]
                context['new_courses'] = new_courses
                context['history_courses'] = history_courses

                context['name'] = student.name
                context['avatar'] = student.avatar.url

                request.session['user_id'] = user.id
                request.session['student_id'] = student.id
                request.session['name'] = student.name
                request.session['avatar'] = student.avatar.url
                request.session.set_expiry(6000)

                return render(request, 'student/main.html', context)
            except:
                return render(request, 'login/login.html', {'msg': 'Mã hoặc mật khẩu bị nhập sai!'})
        else:
            return render(request, 'login/login.html', {'msg': 'Mã hoặc mật khẩu bị nhập sai!'})
                      
    else:
        return render(request, 'login/login.html', {'msg': ''})

    # Nếu mà dữ liệu gửi lên dưới dạng POST và xác thực được user thi sẽ xuống phần này 
    

def teacher(request):
    username = ''
    if request.session.has_key('user_id'):
        teacher = Teacher.objects.get(teacher=request.session['user_id'])
        courses = teacher.courses.all()

        context['courses'] = courses
        context['name'] = teacher.name
        context['avatar'] = teacher.avatar.url
        return render(request, 'teacher/manage_course.html', context)

    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            try:
                teacher = Teacher.objects.get(teacher_id=user.id)
                courses = teacher.courses.all() # course_set = courses trong related_name='courses'
                print(courses)

                context['courses'] = courses
                context['name'] = teacher.name
                context['avatar'] = teacher.avatar.url

                request.session['user_id'] = user.id
                request.session['teacher_id'] = teacher.id
                request.session['name'] = teacher.name   
                request.session['avatar'] = teacher.avatar.url         
                request.session.set_expiry(1800)
                return render(request, 'teacher/manage_course.html', context)
            except:
                return render(request, 'login/login.html', {'msg': 'Mã hoặc mật khẩu bị nhập sai!'})
        else:
            return render(request, 'login/login.html', {'msg': 'Mã hoặc mật khẩu bị nhập sai!'})
    else:
        return render(request, 'login/login.html', {'msg': ''})

    # Nếu mà dữ liệu gửi lên dưới dạng POST và xác thực được user thi sẽ xuống phần này 
    


def login_view(request):
    if request.session.has_key('user_id'):
        id = request.session['user_id']

        try:
            student = Student.objects.get(student=id)
            context['name'] = student.name
            context['avatar'] = student.avatar.url
            return render(request, 'student/main.html', context)
        except:
            pass   
            
        try:
            teacher = Teacher.objects.get(teacher=id)
            courses = teacher.courses.all()

            context['courses'] = courses
            context['name'] = teacher.name
            context['avatar'] = teacher.avatar.url
            return render(request, 'teacher/manage_course.html', context)
        except:
            pass  
        
    return render(request, 'login/login.html', {'msg': ''})


def logout_view(request):
    try:
        del request.session['name']
        del request.session['avatar']
        del request.session['user_id']
        if request.session['student_id']:
            del request.session['student_id']
        if request.session['teacher_id']:
            del request.session['teacher_id']
    except:
        pass
    return render(request, 'guest/guest.html', context)


@csrf_protect
def view_profile(request):
    if request.session.has_key('user_id'):
        id = request.session['student_id']
        student = Student.objects.get(pk=id)          
        context['name'] = student.name
        context['avatar'] = student.avatar.url
        context['student'] = student
        
        if request.method == 'POST':
            form = StudentForm(request.POST, request.FILES)
            if form.is_valid(): 
                student.avatar = request.FILES['avatar']
                student.name = request.POST['name']
                student.school_year = request.POST['school_year']
                student.gender = request.POST['gender']
                student.phone = request.POST['phone']
                student.email = request.POST['email']
                student.address = request.POST['address']

                student.save()
                context['form'] = form
                return render(request, 'student/profile.html', context)
        else:
            form = StudentForm
            context['form'] = form
        return render(request, 'student/profile.html', context)

    return render(request, 'login/login.html', {'msg': ''})


@csrf_protect
def modify_account(request):
    if request.is_ajax():
        data = request.POST
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')
        usernameNew = data_['username'][0]
        passwordNew = data_['password'][0]
        
        user_id = request.session['user_id']
        student = User.objects.get(pk=user_id)
        student.set_password(passwordNew)
        student.save()

        return JsonResponse({
            'data': data_
        })


def get_infor(request):
    student = Student.objects.get(pk=request.session['student_id'])
    avatar = student.avatar.url
    name = student.name
    school_year = student.school_year
    gender = student.gender
    phone = student.phone
    address = student.address
    email = student.email

    return JsonResponse({
        'avatar': avatar,
        'name': name,
        'school_year': school_year,
        'gender': gender,
        'phone': phone,
        'email': email,
        'address': address,
    })


@csrf_protect
def teacher_view_profile(request):
    if request.session.has_key('user_id'):
        teacher = Teacher.objects.get(pk=request.session['teacher_id'])          
        context['name'] = teacher.name
        context['avatar'] = teacher.avatar.url
        context['teacher'] = teacher
        
        if request.method == 'POST':
            form = TeacherForm(request.POST, request.FILES)
            if form.is_valid(): 
                teacher.avatar = request.FILES['avatar']
                teacher.name = request.POST['name']
                teacher.gender = request.POST['gender']
                teacher.email = request.POST['email']

                teacher.save()
                context['form'] = form
                return render(request, 'teacher/profile.html', context)
        else:
            form = TeacherForm
            context['form'] = form
        return render(request, 'teacher/profile.html', context)

    return render(request, 'login/login.html', {'msg': ''})


def teacher_get_infor(request):
    teacher = Teacher.objects.get(pk=request.session['teacher_id'])
    avatar = teacher.avatar.url
    name = teacher.name
    gender = teacher.gender
    email = teacher.email

    return JsonResponse({
        'avatar': avatar,
        'name': name,
        'gender': gender,
        'email': email,
    })


def teacher_modify_account(request):
    if request.is_ajax():
        data = request.POST
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')
        usernameNew = data_['username'][0]
        passwordNew = data_['password'][0]
        
        user_id = request.session['user_id']
        teacher = User.objects.get(pk=user_id)
        teacher.set_password(passwordNew)
        teacher.save()

        return JsonResponse({
            'data': data_
        })