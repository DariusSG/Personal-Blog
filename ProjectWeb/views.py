from django.http import HttpResponsePermanentRedirect
from django.views.generic import TemplateView


class VideoPlayer(TemplateView):
    template_name = 'video.html'
    template_engine = 'engine_jinja2'

    async def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        video_uuid = self.request.GET.get('v', None)

        if video_uuid is None:
            video_uuid = "k"
        context = {
            "page_title": "Video Player",
            "page_dir": [
                {"link": False, "name": "Video Player"}
            ],
            'vid_url': f"something.com/{str(video_uuid)}.mpd"
        }
        return context

    async def get(self, request, *args, **kwargs):
        context: str | dict = await self.get_context_data(**kwargs)
        if context is None:
            return HttpResponsePermanentRedirect('/')
        return self.render_to_response(context)
