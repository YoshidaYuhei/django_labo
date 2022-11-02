from importlib import import_module
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    """Item一覧表示"""
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # TODO: コンテキスト出力はQueryService→DTO
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'labo/index.html', context)

def detail(request, question_id):
    """TODO: Item詳細画面"""
    data = []
    return render(request, 'labo/detail.html', data)

def user_edit(request, question_id):
    """TODO: ユーザー情報編集画面"""
    data = []
    return render(request, 'labo/user.html', data)

def item_edit(request):
    """TODO: Item作成画面"""
    data = []
    return render(request, 'labo/create_item.html', data)