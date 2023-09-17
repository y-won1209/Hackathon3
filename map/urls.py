from .views import *
from django.urls import path

app_name = "map"

# 작품목록조회, 작품 해설(detail) 조회, 댓글 조회, 작성, 삭제, 수정 url.
urlpatterns = [
    path("place/", PlaceFilterView.as_view()),
    path("placelist/", PlaceListView.as_view()),
    #path("placedistancelist/", DistanceView.as_view()),
    path("placesearch/", PlaceSearchView.as_view()),
    path("place/<int:pk>/", PlaceDetailView.as_view()),
    path("my", MyViews.as_view()),
]
