from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

# 뷰객체: 서비스 처리 객체
def test1(request):
    #서비스 구현
    return HttpResponse('Good Luck')



def test2(request, no):
    #서비스 구현
    print(type(no))
    return HttpResponse(f"no : {no}")



#전체 목록 보기
def list(request):
    post_list = Post.objects.all()   # model객체 사용해서 view에서 서비스 실행 함수 작성 -> return 값은 QuerySet이 리스트형태로 나옴. 
    search_key = request.GET.get('keyword')
    if search_key:
        post_list = Post.objects.filter(title__contains=search_key)
    
    return render(request, 'blog/list.html', {'post_all': post_list, 'q': search_key})



#상세 보기 (아래 코드를 get_object_or_404로 간단하게 구현 가능 -> 없는 id값 넣으면 404 페이지 출력됨)
def detail(request, no):
    post = get_object_or_404(Post, id=no) #get 매서드 사용해서 결과값 1개: post 인스턴스임
    comment_list = post.comments.all()    #QuerySet임. 리스트 형태.
    tag_list = post.tag.all()
    return render(request, 'blog/detail.html', {'post': post, 
                                                'comment_all': comment_list,
                                                'tag_list': tag_list,})


def profile(request):
    user = User.objects.first()
    return render(request, 'blog/profile.html', {'user': user})



def tag_list(request, id):
    tag = Tag.objects.get(id=id)
    post_list = tag.post_set.all()
    return render(request, 'blog/list.html', {'post_all': post_list})
    


def test3(request):
    print('요청 방식: ', request.method)
    print('Get방식으로 정달된 문자열: ', request.GET)
    print('Post방식으로 전달된 문자열: ', request.POST)
    return render(request, 'blog/form_test.html')


# Form 기반 Data 생성 작업
def post_create(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid(): # 유효성 검사함 -> cleaned_data = {} 딕셔너리 객체가 생성됨
            print('cleaned_data: ', form.cleaned_data)
            #DB에 추가
            #post = Post.objects.create(**form.cleaned_data)
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post = form.save()
            return redirect(post)
    else:
        form = PostModelForm()
        
    return render(request, 'blog/post_form.html', {'form': form}) # 비어있는 폼



# Form 기반 Data 수정 작업
#'update/<id>/' <- 여기 url에 id에 값이 들어감.
def post_update(request, id):
    post = get_object_or_404(Post, id=id) #db에서 선택한 id와 같은 데이터를 db에서 뽑아냄.
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post) #save()가 추가, 수정이 다 가능하므로 위에 생성코드와 구별하기 위해 instance=post해줘서 db에서 가져온 데이터로 update임을 명시함.
        if form.is_valid():
            form.save()
            return redirect('blog:list')
    else:
        form = PostModelForm(instance=post) # form의 기본값 지정 : 바로 위에서 db에서 뽑아온 데이터를 form의 기본값으로 넣어주는 거임.instance 메서드 활용. 그냥 = 해서 넣어주면 됨.
        
    return render(request, 'blog/post_update.html', {'form': form}) # 수정작업이니까 기존에 채워져있던 값이 보여지는 폼으로 만들어야함
                                                                    # 그 값은 id에서 선택한 것에 해당하는 데이터를 db에서 가져옴.
    
    
# Data 삭제 작업
def post_delete(request, id):
    post = get_object_or_404(Post, id=id) #앞의 id는 필드명, 뒤의 id는 path 변수.
    if request.method == 'POST':
        post.delete()
        return redirect('blog:list')
        
    else:
        return render(request, 'blog/post_delete.html', {'post':post}) #delete 템플릿에 가보면 {{post}}로 context 보여주기때문에 'post'를 key에 적어준 거임.







"""#상세 보기
def detail(request, no): 
    try:
        post = Post.objects.get(id=no)
    
    except:
        return HttpResponse('존재하지 않는 데이터입니다.')
        
    return HttpResponse(post.title)"""