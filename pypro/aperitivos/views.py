from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'slug': 'Motivacao', 'vimeo_id': 425991579, 'titulo': 'Motivação'},
        'passar-do-dia': {'vimeo_id': 426262500, 'titulo': 'Passar do dia'}
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
