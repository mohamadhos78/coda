from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import emailservice
from .models import main, adminProfile


class contact_us(TemplateView):
    from .forms import centure_form
    mains = []
    main_query = main.objects.all()
    for c in main_query:
        mains.append({
            'logo': c.logo.url,
            'field1': c.field1,
            'field2': c.field2,
            'field3': c.field3,
            'field4': c.field4,
        })
    users = []
    user_query = adminProfile.objects.all()
    for a in user_query:
        users.append({
            'name': a.user.first_name + ' ' + a.user.last_name,
            'img': a.avatar.url,
            'description': a.description,
            'theory': a.theory
        })
    centure_form = centure_form()
    form = emailservice()

    def get(self, request, **kwargs):
        context = {
            'users': self.users,
            'main': self.mains[0],
            'centure': self.centure_form,
            'form': self.form,
        }
        return render(request, "contact.htm", context)

    def post(self, request):
        centure_filled_form = self.centure_form(request.POST)
        filled_form = emailservice(request.POST)
        if filled_form.is_valid():
            filled_form.save()
        if centure_filled_form.is_valid():
            centure_filled_form.save()
        context = {
            'users': self.users,
            'main': self.mains[0],
            'form': self.form,
            'centure_form': self.centure_form,
        }
        return render(request, "index.htm", context)


class index(TemplateView):
    mains = []
    users = []
    user_query = adminProfile.objects.all()
    main_query = main.objects.all()
    for c in main_query:
        mains.append({
            'logo': c.logo.url,
            'field1': c.field1,
            'field2': c.field2,
            'field3': c.field3,
            'field4': c.field4,
        })
    for a in user_query:
        users.append({
            'name': a.user.first_name + ' ' + a.user.last_name,
            'img': a.avatar.url,
            'description': a.description,
            'theory': a.theory,
            'github': a.social_media.github,
            'linkedin': a.social_media.linkedin,
            'twitter': a.social_media.twitter,
            'telegram': a.social_media.telegram,
            'bale': a.social_media.bale,
            'instagram': a.social_media.instagram,
        })

    def get(self, request, **kwargs):
        form = emailservice()
        context = {
            'users': self.users,
            'main': self.mains[0],
            'form': form,
        }
        return render(request, "index.htm", context)

    def post(self, request):
        filled_form = emailservice(request.POST)
        if filled_form.is_valid():
            filled_form.save()
        form = emailservice()
        context = {
            'users': self.users,
            'main': self.mains[0],
            'form': form,
        }
        return render(request, "index.htm", context)


class costs(TemplateView):
    mains = []
    main_query = main.objects.all()
    for c in main_query:
        mains.append({
            'logo': c.logo.url,
            'field1': c.field1,
            'field2': c.field2,
            'field3': c.field3,
            'field4': c.field4,
        })

    def get(self, request, **kwargs):
        form = emailservice()
        context = {
            'main': self.mains[0],
            'form': form,
        }
        return render(request, 'costs.htm', context)

    def post(self, request):
        filled_form = emailservice(request.POST)
        if filled_form.is_valid():
            filled_form.save()
        form = emailservice()
        context = {
            'main': self.mains[0],
            'form': form,
        }
        return render(request, "index.htm", context)


class portfolio(TemplateView):
    def get(self, request, **kwargs):
        # mains = []
        # main_query = main.objects.all()
        # for c in main_query:
        #    mains.append({
        #        'logo':c.logo ,
        #        'field1':c.field1 ,
        #        'field2':c.field2 ,
        #        'field3':c.field3 ,
        #        'field4':c.field4 ,
        #    })
        context = {
        }
        return render(request, "portfolio.htm", context)


class blog(TemplateView):
    from django.db.models import Q
    from .models import Article
    # for searching in blog
    mains = []
    posts = []
    post_query = Article.objects.all()
    main_query = main.objects.all()
    for c in main_query:
        mains.append({
            'logo': c.logo.url,
            'field1': c.field1,
            'field2': c.field2,
            'field3': c.field3,
            'field4': c.field4,
        })
    for post in post_query:
        posts.append({
            'id': post.id,
            'author': post.author,
            'cover': post.cover.url,
            'content': post.content[:256] + "...",  # just shows the 256 character
            'category': post.category,
            'title': post.title,
        })

    def get(self, request, **kwargs):
        query = request.GET.get('q')
        if query:
            results = []
            queryset = self.Q(title__icontains=query) | self.Q(content__contains=query)
            # include searched data in title or content
            result_query = self.Article.objects.filter(queryset).distinct()
            # distinct remove duplicate search results
            for result in result_query:
                results.append({
                    'id': result.id,
                    'author': result.author,
                    'cover': result.cover.url,
                    'content': result.content[:256] + "...",  # just shows the 256 character
                    'category': result.category,
                    'title': result.title,
                })
        else:
            results = []
        form = emailservice()
        context = {
            'main': self.mains[0],
            'form': form,
            'posts': self.posts,
            'results': results,
            'query': query,
        }
        return render(request, "blog.htm", context)

    def post(self, request):
        filled_form = emailservice(request.POST)
        if filled_form.is_valid():
            filled_form.save()
        form = emailservice()
        context = {
            'main': self.mains[0],
            'form': form,
            'posts': self.posts,
        }
        return render(request, "blog.htm", context)


def posts(request, pk):
    from django.shortcuts import get_object_or_404
    from .models import Article
    from .forms import CommentForm
    # Forms
    comment = CommentForm()
    form = emailservice()

    # Navbar stuff
    main_query = get_object_or_404(main, id=1)
    mains = {
        'logo': main_query.logo.url,
        'field1': main_query.field1,
        'field2': main_query.field2,
        'field3': main_query.field3,
        'field4': main_query.field4,
    }

    # Comment and Post
    new_comment = None  # uses for saving comments in post part
    query = get_object_or_404(Article, pk=pk)
    comment_query = query.comments.filter(permission=True)
    comments = []
    for i in comment_query:
        comments.append({
            'name': i.name,
            'date': i.date,
            'text': i.text,
        })
    result = {
        'id': query.id,
        'author': query.author,
        'avatar': query.author.avatar.url,
        'cover': query.cover.url,
        'content': query.content,
        'category': query.category,
        'title': query.title,
        'created_at': query.created_at,
    }

    if request.method == "GET":
        context = {
            'post': result,
            'main': mains,
            'form': form,
            'comments': comments,
            "comment": comment,
        }
        return render(request, "post.htm", context)
    if request.method == "POST":
        # EmailService input part
        filled_form = emailservice(request.POST)
        if filled_form.is_valid():
            filled_form.save()

        # comments input part
        comment = CommentForm(request.POST)
        if comment.is_valid():
            new_comment = comment.save(commit=False)
            new_comment.post = query
            print(new_comment)
            new_comment.save()

        context = {
            'main': mains,
            'comments': comments,
            'post': result,
            'form': form,
            "comment": "comment",
        }
        return render(request, "post.htm", context)
