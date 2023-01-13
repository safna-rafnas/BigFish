
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
# from myapp.serializers import productSerializer
# from myapp.models import products_db
# from django.shortcuts import get_list_or_404, get_object_or_404

# class product_create_list(APIView):
#     def get(self, request):
#         datas=products_db.objects.all()
#         serializer = productSerializer(datas,many=True)
#         return Response({'productdetails':serializer.data})

#     def post(self, request):
#         datas=request.data
#         print(type(datas))
#         serializer =productSerializer(data=datas)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class product_details(APIView):

#     def get_object(self, pk):
#         prodata = get_object_or_404(products_db, pk=pk)
#         return prodata

#     def get(self, request, pk):
#         prodata = self.get_object(pk)
#         serializer = productSerializer(prodata)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         prodata = self.get_object(pk)
#         serializer = productSerializer(prodata, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         prodata = self.get_object(pk)
#         prodata.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)