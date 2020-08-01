
from django.contrib import admin
from django.urls import path
from ebdjango.views import ProductApi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/bulk_insert/', ProductApi.as_view(), name='api_create_product'),
]




#curl -d "{ products: [ { Product : {id_product:200 , name= galletas, value15, discount_value=1, stock=10}  }, { Product : {id_product:201 , name= tamales, value=10, discount_value=4, stock=100}  }, { Product : {id_product:202 , name= tacos, value=5, discount_value=2, stock=10}}, { Product : {id_product:203 , name= refresco, value15, discount_value100, stock=0} } ] }"  http://127.0.0.1:8000/api/products/bulk_insert/

#curl -d "{ products: [ { Product : {id_product:200 , name= galletas, value15, discount_value=1, stock=10}  }, { Product : {id_product:201 , name= tamales, value=10, discount_value=4, stock=100}  }, { Product : {id_product:202 , name= tacos, value=5, discount_value=2, stock=10}}, { Product : {id_product:203 , name= refresco, value15, discount_value100, stock=0} } ] }"  http://django-env.eba-s9tpphsy.us-west-2.elasticbeanstalk.com/api/products/bulk_insert/

#curl -d "{ products: [ { Product : {id_product:200 , name= galletas, value15, discount_value=1, stock=10}  }, { Product : {id_product:201 , name= tamales, value=10, discount_value=4, stock=100}  }, { Product : {id_product:202 , name= tacos, value=5, discount_value=2, stock=10}}, { Product : {id_product:203 , name= refresco, value15, discount_value100, stock=0} } ] }"  http://django-env.eba-8a3we8cm.us-east-2.elasticbeanstalk.com/api/products/bulk_insert/
