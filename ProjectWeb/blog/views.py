from django.db import OperationalError
from django.http import HttpResponsePermanentRedirect
from django.views.generic import TemplateView

from ProjectWeb.blog.markdown_utils import conv_from_markdown
from ProjectWeb.blog.models import Post


class Article(TemplateView):
    template_name = "posts/post.html"
    template_engine = 'engine_jinja2'

    async def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_id = self.request.GET.get('id', None)
        if post_id is None:
            return None

        try:
            md_post: Post = await Post.objects.aget(slug__exact=post_id)
            context['page_title'] = md_post.title
            context['page_dir'] = [
                {"link": False, "name": md_post.title}
            ]
            context['post'], context['post_toc'] = conv_from_markdown(md_post.content)
            author = await md_post.post_author()
            context['author_name'] = " ".join([author.first_name, author.last_name])
            context['creation_date'] = md_post.created_on.strftime('%b %d')
            context['read_time'] = md_post.read_time

        except OperationalError:
            return None

        return context

    async def get(self, request, *args, **kwargs):
        context: str | dict = await self.get_context_data(**kwargs)
        if context is None:
            return HttpResponsePermanentRedirect('/')
        return self.render_to_response(context)


class Article_Creation(TemplateView):
    template_name = 'posts/create.html'
    template_engine = 'engine_jinja2'

    async def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pass

    async def get(self, request, *args, **kwargs):
        pass

