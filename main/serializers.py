from rest_framework import serializers
from .models import *
from django.db.models import Q
from rest_framework.serializers import ReadOnlyField
from datetime import datetime, timedelta

class FunctionMixin:
    def get_relikes_count(self, obj):
        return obj.relikes.count()

    def get_created_at(self, obj):
        current_time = datetime.now(obj.created_at.tzinfo)
        time_difference = current_time - obj.created_at

        if time_difference < timedelta(minutes=1):
            return "방금 전"
        elif time_difference < timedelta(hours=1):
            return f"{int(time_difference.total_seconds() / 60)}분 전"
        elif time_difference < timedelta(days=1):
            return f"{int(time_difference.total_seconds() / 3600)}시간 전"
        else:
            return obj.created_at.strftime('%m-%d')
        
    def get_scraps_count(self, obj):
        return obj.scraps.count()
    
    def get_recomments_count(self, obj):
        return obj.recomments.count()
    
    def get_comment_count(self, obj):
        return obj.comment.count() 
    
    def get_author_username(self, obj):
        return obj.author.username if obj.author else""
    
    def get_likes_count(self, obj):
        return obj.likes.count()
    
    #def get_all_comments_count(self, obj):
    #    return self.get_comment_count(obj) + self.get_recomments_count(obj)


class RecommentSerializer(FunctionMixin, serializers.ModelSerializer):
    relikes_count = serializers.SerializerMethodField()
    author_username = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Recomment
        fields = (
            "id",
            "author",
            "author_username",
            "created_at",
            "content",
            "relikes",
            "relikes_count",
        )
    read_only_fields = ["author"]


class CommentSerializer(FunctionMixin, serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    recomments_count = serializers.SerializerMethodField()
    author_username = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    #post = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            "id",
            "author",
            "post",
            "author_username",
            "content",
            "created_at",
            "likes",
            "likes_count",
            #"recomments",
            "recomments_count",
        ]
    read_only_fields = ["author"]

    
class CommentDetailSerializer(FunctionMixin, serializers.ModelSerializer):
    #comment_like = LikeSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()
    recomments = RecommentSerializer(many=True, read_only=True)
    author_username = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            "id",
            "author",
            "author_username",
            "post",
            "author",
            "content",
            "created_at",
            "likes",
            "likes_count",
            "recomments",
        ]
    read_only_fields = ["author","post"]



class PostSerializer(FunctionMixin, serializers.ModelSerializer):
    #comment = CommentSerializer(many=True, read_only=True)
    scraps_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField() 
    image = serializers.ImageField(use_url = True)
    author_username = serializers.SerializerMethodField()
    # is_manager = serializers.SerializerMethodField()
    # total_comment_count = serializers.SerializerMethodField()



    class Meta:
        model = Post
        fields = [ 
            "id",
            "author",
            "author_username",
            "image",
            "description",
            "title",
            "painter",
            "type",
            "scraps",
            "scraps_count",
            "comment_count",
            #"is_manager",
            #"total_comment_count",

        ]

        read_only_fields = ["author"]

    # def get_is_manager(self, obj):
    #    user = self.context['request'].user
    #    return user.is_authenticated and user.manager


class PostDetailSerializer(FunctionMixin, serializers.ModelSerializer):
    scraps_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    author_username = serializers.SerializerMethodField()
    image = serializers.ImageField(use_url = True)
    #all_comments_count = serializers.SerializerMethodField()


    class Meta:
        model = Post
        fields = [ 
            "id",
            "author",
            "author_username",
            "image",
            "description",
            "content",
            "title",
            "painter",
            "drawing_technique",
            "work_year",
            #"type_choices",
            "type",
            "scraps",
            "scraps_count",
            "created_at",
            #"comment",
            "comment_count",
        ]
        read_only_fields = ["author"]
'''
class ImageSerializers(serializers.ModelSerializer):
    author_username = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fielsd = ['id','post','image',"username"] '''