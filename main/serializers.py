from rest_framework import serializers
from .models import Setting , Projects, Comments
import requests
BOT_TOKEN = "6948853620:AAE7pAm3v3FxP6zTFSLD-LBPxCEg3kyAqlk"
CHAT_ID = "981203451"
# Create your views here.
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = "__all__"

    password = serializers.CharField(write_only=True)



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"

    def create(self, validated_data):
        content =validated_data.get('comment', "")
        response = requests.post(url, json={"chat_id": CHAT_ID, "text": content})
        print(response.status_code)
        return Comments.objects.create(**validated_data)
