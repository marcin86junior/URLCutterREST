from rest_framework import serializers
from .models import Link


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['original_link', 'shortened_link',]
        read_only_fields = ('shortened_link','count',)


class EditLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'