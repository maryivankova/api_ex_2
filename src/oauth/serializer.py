from rest_framework import serializers


class GoogleAuth(serializers.Serializer):
    """ Serializer of date of Google
    """
    email = serializers.EmailField()
    token = serializers.CharField()
