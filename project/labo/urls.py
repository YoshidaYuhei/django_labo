from django.urls import path

from .views import item_views

app_name = 'labo'

urlpatterns = [
    path('top/', item_views.index, name='index'),
    path('item/<int:item_id>', item_views.detail, name='detail'),
    path('user/edit/', item_views.user_edit, name='user_edit'),
    path('item/edit/', item_views.item_edit, name='item_edit'),
    # items.html
    # path('items/', items_view.index, name='index'),
    # path('items/recent/', items_views.recent, name='recent_item'),
    # path('items/category/', items_views.category, name='category_item'),
    # path('items/ranking/', items_view.ranking, name='ranking_item'),
    
    # item_detail.html
    # path('items/detail/<int:item_id>', items_detail_view.detail, name='detail_item'),
    # path('items/edit/<int:item_id>', items_detail_view.edit, name='edit_item'),
    
    # users.html
    # path('users/', users_views.index, name='users_index'),
    # path('users/favorite', users_views.favorite, name='users_favorite'),
    
    # users_detail.html
    # path('users/detail/', users_views.detail, name='users_detail'),
    # path('users/edit/', users_views.edit, name='users_edit'),
]