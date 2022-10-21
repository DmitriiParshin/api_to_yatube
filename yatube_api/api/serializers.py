from rest_framework.exceptions import ValidationError
from rest_framework.fields import CurrentUserDefault
from rest_framework.serializers import ModelSerializer
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        fields = '__all__'
        model = Post


class GroupSerializer(ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group


class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)


class FollowSerializer(ModelSerializer):
    user = SlugRelatedField(read_only=True, slug_field='username',
                            default=CurrentUserDefault())
    following = SlugRelatedField(slug_field='username',
                                 queryset=User.objects.all())

    class Meta:
        fields = '__all__'
        model = Follow
        validators = (
            UniqueTogetherValidator(queryset=Follow.objects.all(),
                                    fields=('user', 'following'),
                                    message='Уже подписан!'),
        )

    def validate_following(self, value):
        if self.context.get('request').user == value:
            raise ValidationError('Нельзя подписаться на себя!')
        return value
