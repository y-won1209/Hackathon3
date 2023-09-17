from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
    path('mypage/', ProfileView.as_view()),
    path('mypage/my_comments/', MyCommentView.as_view()),
    path('mypage/my_recomments/', MyRecommentView.as_view()),
    path('mypage/my_scraped/', MyScrapedView.as_view()),
    path('mypage/my_posted/', MyPostedView.as_view()),
    path('profile/<int:user_id>/', UserProfileView.as_view()),
    #path('my_comments_page/', MyScrapedPostsView.as_view()),
    path('uniquecheck/', UsernameUniqueCheck.as_view()),
    path('delete/', AccountDeleteView.as_view()),

]
