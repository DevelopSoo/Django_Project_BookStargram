from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    class Meta:
        ordering = ['-created_at']

    POST_TYPES = [
        (0, '기타'),
        (1, '소설'),
        (2, '시/에세이'),
        (3, '경제/경영'),
        (4, '자기계발')
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50,
                             verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    view_count = models.IntegerField(default=0,
                                     verbose_name="조회 수")

    _type = models.PositiveSmallIntegerField(choices=POST_TYPES,
                                             verbose_name="종류")
    image = models.ImageField(upload_to='bookst/image', default='bookst/default/기본이미지.jpg')

    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="생성 시간")
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name="수정 시간")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bookst:detail', args=[self.pk])

