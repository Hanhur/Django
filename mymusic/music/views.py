from django.shortcuts import render, get_object_or_404
# from django.http import Http404
from music.models import Music
from django.db.models import Avg, Max, Min

# Create your views here.
def index(request):
    songs = Music.objects.all().order_by('rating')
    num_songs = songs.count()
    avg_rating = songs.aggregate(Avg('rating'))
    return render(request, 'music/index.html', {
        'all_songs': songs,
        'total_songs_number': num_songs,
        'average_rating': avg_rating,
    })

def music_detail(request, slug):
    # try:
    #     song = Music.objects.get(id=id)
    # except:
    #     raise Http404

    song = get_object_or_404(Music, slug=slug)

    return render(request, 'music/music_detail.html', {
        'title': song.title,
        'author': song.author,
        'description': song.description,
        'popular': song.is_popular,
    })