# Latest Exchange Information System #

## DEMONSTRATION ##

first generate an api key by inserting the following url into postman:

`http://stark-hamlet-59828.herokuapp.com/api/v1/createkey`

once the new key is obtained in the same postman session go to:

`http://stark-hamlet-59828.herokuapp.com/api/v1/exchange`

and under the headers fields insert a new header:

`|Authorization | Api-Key <your key goes here>|`

try to do this request six times, the response should be throttled.

## Local installation for testing ##

from Project Root:

`$docker-compose build`

`$docker-compose up -d`

`$docker-compose exec web python manage.py migrate --noinput`

## Testing ##

`$docker-compose exec web python manage.py test`

