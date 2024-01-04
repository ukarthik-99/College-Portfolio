from django.shortcuts import render

from schoolApp.forms import studentmodelform

from schoolApp.forms import teachermodelform

from schoolApp.models import schoolApp

from schoolApp.models import Teacher1

from django.contrib.auth.decorators import login_required ,permission_required






# Create your views here.
@login_required
@permission_required('project.view_schoolApp')
def homepage(request):
    return render(request,'home.html')

def logout(request):
    return render(request,'LOGOUT.html')


@login_required
@permission_required('project.add_schoolApp')
def admis(request):
    form=studentmodelform
    studentform={'form':form}
    if request.method=='POST':
        form=studentmodelform(request.POST)
        if form.is_valid():
            form.save()
        return  homepage(request)
    return render(request,'school/admis.html',studentform)


@login_required
@permission_required('project.delete_schoolApp')
def deletestudent(request,id):
    s=schoolApp.objects.get(id=id)
    s.delete()
    return admis_report(request)

@login_required
@permission_required('project.change_schoolApp')
def updatestudent(request,id):

    s=schoolApp.objects.get(id=id)
    form=studentmodelform(instance=s)
    dict={'form':form}
    if request.method=='POST':
        form=studentmodelform(request.POST,instance=s)
        if form.is_valid():
            form.save()
        return admis_report(request)
    return render(request,'update.html',dict)


@login_required
@permission_required('project.view_schoolApp')
def admis_report(request):
    result=schoolApp.objects.all()
    student={'allresult':result}
    return render(request,'school/admis_report.html',student)
    

@login_required
@permission_required('project.add_Teacher1')
def Teacher(request):
    form=teachermodelform
    teacherform={'form':form}
    if request.method=='POST':
        form=teachermodelform(request.POST)
        if form.is_valid():
            form.save()
        return homepage(request)
    return render(request,'school/teacher.html',teacherform)

@login_required
@permission_required('project.view_Teacher1')
def Teacher_report(request):
    result=Teacher1.objects.all()
    teacher={'allresult':result}
    return render(request,'school/teacher_report.html',teacher)


@login_required
@permission_required('project.delete_Teacher1')
def deleteteacher(request,id):
    s=Teacher1.objects.get(id=id)
    s.delete()
    Teacher_report(request)



@login_required
@permission_required('project.change_Teacher1')
def updateteacher(request,id):
    s=Teacher1.objects.get(id=id)
    form=teachermodelform(instance=s)
    dict={'form':form}
    if request.method=='POST':
        form=teachermodelform(request.POST,instance=s)
        if form.is_valid():
            form.save()
        return Teacher_report(request)
    return render(request,'update1.html',dict)