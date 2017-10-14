from rest_framework import serializers
from api.models import NewsItem

class NewsItemSerializer(serializers.ModelSerializer):
    """
    serializer class for the newsitem
    """
    class Meta:
        """
        meta for the model and fields that the serializer class will use
        """
        model = NewsItem
        fields = ('id', 'source_id', 'title', 'author', 'picture_url', 'summary', 'story','news_item_source', 'article_url')
