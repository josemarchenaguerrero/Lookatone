from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
import tweepy
from tweepy import OAuthHandler
import re
from UnderTwitter.settings import *
from Twitter.models import *
from social_django.models import UserSocialAuth
from tweepy.error import *
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

#login personalizado
def customlogin(request):
    return render(request,'twitter/registration/login.html')

#logout personalizado
def customlogout(request):
    logout(request)
    return render(request,'twitter/registration/login.html')

#abre el template de la aplicación
def cargar(request):
    if request.user.id:
        return render(request, 'twitter/principal.html')
    else:
        return render(request,'twitter/registration/login.html')

#función que devuelve una lista de tweets en función de un hashtag o palabra clave dada.
def Filtrartweet(request):
    try:
        keyword = request.GET.get('filt')
        #tokens de aplicación
        CONSUMER_KEY = SOCIAL_AUTH_TWITTER_KEY
        CONSUMER_SECRET = SOCIAL_AUTH_TWITTER_SECRET

        #consulta para objtener un objeto de UserSocialAuth donde se alojan los token de usuario
        usuario = User.objects.get(username=request.user.username)
        usk = UserSocialAuth.objects.get(user_id=usuario.id)
        ACCESS_TOKEN = usk.extra_data['access_token']['oauth_token']
        ACCESS_TOKEN_SECRET = usk.extra_data['access_token']['oauth_token_secret']

        #autentificación de tokens  de la aplicación y usuario.
        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)

        #busqueda de tweets por la palabra clave
        tweets = api.search(q=keyword)

        #se crea una lista para poder jserializar la información y enviarla al template
        list = []
        arrayus = {}
        for a in tweets:
            content = ""
            content += str(a.id_str) + ';' + str(a.created_at) + ';' + str(a.text)
            list.append(content)

        data = {'hastaghs': list,'arrlugares':arrayus}

        return JsonResponse(data, safe=False)
    except TweepError as e:

        data = {'error':str(e.response)}

        return JsonResponse(data,safe=False)


def principal(request):
    try:
        #usuario pasado por get a través de formulario
        username = request.GET.get('username')

        #tokens de aplicación
        CONSUMER_KEY = SOCIAL_AUTH_TWITTER_KEY
        CONSUMER_SECRET = SOCIAL_AUTH_TWITTER_SECRET

        #obtencion tokens usuario almacenados en un objeto del modelo UserSocialAuth
        usuario = User.objects.get(username=request.user.username)
        usk = UserSocialAuth.objects.get(user_id=usuario.id)
        ACCESS_TOKEN = usk.extra_data['access_token']['oauth_token']
        ACCESS_TOKEN_SECRET = usk.extra_data['access_token']['oauth_token_secret']

        #autentificación de tokens de la aplicación
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        api = tweepy.API(auth)

        #obtiene el objeto del usuario introducido
        user_me = api.get_user(username)

        #obtiene los seguidores del usuario, count señala el numero de resultados que va a devolver la consulta
        seguidores_user = api.followers(user_id=user_me.id,count=10)
        #obtiene los tweets del usuario
        tweets_user = api.user_timeline(user_id=user_me.id,count=10)
        #obtiene a las perona que sigue el usuario
        seguidos_id_user = api.friends_ids(user_id=user_me.id,count=10)

        #se crean listas para jserializar la información y enviarla al template
        seguidos_user = {}

        if(user_me.location):
            localizacion = user_me.location
        else:
            localizacion = 'Disabled'

        if(user_me.profile_location):
            perfillocation = user_me.profile_location
        else:
            perfillocation = 'None'

        if(user_me.description):
            descripcion = user_me.description
        else:
            descripcion = 'None'

        if(user_me.geo_enabled):
            geo = 'Enabled'
        else:
            geo = "Disabled"

        dic = {}
        dicfollowers = {}
        dicdispositivo = {}
        usulugar={}
        usudlugar={}
        mostmentioned={}
        hashtags_dict = {}

        for tw in tweets_user:
            if tw.id_str not in dic:
                contenido = tw.id_str+";"+str(tw.created_at)+";"+tw.text+";"+tw.source
                dic[tw.id_str] = contenido

            if tw.source not in dicdispositivo:
                dicdispositivo[tw.source] = 1
            else:
                dicdispositivo[tw.source] += 1

            nuevacadena = re.sub('[^ @a-zA-Z0-9]', '', str(tw.text))
            division = nuevacadena.split(" ")

            for a in division:
                if '@' in a:
                    if a[a.index('@'):] not in mostmentioned:
                        mostmentioned[a[a.index('@'):]] = 1
                    else:
                        mostmentioned[a[a.index('@'):]] += 1


            hashtags = tw.entities.get('hashtags')
            for hashtag in hashtags:
                if hashtag['text'] in hashtags_dict.keys():
                    hashtags_dict[hashtag['text']] += 1
                else:
                    hashtags_dict[hashtag['text']] = 1

        for f in seguidores_user:
            if f.id_str not in dicfollowers:
                contenido = f.id_str+";"+f.name+";"+f.screen_name+";"+f.description
                dicfollowers[f.id_str]=contenido
            if (f.location not in usulugar):
                if(f.location != '' and f.location!=','):
                    usulugar[f.location]=f.screen_name
            else:
                if (f.location != '' and f.location != ','):
                    contenido = usulugar[f.location]
                    usulugar[f.location]= contenido+';'+f.screen_name

        for seguidos in seguidos_id_user:
            seguidor = api.get_user(seguidos)

            if seguidor.id_str not in seguidos_user:
                contenido = seguidor.id_str + ";" + seguidor.name + ";" + seguidor.screen_name + ";" + seguidor.description
                seguidos_user[seguidor.id_str]=contenido

            if seguidor.location not in usudlugar:
                if (seguidor.location != '' and seguidor.location != ','):
                    usudlugar[seguidor.location] = seguidor.screen_name
            else:
                if (seguidor.location != '' and seguidor.location != ','):
                    contenido = usudlugar[seguidor.location]
                    usudlugar[seguidor.location] = contenido + ';' + seguidor.screen_name

        #se envía la información solicitada al template
        lista = {'username':user_me.screen_name,'name':user_me.name,'id':user_me.id_str,'location':localizacion,'profilelocation':perfillocation,'description':descripcion
                 ,'geoenabled':geo,'creationdata':user_me.created_at,'image':user_me.profile_image_url_https,'followers':user_me.followers_count,'following':user_me.friends_count
                 ,'tweets':user_me.statuses_count}

        data = {'user':lista,'listatweets':{'lista':dic,'listadispositivos':dicdispositivo,'listafollowers':dicfollowers,'listafollowing':seguidos_user,
                                            'usulugar':usulugar,'usudlugar':usudlugar},'hash':hashtags_dict,'mostmentioned':mostmentioned}

        return JsonResponse(data, safe=False)
    except TweepError as e:
        print(e.response)
        data = {'error':str(e.response)}
        return JsonResponse(data,safe=False)


def comprobar(request):
    if request.method == 'POST':
        uploaded_files = request.FILES

        if uploaded_files:
            data = {'data':'si'}
        else:
            data = {'data': 'no'}
        return JsonResponse(data, safe=False)

def comprobaramistad(request):
    try:
        #se obtienen los usuarios a comprobar del formulario por get
        username = request.GET.get('usu1')
        username2 = request.GET.get('usu2')

        #tokens de aplicación
        CONSUMER_KEY = SOCIAL_AUTH_TWITTER_KEY
        CONSUMER_SECRET = SOCIAL_AUTH_TWITTER_SECRET

        #autentificación de los tokens
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        api = tweepy.API(auth)

        #se obtiene un objeto de cada usuario
        user1 = api.get_user(username)
        user2 = api.get_user(username2)

        #comprueba si existe relación
        respuesta = api.show_friendship(source_id=user1.id,target_id=user2.id)

        #se retorna la información al template
        data ={ 'rfollowing':respuesta[0].following,'rfollowed':respuesta[0].followed_by}

        return JsonResponse(data, safe=False)
    except TweepError as e:
        data = {'error': str(e.response)}

        return JsonResponse(data, safe=False)


def cargargeotweets(request):
    try:
        #obtiene la ubicacion por get desde el formulario
        ubicacion = request.GET.get('ubi')

        #tokens de aplicación
        CONSUMER_KEY = SOCIAL_AUTH_TWITTER_KEY
        CONSUMER_SECRET = SOCIAL_AUTH_TWITTER_SECRET

        #obtiene los tokens de usuarios almacenados en el modelo UserSocialAuth
        usuario = User.objects.get(username=request.user.username)
        usk = UserSocialAuth.objects.get(user_id=usuario.id)

        ACCESS_TOKEN = usk.extra_data['access_token']['oauth_token']
        ACCESS_TOKEN_SECRET = usk.extra_data['access_token']['oauth_token_secret']

        #autentificación de tokens
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)

        #obtiene tweets por geolocalización
        places = api.geo_search(query=ubicacion, granularity="city")
        place_id = places[0].id
        tweets = api.search(q="place:%s" % place_id)

        #se crea lista para poder jserializar la informacion que se retorna al template
        array = []
        arrayus = {}

        for a in tweets:
            content = ""
            #.id_str para el id del tweet, .created_at para la fecha de creación y .text para el texto del tweet
            content += str(a.id_str)+';'+ str(a.created_at) +';'+str(a.text)
            array.append(content)
            #se obtiene la localización del tweet con el .place.full_name
            arrayus[a.place.full_name]='tweet id: '+ str(a.id_str)


        data = {'rfollowing': array,'arrlugares':arrayus}

        return JsonResponse(data, safe=False)
    except TweepError as e:
        data = {'error': str(e.response)}

        return JsonResponse(data, safe=False)

def Seguimientoalarma(request):

    try:
        #usuario y palabra clave obtenidos por método get desde un formulario
        usuario = request.GET.get('usualarma')
        clave = request.GET.get('usupalabra')

        #tokens de aplicación
        CONSUMER_KEY = SOCIAL_AUTH_TWITTER_KEY
        CONSUMER_SECRET = SOCIAL_AUTH_TWITTER_SECRET

        #se obtienen tokens de usuario alojados en el model UserSocialAuth
        usuari = User.objects.get(username=request.user.username)
        usk = UserSocialAuth.objects.get(user_id=usuari.id)
        ACCESS_TOKEN = usk.extra_data['access_token']['oauth_token']
        ACCESS_TOKEN_SECRET = usk.extra_data['access_token']['oauth_token_secret']

        #autentificación de tokens
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)

        #objeto de usuario
        user_me = api.get_user(usuario)
        #obtiene los tweets del usuario dado
        tweets_user = api.user_timeline(user_id=user_me.id, count=5)

        #se crean listas para jserializar la información solicitada
        lista = {}

        #la función de la alarma consiste en peticiones en bucle por ajax al controlador y el controlador comprueba cada x tiempo si hay tweets nuevos
        for tweet in tweets_user:
            if str(clave).lower() in str(tweet.text).lower():
                    #comprueba si hay en la bd si existe el tweet en esa fecha con ese texto y para ese usuario
                    obj = Alarmcontrol.objects.filter(fecha = str(tweet.created_at), texto=str(tweet.text), usuario=usuario).count()

                    #si lo encuentra es porque ya se ha mostrado en el template y si no lo encuentra es porque aun no se ha mostrado. El programa lo almacena en la bd y lo
                    #envía al template
                    if obj :
                        lista['no'] = 'false'
                    else:
                        obj = Alarmcontrol(fecha=str(tweet.created_at), texto=str(tweet.text), usuario=usuario)
                        obj.save()
                        cadena = ""
                        cadena += str(tweet.created_at) + ' ' + tweet.text + ';true'
                        lista[str(tweet.id_str)] = cadena


        data = {'response': lista}

        return JsonResponse(data, safe=False)
    except TweepError as e:
        data = {'error': str(e.response)}

        return JsonResponse(data, safe=False)