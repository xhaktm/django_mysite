from django.db import models
from django.urls import reverse

# models.py 수정하면 반드시 migrate 해줘야함.! 만들고 db에 적용하기
#python manage.py makemigrations blog
#python manage.py migrate blog


class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    ip = models.GenericIPAddressField(null=True)
    tag = models.ManyToManyField('Tag', null=True, blank=True)
    
    # str 매서드 지정: 인스턴스만의 고유한 값으로 출력되도록 지정(선택 사항)  -> title 이름으로 보여짐.
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.id])
    
    
    
    """# title과 autoincremente된 id가 같이 나오게 수정
    def __str__(self) :
        return str(self.id) + ":" + self.title"""
        
        
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=20)
    message = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True) #값이 중복을 허용하지 않도록 unique지정
    
    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)