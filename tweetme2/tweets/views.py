from django.http.response import Http404, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import Tweet


def home_view(request, *args, **kwargs):

    return render(request, "pages/home.html", context={})



# for js
# when our 
def tweet_list_view(request, *args, **kwargs):
    """
    REST API VIEW
    Consume by JS or Swift/Java/iOS/
    return json data
    """

    objs = Tweet.objects.all()

    tweets_list  = [{"id": obj.id, "content": obj.content} for obj in objs]

    data = {

        "isUser":False,

        "tweets_list": tweets_list
    }

    return JsonResponse(data)


# 
def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    REST API VIEW
    Consume by JS or Swift/Java/iOS/
    return json data
    """


    data = {
        
        "id": tweet_id,
    }
    
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data["content"] = obj.content
        status = 200

    except:
        data["message"] = "Not found"
        status = 404

    return JsonResponse(data, status=status) # json.dumps content_type="/application_json"

