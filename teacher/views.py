from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Teacher, TeacherComment
from .forms import TeacherForm, TeacherCommentForm
from django.urls import reverse

# Create your views here.

def t_main(request):
    teachers = Teacher.objects.all()
    
    # 검색 쿼리를 확인합니다.
    query = request.GET.get('q')
    if query:
        # 검색어에 따라 teachers 쿼리셋을 필터링합니다.
        teachers = teachers.filter(title__icontains=query)
        
    content = {'teachers':teachers}
    return render(request, 't_main.html', content)


@login_required
def t_c(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.user = request.user
            teacher.save()
            return redirect('t_r', pk=teacher.pk)
        
    else:
        form = TeacherForm()
    content = {'form': form}
    return render(request, 't_c.html', content)



def t_r(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    if request.method == 'POST':
        if request.user.is_authenticated:
            if request.user == teacher.user:
               teacher.delete()
               return redirect('t_main')
        return redirect('t_main')
    else:
        commentform = TeacherCommentForm()
        comment = teacher.TeacherComments.all
        content = {'teacher': teacher, 'commentform':commentform, 'comment':comment}
        return render(request, 't_r.html', content)
    


def t_u(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    if request.user != teacher.user:
        return redirect('t_main')
    if request.user == teacher.user:
        if request.method == 'POST':
            form = TeacherForm(request.POST, request.FILES, instance=teacher)
            if form.is_valid():
                form.save()
                return redirect('t_r', pk=teacher.pk)
        else:
            form = TeacherForm(instance=teacher)
        content = {'teacher': teacher, 'form': form, }
        return render(request, 't_u.html', content)
    else:
        return redirect('t_main')


@login_required
def t_comment_create(request,pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        commentform = TeacherCommentForm(request.POST)
        if commentform.is_valid():
            comment = commentform.save(commit=False)
            comment.teacher = teacher
            comment.user = request.user
            comment.save()
        return redirect('t_r', teacher.pk)


def t_comment_delete(request, comment_pk):
    comment = TeacherComment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        teacher_pk = comment.teacher_id  # 댓글이 연결된 teacher의 pk 값
        comment.delete()
    return redirect(reverse('t_r', kwargs={'pk': teacher_pk}))


from django.contrib import messages
from django.db.models import Q

def teacher_search(request):
    query = request.GET.get('query')
    search_results = []

    if query:
        search_results = Teacher.objects.filter(title__icontains=query)

    context = {'search_results': search_results, 'query': query}
    return render(request, 't_main.html', context)