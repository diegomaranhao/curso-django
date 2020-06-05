from django.shortcuts import render

videos = [
    {'slug': 'motivacao', 'vimeo_id': 425991579, 'titulo': 'Motivação'},
    {'slug': 'passar-do-dia', 'vimeo_id': 426262500, 'titulo': 'Passar do dia'}
]

videos_dct = {dct['slug']: dct for dct in videos}


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})

