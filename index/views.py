from django.shortcuts import render

def index(request):
    context = {
        'page_title': '首頁',
    }
    return render(request, 'index/index.html', context)

def campus_food(request):
    context = {
        'page_title': '校內餐廳',
    }
    return render(request, 'index/campus_food.html', context)

def nearby_food(request):
    context = {
        'page_title': '校外餐廳',
    }
    return render(request, 'index/nearby_food.html', context)

def popular_food(request):
    context = {
        'page_title': '人氣排行',
    }
    return render(request, 'index/popular_food.html', context)

def rice_food(request):
    context = {
        'page_title': '飯類餐廳',
    }
    return render(request, 'index/popular_food.html', context)

def noodle_food(request):
    context = {
        'page_title': '面類排行',
    }
    return render(request, 'index/popular_food.html', context)

def about(request):
    context = {
        'page_title': '關於我們',
    }
    return render(request, 'index/about.html', context)
