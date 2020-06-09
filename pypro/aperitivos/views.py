from django.shortcuts import render, get_object_or_404

from pypro.aperitivos.models import Video

videos = [
    Video(slug='motivacao', titulo='Motivação', vimeo_id='425991579'),
    Video(slug='passar-do-dia', titulo='Passar do dia', vimeo_id='426262500')
]

videos_dct = {v.slug: v for v in videos}


def video(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})
