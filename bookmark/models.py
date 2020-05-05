from django.db import models
from django.urls import reverse

class Bookmark(models.Model):
    site_name=models.CharField(max_length=100) # 문자열로 최대 100글자까지 저장,
    url=models.URLField('Site URL') # http://www. 형태의 문자열을 저장할 수 있음,
    # url=>'Site URL'로 지정함으로써 admin 실행 사이트에서 bookmark 테이블의 폴더 안에 이름이 그대로 들어감
    # site_name은 따로 이름을 지정해주지 않았기 때문에 변수의 이름이 그대로 들어감

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
    # views 에서 success_url을 따로 설정하지 않은 경우, 이 함수 실행

    def __str__(self):
        return "이름:" + self.site_name + ", 주소:" + self.url