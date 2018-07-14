from django.shortcuts import render, redirect
from .models import Post,City
from .forms import PostForm


def main(request):
    return render(request, 'travel/_main.html')

def local_list(request):
    queryset = City.objects.all()

    queryset1 = Post.objects.all()


    return render(request, 'travel/local_list.html', {
        'local' : queryset,
        'local_list' : queryset1
    })

def local_detail(request, City):
    queryset = Post.objects.all()
    path = request.path
    print(path)
    filter = path.split('/')[3]
    print(filter)
    qs = queryset.filter(City__city=filter)

    return render(request, 'travel/local_detail.html',{
        'local_list': qs
    })


def local_detail_form(request, City ,pk):
    queryset = Post.objects.all()
    path = request.path
    print(path)
    filter = path.split('/')[4]
    print(filter)
    qs = queryset.filter(pk=filter)
    return render(request, 'travel/local_detail_form.html',{
        'local_detail': qs,
        'filter':filter,
    })



def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else:
        form = PostForm()
    return render(request, 'travel/post_form.html', {
        'form': form,
})