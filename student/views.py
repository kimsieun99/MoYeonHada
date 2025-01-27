from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Student, StudentComment
from .forms import StudentForm, StudentCommentForm
from django.urls import reverse

# Create your views here.

def s_main(request):
    students = Student.objects.all()
    
    # 검색 쿼리를 확인합니다.
    query = request.GET.get('q')
    if query:
        # 검색어에 따라 students 쿼리셋을 필터링합니다.
        students = students.filter(title__icontains=query)
        
    content = {'students':students}
    return render(request, 's_main.html', content)


@login_required
def s_c(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            return redirect('s_r', pk=student.pk)
        
    else:
        form = StudentForm()
    content = {'form': form}
    return render(request, 's_c.html', content)



def s_r(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        if request.user.is_authenticated:
            if request.user == student.user:
               student.delete()
               return redirect('s_main')
        return redirect('s_main')
    else:
        scommentform = StudentCommentForm()
        comment = student.StudentComments.all
        content = {'student': student, 'scommentform':scommentform, 'comment':comment}
        return render(request, 's_r.html', content)
    


def s_u(request, pk):
    student = Student.objects.get(pk=pk)
    if request.user != student.user:
        return redirect('s_main')
    if request.user == student.user:
        if request.method == 'POST':
            form = StudentForm(request.POST, request.FILES, instance=student)
            if form.is_valid():
                form.save()
                return redirect('s_r', pk=student.pk)
        else:
            form = StudentForm(instance=student)
        content = {'student': student, 'form': form, }
        return render(request, 's_u.html', content)
    else:
        return redirect('s_main')


@login_required
def s_comment_create(request,pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        scommentform = StudentCommentForm(request.POST)
        if scommentform.is_valid():
            comment = scommentform.save(commit=False)
            comment.student = student
            comment.user = request.user
            comment.save()
        return redirect('s_r', student.pk)


def s_comment_delete(request, comment_pk):
    comment = StudentComment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        student_pk = comment.student_id  # 댓글이 연결된 teacher의 pk 값
        comment.delete()
    return redirect(reverse('s_r', kwargs={'pk': student_pk}))


def student_search(request):
    query = request.GET.get('query')
    search_results = []

    if query:
        search_results = Student.objects.filter(title__icontains=query)

    context = {'search_results': search_results, 'query': query}
    return render(request, 's_main.html', context)