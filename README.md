# Reto_back

Autor: Rafael Robles

Para el uso aplicación se hará por un curl de la siguiente forma:

curl -d "data"   http://django-env.eba-8a3we8cm.us-east-2.elasticbeanstalk.com/api/products/bulk_insert/

Donde cambiamos “data”, por el json que contiene la lista de productos, como sigue:

curl -d "{ products: [ { Product : {id_product:200 , name= galletas, value15, discount_value=1, stock=10}  }, { Product : {id_product:202 , name= tacos, value=5, discount_value=2, stock=10}}, { Product : {id_product:203 , name= refresco, value15, discount_value100, stock=0} } ] }"  http://django-env.eba-8a3we8cm.us-east-2.elasticbeanstalk.com/api/products/bulk_insert/

Como resultado simplemente regresa el json que le fue mandado si está bien formado, en caso contrario regresa 422.

Además el repositorio incluye el comprimido en django_desarrollo.zip que son los archivos necesarios para crear e implementar la aplicación en la plataforma aws elastic beanstalk, en un ambiente de aplicación web. 

También se encuentra otro comprimido que es una aplicación simple de django. Se agrega el ambiente virtual de python para verificar la configuración inicial. 

En el entorno usado de aws elastic beanstalk, se encuentra dentro de la capa gratuita que brinda la plataforma.
