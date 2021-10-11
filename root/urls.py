"""root URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings
from course.views import cmt_json, course_detail, course_list, history_courses, history_quizzes, save_cmt, save_student_course, search, subject_list, teacher_add_course, teacher_del_course, teacher_get_course_json, teacher_manage_course, teacher_modify_course, teacher_view_course
from quiz.views import get_list_score, question_bydocx_data, quiz_data, quiz_detail, quizzes_json, save_quiz, show_quizzes, subject_quizzes, teacher_add_question_bydocx, teacher_add_question_form, teacher_add_quiz, teacher_delete_quiz, teacher_get_quiz_data, teacher_get_subject, teacher_manage_score, teacher_save_question_form, teacher_save_quiz
from user.views import get_infor, login_view, logout_view, modify_account, student, teacher, teacher_get_infor, teacher_modify_account, teacher_view_profile, view_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('student/', include([
        path('', student, name='student_home'),
        path('search/', search, name='search'),
        path('major/<int:id>', subject_list, name='subject_list'),
        path('subject/<int:id>', course_list, name='course_list'),
        path('course/<int:id>', course_detail, name='course_detail'),
        path('course/<int:id>/save', save_student_course, name='save_student_course'),
        path('course/<int:id>/cmt', cmt_json, name='cmt_json'),
        path('course/<int:id>/save-cmt', save_cmt, name='save_cmt'),
        path('subject-quiz', subject_quizzes, name='subject_quizzes'),
        path('subject-quiz/<int:id>', show_quizzes, name='quizzes'),
        path('quiz/<int:id>', quiz_detail, name='quiz_detail'),
        path('quiz/<int:id>/data', quiz_data, name='quiz_data'),
        path('quiz/<int:id>/save', save_quiz, name='save_quiz'),
        path('history-course/', history_courses, name='history_courses'),
        path('history-quizzes/', history_quizzes, name='history_quizzes'),
        path('profile/', view_profile, name='view_profile'),
        path('profile/modify-account', modify_account, name='modify_account'),
        path('profile/get-infor', get_infor, name='get_infor'),

    ])),

    path('teacher/', include([
        path('', teacher, name='teacher_home'),
        path('manage-course/', teacher_manage_course, name="manage_course"),
        path('add-course/', teacher_add_course, name="add_course"),
        path('view-course/<int:id>', teacher_view_course, name="view_course"),
        path('view-course/<int:id>/cmt', cmt_json, name='cmt_json'),
        path('view-course/<int:id>/save-cmt', save_cmt, name='save_cmt'),
        path('modify-course/<int:id>', teacher_modify_course, name="modify_course"),
        path('modify-course/<int:id>/get-course', teacher_get_course_json, name="get_course_json"),
        path('delete-course/<int:id>', teacher_del_course, name="del_course"),
        path('manage-quiz/', teacher_get_subject, name="subject_quiz"),
        path('manage-quiz/<int:id>/data', quizzes_json, name="quizzes_json"),
        path('add-quiz/<int:id>/', teacher_add_quiz, name="add_quiz"),
        path('add-quiz/<int:id>/save', teacher_save_quiz, name="save_quiz"),
        path('add-question-form/<int:id>', teacher_add_question_form, name="add_question_manual"),
        path('add-question-form/<int:id>/save', teacher_save_question_form, name="save_question_manual"),
        path('add-question-bydocx/<int:id>', teacher_add_question_bydocx, name="add_question_bydocx"),
        path('add-question-bydocx/<int:id>/data', question_bydocx_data, name="get_question_bydocx"),
        path('delete-quiz/<int:id>/', teacher_delete_quiz, name="delete_quiz"),
        path('manage-score/', teacher_manage_score, name='manage_score'),
        path('manage-score/<int:id>/data', teacher_get_quiz_data, name='manage_score'),
        path('view-score/<int:id>', get_list_score, name="view_score"),
        path('profile/', teacher_view_profile, name="teacher_profile"),
        path('profile/get-infor', teacher_get_infor),
        path('profile/modify-account', teacher_modify_account),
    ])),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)