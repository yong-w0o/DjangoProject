# app폴더 urls.py
# urls.py에서 blog앱에서 사용하는 url을 모두 가져옵니다.

from django.urls import path
from . import views #현재 폴더에 있는 views에 접근하기 때문

app_name = 'blog' # app_name에는 앱 이름을 넣어줍니다.

urlpatterns = [
    path('<int:id>', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path("update/<int:id>", views.update, name="update"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('newreply', views.newreply, name='newreply'),
    path('replydelete/<int:id>', views.replydelete, name="replydelete"),
]