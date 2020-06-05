from django.shortcuts import render


class Video:
    def __init__(self, slug, vimeo_id, titulo):
        self.slug = slug
        self.titulo = titulo
        self.vimeo_id = vimeo_id


videos = [
    Video('motivacao', 425991579, 'Motivação'),
    Video('passar-do-dia', 426262500, 'Passar do dia')
]

videos_dct = {v.slug: v for v in videos}


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})
