from django.shortcuts import render


def func_view(request):
    return render(request, 'second_task/func_template.html')


class ClassView:
    def as_view(request):
        return render(request, 'second_task/class_template.html')

