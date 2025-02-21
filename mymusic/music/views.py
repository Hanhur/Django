from django.shortcuts import render, get_object_or_404
# from django.http import Http404
from music.models import Music

# Create your views here.
def index(request):
    songs = Music.objects.all()
    return render(request, 'music/index.html', {
        'all_songs': songs,
    })

def music_detail(request, id):
    # try:
    #     song = Music.objects.get(id=id)
    # except:
    #     raise Http404

    song = get_object_or_404(Music, id=id)

    return render(request, 'music/music_detail.html', {
        'title': song.title,
        'author': song.author,
        'description': song.description,
        'popular': song.is_popular,
    })