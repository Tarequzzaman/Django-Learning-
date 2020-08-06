
<html>

<body>
<h2>MultipleDB</h2>
<br>
1. Deault <br>

2. another <br>

3. MongoDB<br>
   The source is found  <a href="https://bezkoder.com/django-mongodb-crud-rest-framework/">here</a>
   Steps: <br>

   - For mongodb we have to create an app **mongoDBWork**<br>

   - install djongo for MongoDB engine <br>

        ```
           pip install djongo
        ```
  

   - Add Db engine on setting.py<br>

        ```python
             DATABASES = {
                .
                .

                'mongo':{
                    "ENGINE": "djongo",
                    "NAME": "local",
                    'HOST': '127.0.0.1',
                    'PORT': 27017,
                }
             }
        ```
    - Since it is not default Database we Have to add DATABASE_ROUTERS for this DB<br>

        ```python 
           DATABASE_ROUTERS = ['otherdbapp.router.OtherAppDB',"mongoDBwork.router.MongoDBRouter"]
        ```
        Description of DATABASE_ROUTERS:<br>
        mongoDBwork : App Name<br>
        router : router.py file inser<br>
        MongoDBRouter: class name on the router.py file <br>
        Please have a look on router.py file <br>


    - Create a model name Posts <br>

    - migration <br>
        ```
            python manage.py makemigrations mongoDBwork
        ```
    - Migrate DB<br>
        ```
            python manage.py migrate --database=mongo  
        ```




<br>


<br>


<h2>Testcase: </h2>

<p>Unittest is very importent for CI/CD. Whenever you wirte a code you need to initaiate test case for this code</p>
<br>

<p>Below I have added some code for testing the views functions( get apis)</p>


1. urls.py for otherdbapp

```python

	urlpatterns = [
          #url(r'^admin/', admin.site.urls),
   	  url(r'create_user', create_user),
  	  url(r'get_user/', get_user),
	]
```
<br>
from the urls.py we can see there is two basic(not REST) apis path(create_user, get_user). Now we can move the views function these path

<br>
2.  The view function for these two url path are given here <strong>views.py</strong>


```python
def create_user(requests):
    try:
        first_name = requests.GET.get("first_name")
        last_name = requests.GET.get("last_name")
        phone =  requests.GET.get('phone')
        email = requests.GET.get('email')
        data = Users.objects.create(first_name= first_name, last_name= last_name, phone = phone, email = email)
        uuid = data.id
        return Response_data.success_response([{'id': uuid}])
    except Exception as E:
        return Response_data.failure_response("Something Went Wrong", str(E))



def get_user(requests):
    return Response_data.failure_response("Something Went Wrong", "")	

```

3. Now we can write testcase for these two functions   <strong>test.py</strong><br>


```python
class TestView(unittest.TestCase):
    def test_create_users(self):
        client = Client()
        response= client.get(reverse(create_user), {'first_name': 'john', 'last_name': 'smith', 'phone': "......", 'email': "/........."})
        self.assertEqual(response.status_code, 200)

    def test_get_user(self):
        client = Client()
        response= client.get(reverse(get_user))
        self.assertEqual(response.status_code, 450)
```

<h2>TokenAuthentication: </h2> 

I am trying to apply TokenAuthentication  on My an api  `http://127.0.0.1:8000/data/get_all_data/`.  The process is given here step by step:

1.  Install django rest framework
```
    pip install djangorestframework

```

2. Adding **rest_framework**  **'rest_framework.authtoken'** on my `INSTALLED_APPS`  py and `DEFAULT_AUTHENTICATION_CLASSES` inside the testDjango/settings.py

```
INSTALLED_APPS = [
   .
   .
   .
    
    'rest_framework',
    'rest_framework.authtoken',  # <-- Here


    .
    .
    .
]
```


```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',  # <-- And here
    ],
}
```

3. Then Run this command 

```
python manage.py migrate
python manage.py createsuperuser --username Tareq --email tareqcse12@gmail.com

```



4. For getting the user (Tareq) token we need to add some code on testDjango/urls.py 




```python

from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here


urlpatterns = [
  #url(r'^admin/', admin.site.urls),
     .
     .
     .
     path('api-token-auth/', obtain_auth_token, name='api_token_auth')
]
```

5. Call the api with username and password 


<center>
<img src="https://i.imgur.com/uaubFEO.png">
</center>





</body>
</html>





