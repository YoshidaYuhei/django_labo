from importlib import import_module
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from project.labo.infra.query_service import ItemQueryService


@login_required
def index(request):
    """Item一覧表示"""
    query_service = ItemQueryService
    context = query_service.get_all_items()
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