from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CurrentUserDefault
from rest_framework.serializers import ModelSerializer
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Group, Post, Follow


User = get_user_model()


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class GroupSerializer(ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group


class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(read_only=True, slug_field='username')
    post = SlugRelatedField(read_only=True, slug_field='pk')

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(ModelSerializer):
    user = SlugRelatedField(read_only=True, slug_field='username',
                            default=CurrentUserDefault())
    following = SlugRelatedField(slug_field='username',
                                 queryset=User.objects.all())

    class Meta:
        fields = ('user', 'following')
        model = Follow
        validators = (
            UniqueTogetherValidator(queryset=Follow.objects.all(),
                                    fields=('user', 'following'),
                                    message='Уже подписан!'),
        )

    def validate(self, data):
        if data['following'] == self.context.get('request').user:
            raise ValidationError('Нельзя подписаться на себя!')
        return data
