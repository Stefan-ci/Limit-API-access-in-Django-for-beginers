from profil.models import Profile
from rest_framework.response import Response
from rest_framework.decorators import api_view
from profil.serializers import ProfileSerializer



@api_view(['GET'])
def get_all_profiles(request):
    profiles = [] #On déclare une liste vide. 
    
    #On vérifie d'abord si l'en-tête 'apiKey' est présent dans les en-têtes de la requête.
    if 'apiKey' in request.headers:
        try:
            #Si une clé est fournie, on essaie de vérifier si la clé fournie correspond
            # à une clé existant dans la base de données. Si oui, alors, au lieu de 
            # renvoyer une liste de profils vide, on renvoie les informations demandées 
            # à savoir tous les profils.
            profile = Profile.objects.get(api_key=request.headers['apiKey'])
            if profile:
                profiles = Profile.objects.all()
        except:
            pass
    
    data = {
        'profiles': ProfileSerializer(profiles, many=True).data
    }
    
    #La liste vide au début permet de renvoyer une liste vide si 'apiKey' ne figure pas
    # parmi les en-têtes de le requête ou bien si la clé fournie ne correspond à
    # aucune clé dans la table 'Profile'.
    #On peut très bien faire ceci avec une classe au lieu d'une fonction mais je
    # préfère les fonctions par rapport aux classes.
    
    return Response(data, content_type='application/json')

