from django.shortcuts import render
from django.http import HttpResponse

from . import models


# Функция для главной страницы
def home_page(request):
    # Курсы, Категории, Скидки
    category = models.Category.objects.all()
    courses = models.Course.objects.all()
    sales = models.Sale.objects.all()

    context = {'category': category, 'courses': courses, 'sales': sales}

    return render(request, 'homepage.html', context)


# Функция для вывода продуктов из категории
def get_category(request, pk):
    current_category = models.Category.objects.get(category_name=pk)
    courses_from_category = models.Course.objects.filter(course_category=current_category)

    return render(request, 'category.html', {'courses': courses_from_category, 'category': current_category})




