from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework import status
import json

class ProductApi(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        print ('\n')
        data=request.data
        datos=list(data.items()) 
        #json_data=json.loads(datos[0][0])
        
        print ('\n')
        mensage='{status: Error, aplicacion django}'
        try :   
            mensage='{status:OK}, \n'+str(datos[0])
            return Response(mensage, status=status.HTTP_200_OK)
        except:
            return Response( status=status.HTTP_422_UNPROCESSABLE_ENTITY) 
            
