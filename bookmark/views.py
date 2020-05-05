from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import Bookmark

class BookmarkListView(ListView):
    model=Bookmark
    # 목록 뷰를 만들건데 목록에 사용되는 데이터베이스 모델은 Bookmark
    #template_name_suffix='_list', 얘는 따로 지정해주지 않아도 이동!
    paginate_by = 5

class BookmarkCreateView(CreateView):
    model=Bookmark
    fields=['site_name', 'url'] # CreateView에서 나타날 필드를 나열한 것. models의 필드값을 입력받겠다는 의미 (칸 생성)
    success_url = reverse_lazy('list')
    # 북마크의 add 버튼을 누르고 나면 그 다음에 나올 페이지를 정하는 것.
    # bookmark.urls의 네임인 list를 찾아서 거기에 나타나있는 view로 이동(BookmarkListView)
    template_name_suffix='_create'
    # 리스트 뷰를 만들고, 이 뷰(ListView)가 펼쳐질 때 사용되는 bookmark_list.html 템플릿에 자동으로 이동하게끔 되어있는데,
    # 이 클래스에서는 '_list'가 아닌 '_create'로 따로 찾아가겠다고 지정.
    # 지정해주지 않을 경우 디폴트값으로 '_form'으로 되어서, bookmark_form.html으로 이동! 그래서 '_create-로 따로 지정한 것

class BookmarkDetailView(DetailView):
    model=Bookmark
    # 따로 template~을 지정하지 않아도 html로 넘어감


class BookmarkUpdateView(UpdateView):
    model=Bookmark
    fields=['site_name', 'url']
    template_name_suffix='_update'
    # 제네릭의 edit에서만 디폴트값이 모두 _form인가? *


class BookmarkDeleteView(DeleteView):
    model=Bookmark
    success_url = reverse_lazy('list') # 삭제가 성공적으로 이루어지면 list로 넘어감