import json
from django.http import HttpResponse, JsonResponse
from .models import user, selfPost, twitterPost, instaPost
from dateutil.parser import parse
import twitter
from instagram_web_api import Client, ClientCompatPatch, ClientError, ClientLoginError
import time



TwitterApi = twitter.Api(consumer_key='tYbGmWUZkn4eNeJwG00t9N7Si',
                  consumer_secret='OoKHVW52WU7p2hbYo0dHp1Nb2zwk1wgwRUjQ6YaKauAFVehdl2',
                  access_token_key='3288956831-FpFDCVDeupp192qXpuJmOIC9VvT1gHXoHP0PQKc',
                  access_token_secret='GcSIrBQy4c23dCvt5xPWSjg7ItT8tlyGrYctSzHjmBmd7')

InstaApi = Client(auto_patch=True, drop_incompat_keys=False)


def getUser(request, username):
    u = user.objects.get(username=username)
    result = {
    "username": u.username,
    "twitterID": u.twitterID,
    "InstagramID": u.instaID
    }
    return JsonResponse(result, safe=False, status=200)

def getPosts(request, username):
    results = []
    u = user.objects.get(username=username)

    p = selfPost.objects.filter(user=u)
    for post in p:
        results.append({"id": post.id,"text": post.text, 'created_at': post.created_at, "source": "aggregator"})
    p = twitterPost.objects.filter(user=u)
    for post in p:
        results.append({"id": post.id,"text": post.text, 'created_at': post.created_at, "source": "twitter"})
    p = instaPost.objects.filter(user=u)
    for post in p:
        results.append({"id": post.id,"text": post.text, 'created_at': post.created_at, "source": "instagram"})
    
    return JsonResponse(results, safe=False, status=200)

def deleteUser(request, username):
    u = user.objects.get(username=username)
    u.delete()
    return JsonResponse({'deleted':True}, safe=False, status=200)

def createUser(request, username, twitter, insta):
    u = user(username=username, twitterID=twitter, instaID=insta)
    u.save()
    result = {
    "username": u.username,
    "twitterID": u.twitterID,
    "InstagramID": u.instaID
    }
    return JsonResponse(result, safe=False, status=201)

def updateUser(request, username, twitter, insta):
    u = user.objects.get(username=username)
    u.username = username
    u.twitterID = twitter
    u.instaID = insta
    u.save()

    result = {
    "username": u.username,
    "twitterID": u.twitterID,
    "InstagramID": u.instaID
    }
    return JsonResponse(result, safe=False, status=200)

def createSelfPost(request, username, text):
    u = user.objects.get(username=username)
    post = selfPost(user=u,text=text, created_at=int(time.time()))
    post.save()
    result = {"id": post.id,"text": post.text, "source":'aggregator'}
    return JsonResponse(result, safe=False, status=201)

def deleteSelfPost(request, idx):
    post = selfPost.objects.get(id=idx)
    post.delete()
    result = {"id": post.id,"text": post.text, "source":'aggregator'}
    return JsonResponse({'deleted':True}, safe=False, status=200)

def updateSelfPost(request, idx, text):
    post = selfPost.objects.get(id=idx)
    post.text = text
    post.save()
    result = {"id": post.id,"text": post.text, "source":'aggregator'}
    return JsonResponse(result, safe=False, status=200)

def getTwiiter(request, username):
    results = []
    u = user.objects.get(username=username)
    statuses = TwitterApi.GetUserTimeline(screen_name=u.twitterID)
    for status in statuses:
        time = parse(status.created_at).timestamp()
        post = twitterPost(user=u, text=status.text, created_at=int(time))
        post.save()
        results.append({"id": post.id,"text": post.text, 'created_at': post.created_at, "source": "instagram"})
    return JsonResponse(results, safe=False, status=201)

def getInstagram(request,username):
    results = []
    u = user.objects.get(username=username)
    user_info = InstaApi.user_info2(user_name=u.instaID)
    user_feed = InstaApi.user_feed(user_id=user_info['id'])
    for thing in user_feed:
        if len(thing['node']['edge_media_to_caption']['edges']) > 0:
            time = (thing['node']['taken_at_timestamp'])
            t = (thing['node']['edge_media_to_caption']['edges'][0]['node']['text'])
            post = instaPost(user=u, text=t, created_at=int(time))
            post.save()
            results.append({"id": post.id,"text": post.text, 'created_at': post.created_at, "source": "instagram"})
    return JsonResponse(results, safe=False, status=201)

def searchText(request, username, text):
    results = []
    u = user.objects.get(username=username)
    p = selfPost.objects.filter(user=u, text__icontains=text)
    for post in p:
        results.append({"id": post.id,"text": post.text, 'created_at': post.created_at, "source": "aggregator"})
    p = twitterPost.objects.filter(user=u, text__icontains=text)
    for post in p:
        results.append({"id": post.id,"text": post.text, 'created_at': post.created_at, "source": "twitter"})
    p = instaPost.objects.filter(user=u, text__icontains=text)
    for post in p:
        results.append({"id": post.id,"text": post.text, 'created_at': post.created_at, "source": "instagram"})
    return JsonResponse(results, safe=False, status=200)