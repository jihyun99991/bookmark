from django.contrib import admin

from .models import Bookmark  #.models 라는 것은 현재 폴더의 models 파일을 의미


admin.site.register(Bookmark) # models파일의 bookmark라는 클래스를 불러와서 등록.
