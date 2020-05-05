from django.urls import path
from .views import * # view에 있는 모든 클래스들을 import해라

urlpatterns=[
    path('', BookmarkListView.as_view(), name='list'),
    # config.urls에서는 bookmark로 지정했지만 bookmark.url으로 넘어오면서 경로가 사라짐(자동으로 달려있음)
    # 여기서 BookmarkListView를 보여줘라-> 그런데 view에는 보여줄 내용이 없음 -> html 생성
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    #detail/뒤에 정수가 오면 그 값을 pk로 해라 + view 열어라
    path('update/<int:pk>',BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>',BookmarkDeleteView.as_view(), name='delete'),
]