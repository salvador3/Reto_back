from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    id =serializers.CharField() 
    name= serializers.CharField(min_length=3, max_length=55)
    value=serializers.FloatField(max_value=99999.9, min_value=0)
    discount_value=serializers.FloatField( min_value=0)
    stock=serializers.IntegerField( min_value=1)
    
  
