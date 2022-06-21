from django.shortcuts import render, HttpResponseRedirect
from .models import Student
from .forms import StudentForm
from django.contrib import messages


def student_add(request):
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        print(fm)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            ct = fm.cleaned_data['city']
            rl = fm.cleaned_data['roll']
            stud = Student(name=nm, city=ct, roll=rl)
            stud.save()
            messages.success(request, 'Data Added Successfully !!!')
    else:
        fm = StudentForm()

    return render(request, "add.html", {'form': fm})


def student_show(request):
    stud = Student.objects.all()
    print(stud)
    return render(request, "show.html", {'student': stud})


def student_edit(request, id):
    if request.method == 'POST':
        stud = Student.objects.get(pk=id)
        fm = StudentForm(request.POST, instance=stud)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Data Updated Successfully !!!')
            return HttpResponseRedirect("/show/")
    else:
        stud = Student.objects.get(pk=id)
        fm = StudentForm(instance=stud)
    return render(request, "edit.html", {'form': fm})


def student_delete(request, id):
    stud = Student.objects.get(pk=id)
    stud.delete()
    messages.success(request, 'Data Deleted Successfully !!!')
    return HttpResponseRedirect('/show/')
