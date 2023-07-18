from django.shortcuts import render
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from rest_framework import serializers,authentication,permissions
from cakeapi.serializers import UserSerializer,CakeSerializer
from myapp.models import Cake
from django.contrib.auth.models import User
from rest_framework.decorators import action


# class CakeSerializer(serializers.ModelSerializer):
#     id=serializers.CharField(read_only=True)
#     class Meta:
#         model=Cake
#         fields="__all__"
#         # exclude=("id",)


# class CakeView(ViewSet):
#     def list(self,request,*args,**kwargs):
#         qs=Cake.objects.all()
#         if "flavour" in request.query_params:
#             flav=request.query_params.get("flavour")
#             qs=qs.filter(flavour__iexact=flav)
#         if "shape" in request.query_params:
#             sh=request.query_params.get("shape")
#             qs=qs.filter(shape__iexact=sh)
#         if "price" in request.query_params:
#             pri=request.query_params.get("price")
#             qs=qs.filter(price=pri)
#         if "price_gt" in request.query_params:
#             pri=request.query_params.get("price_gt")
#             qs=qs.filter(price__gte=pri)
#         serializer=CakeSerializer(qs,many=True)
#         return Response(data=serializer.data)
    
#     def create(self,request,*args,**kwargs):
#         serializer=CakeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
        
    
#     def retrieve(self,request,*args,**kwargs):
#         id=kwargs.get("pk")
#         qs=Cake.objects.get(id=id)
#         serializer=CakeSerializer(qs)
#         return Response(data=serializer.data)
    
#     def update(self,request,*args,**kwargs):
#         id=kwargs.get("pk")
#         cake_obj=Cake.objects.get(id=id)
#         serializer=CakeSerializer(instance=cake_obj,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
        
    
#     def destroy(self,request,*args,**kwargs):
#         id=kwargs.get("pk")
#         try:
#             Cake.objects.get(id=id).delete()
#             return Response(data="deleted")
#         except Exception:
#             return Response(data="not found")
    

#     @action(methods=["get"],detail=False)
#     def flavour(self,request,*args,**kwargs):
#         qs=Cake.objects.all().values_list("flavour",flat=True).distinct()
#         return Response(data=qs)


class UsersView(ModelViewSet):
    model=User
    serializer_class=UserSerializer
    queryset=User.objects.all()


class CakesView(ModelViewSet):
    serializer_class=CakeSerializer
    queryset=Cake.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]


    def create(self, request, *args, **kwargs):
        serializer=CakeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)