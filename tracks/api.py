from typing import List, Optional

from django.http import JsonResponse
from ninja import NinjaAPI

from tracks.models import Track
from tracks.schema import TrackSchema, NotFoundSchema, TrackSchemaUpdate

api = NinjaAPI()


@api.get('/tracks', response=List[TrackSchema])
def tracks(request, title: Optional[str] = None):
    if title:
        return Track.objects.filter(title__icontains=title)
    return Track.objects.all()


@api.get('/tracks/{track_id}', response={200: TrackSchema, 404: NotFoundSchema})
def track(request, track_id: int):
    try:
        track = Track.objects.get(pk=track_id)
        return track
    except Track.DoesNotExist as e:
        return 404, {"message": "Track does not exist"}


@api.post('/tracks', response={201: TrackSchema})
def create_track(request, track: TrackSchema) -> Track:
    track = Track.objects.create(**track.dict())
    return track


@api.put('/tracks/{track_id}', response={200: TrackSchema, 404: NotFoundSchema})
def change_track(request, track_id: int, data: TrackSchema):
    try:
        track = Track.objects.get(pk=track_id)
        for attibute, value in data.dict().items():
            setattr(track, attibute, value)
        track.save()
        return 200, track
    except Track.DoesNotExist as e:
        return 404, {"message": "Track does not exist"}


@api.delete('/tracks/{track_id}', response={200: None, 404: NotFoundSchema})
def delete_track(request, track_id: int):
    try:
        track = Track.objects.get(id=track_id)
        track.delete()
        return JsonResponse({'success': True})
    except Track.DoesNotExist as e:
        return 404, {"message": "Track does not exist"}
