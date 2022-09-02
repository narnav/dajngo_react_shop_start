from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from .serializers import NoteSerializer
from base.models import Note
from django.contrib.auth import logout

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['eeemail'] = user.email
        # ...

        return token

# login
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# @api_view(['GET'])
# def getRoutes(request):
#     routes = [
#         '/api/token',
#         '/api/token/refresh',
#     ]

#     return Response(routes)

# register/signup
@api_view(['POST'])
def register(request):
    User.objects.create_user(username= request.data["username"],email=request.data["email"],password=request.data["password"])
    print( request.data["username"])
    print( request.data["email"])
    print(request.data["password"])
    return Response("routes")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCategories(request):
    return Response("Categories")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def myLogout(request):
    logout(request)
    return Response("for yanay with love")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
    user = request.user
    notes = user.note_set.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOneNote(request):
    user = request.user
    notes = user.note_set.get(id=id)
    serializer = NoteSerializer(notes, many=False)
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMyOneNote(request):
    user = request.user
    note = user.note_set.get(id=id)
    res={"body":note.body}
    return Response(res)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addNote(request):
    serializer = NoteSerializer(data=request.data)

    if( serializer.is_valid()):
        serializer.save()
    else:
        return Response("data was not saved, error ....")

    return Response("data was create")



    # user = request.user
    # print(user)
    # notes = user.note_set.all()
    # ps = user.pita_set.all()
    # print(ps)
    # serializer = NoteSerializer(notes, many=True)
    # return Response(serializer.data)
