# API Development in Django and Rest framework
this is an api with multiple endpoints allowing GET, POST, PUT, DELETE options.
which by default interact with an SQLITE database

## What does it consist of ?
The API has Login and Logout endpoints which allow the client to use it to create a user who will be granted a token, which will serve as authentication to verify if a user exists and if that user is active, that is, it has a token. .

then that user will be allowed to access and interact with the other endpoints or routes such as entering, listing, updating and deleting products

## Documentation route of the endpoints and nodels that have the API
A documentation interface with a very intuitive swagger library has been included

```zsh
http://localhost:8000/swagger/
```
![Captura desde 2023-01-31 19-16-14](https://user-images.githubusercontent.com/105228140/215913770-1111cdf3-0268-45f3-96d9-47b3d6151f43.png)

Once inside the swagger interface you will be able to see all the endpoints and methods allowed in each endpoint

- Important, 
If you have changed the access port 8000 to something else then be sure to change the port to the one you have specified.
