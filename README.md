# stilsoft-test
Test project built in Django, with user authentication and authorization. Supports different user roles with different access rights to API endpoints. 

For authorization
----------
JWT is used which is available with the indication of the username and password at:

> token/

# Requirements
The project was built in Django using the following requirements:

- rest_framework
- django_filters
- drf_yasg

Requests
----------
API endpoints support filter, sort and pagination queries, for example:
> api/routes/?route_type=bus

> api/routes/?ordering=number

> api/routes/?page=2

To the project added a swagger available at
----------
> swagger/