# TOKEN

Method: POST

URL: http://127.0.0.1:8000/api-auth/login/

Header:
~~~~
Accept application/json

Content-Type application/json
~~~~

Body:
~~~~
{
  "email": "durmusyasar3@gmail.com",
  "password": "doit2017"
}
~~~~

Sample Request:
~~~~
  curl --request POST \
  --url http://127.0.0.1:8000/api-auth/login/ \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --data '{
    "email": "durmusyasar3@gmail.com",
    "password": "doit2017"
  }'
~~~~

Response:
~~~~
{
  "auth_token": "91f4def1bee0d16730aef26879de74d10b7cad96"
}
~~~~












