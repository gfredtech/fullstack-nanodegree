# Casting Agency Capstone Project

This is my final capstone project for Udacity's FullStack Web Developer Nanodegree.
Web app can be accessed at [here](https://flaskcasting.herokuapp.com)

##### Project Dependencies
* __Flask__ - Slim python web library.
* __SQLAlchemy__ - Python ORM library
* __Heroku__ - PaaS platform for easy hosting of web apps
* __Postman__ - API testing tool

### Installation instructions
* Clone project to directory of your choice.
* Create a virtualenv in project directory
* run ```pip install -r requirements.txt``` to install project dependencies
* add ```DATABASE_URL``` to environment variables of your system. 
On Unix systems, use ```export DATABASE_URL={username}:{password}@{host}:{port}/{database_name}```
* run ```export FLASK_APP=app.py```
* type ```flask run``` in terminal

###Endpoints:
* GET /actors and /movies
* DELETE /actors/ and /movies/
* POST /actors and /movies and
* PATCH /actors/ and /movies/

### Roles
* Casting Assistant
    * GET /actors and /movies

* Casting Director
    * GET /actors and /movies
    * ADD /actors and DELETE /actors
    * PATCH /actors and /movies
    
* Executive Producer
    * GET /actors and /movies
    * ADD /actors and DELETE /actors
    * PATCH /actors and /movies
    * ADD /movies and DELETE /movies


### JWT Tokens for each role:
* Casting Assistant - ```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVPcHlkUXpPRFVjTUFIYjBtSmp5QyJ9.eyJpc3MiOiJodHRwczovL2dmcmVkLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZTg5YWY4ZDY1OTUxMTBjMTBjZGUxNTQiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTg3MDMyNjc4LCJleHAiOjE1ODcxMTkwNzcsImF6cCI6IlEzUHJVMWh6UUJJSjdEMFhjUXA0eUttN041dnJOV2pBIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.GxEMs2BKww191P5GfY0xmlht7wW0ShulDbrFxc4vJ4leN7tbyqAvYLv_1KFLLxmI21_TAws78cc0_-nx6FzKegy_FpSVOhVbKPsZwPXvXX2rnZUPmUSwegOfFA238cQlH9fVK-1s03TuyjogD5kgH5LWMK7AffylCI1c0dXhoaG1-1v3uj_fqVN5frPvATPOY2ft0xriGS7vdkjPFmodiUNBAc1sPrwfoJp9qhQHgpkz6h_zzhAxLPpDp5kBkakW-eJGMnVpbBZBd199lvV3AA9D1FaIJQ4G1EsY0APRUAwBze6m2vjT3FCJY5Ef5bZGWJMXJOl5O_1r20LqhkStfQ```

* Casting Director- ```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVPcHlkUXpPRFVjTUFIYjBtSmp5QyJ9.eyJpc3MiOiJodHRwczovL2dmcmVkLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZTg5YzgxZjg1ZGQ5ODBjNjhlMzA0MmYiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTg3MDMyNzQ3LCJleHAiOjE1ODcxMTkxNDYsImF6cCI6IlEzUHJVMWh6UUJJSjdEMFhjUXA0eUttN041dnJOV2pBIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJhZGQ6YWN0b3JzIiwiZGVsZXRlOmFjdG9ycyIsInVwZGF0ZTphY3RvcnMiLCJ1cGRhdGU6bW92aWVzIiwidmlldzphY3RvcnMiLCJ2aWV3Om1vdmllcyJdfQ.B9A7vWXbJOg6KY1hBf2sczrqdyD8Ue0_zrqgdEbhS_LMtbBnpbqDudtOM0CJ_yd5pGMPK6lJDbiKKSRxgDyYl0XsHOsh6Za3aXXo14Xp_8zSTrI2B9mbbhRURxo6xK2uDJ6FfsV6e35HaWHWZxqYRikO0vRveTGmRWJu7I7PNjr1AO1YuAHQI5vkrCvWimThx8Awf99qUaja28CyWRwywg1OUxVVA33DND9PFazmfIZQNQbP0KjHIL8UwN-aLUpNJI7hHSqM1W1GLSqyOgzZj7Drhas54KDtUWnoyWyR8OfKV9wKEPkVZ_Gv81s9ILm42PPL_Q472JgSESnmWUEQbA```

* Executive Producer - ```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVPcHlkUXpPRFVjTUFIYjBtSmp5QyJ9.eyJpc3MiOiJodHRwczovL2dmcmVkLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZThhNTBlNTg1ZGQ5ODBjNjhlNWFmZjAiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTg3MDMyODIwLCJleHAiOjE1ODcxMTkyMTksImF6cCI6IlEzUHJVMWh6UUJJSjdEMFhjUXA0eUttN041dnJOV2pBIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJhZGQ6YWN0b3JzIiwiYWRkOm1vdmllcyIsImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.YOm5uNPiWbhqdt0ZD1czu9PLT4SlaqF8lWzj1Cdp_3LrPLD2JVIZbphE4z8X9iM2Afdz1GnG_Bclhz5O5TvrnvRILc2I83yX2p3nPZhPiUt-T-qdGfP0BPAqxaTaKRDSd-wXtW_aTgb0NbaLyOFXOgIQDW2or0rpiEoLEdL1Bn9oQhxW947ZUdwCtkd_ThOC2gVRREPgTB-bO_4h7EwqQJAnJVHmyHVtsM9v3s_jk48cb7M1T9N_zlGuq7NWK8wAwzwkPnKd7b7W9oVIm7XhTA3J3eMjVetKR0j6pkVkLKjZU4tOBmqnV-CJ6uN3s_xGJuxMsXKEqUedIrswixvpmw```

## API Endpoints

In the next few subsections, we'll cover how the API works and what you can expect back in the results.

### Default Path

#### GET /
Verifies that application is up and running on Heroku.

Sample response:
```
{
    "description": "App is running.",
    "success": true
}
```

### GET Endpoints

#### GET /movies
Displays all movies listed in the database.

Sample response:
```
{
    "movies": [
        {
            "id": 3,
            "release_year": 2008,
            "title": "Movie 3"
        },
        {
            "id": 4,
            "release_year": 1973,
            "title": "Movie 4"
        },
    ],
    "success": true
}
```

#### GET /actors
Displays all actors / actresses listed in the database.

Sample response:
```
{
    "actors": [
        {
            "age": 34,
            "gender": "female",
            "id": 3,
            "movie_id": 2,
            "name": "Actor 3"
        },
        {
            "age": 34,
            "gender": "male",
            "id": 4,
            "movie_id": 3,
            "name": "Actor 4"
        },
    ],
    "success": true
}
```

### POST Endpoints

#### POST /movies/create
Creates a new movie entry in the database.

Sample response:
```
{
    "movie_id": 8,
    "success": true
}
```

#### POST /actors/create
Creates a new actor / actress entry in the database.

Sample response:
```
{
    "actor_id": 7,
    "success": true
}
```

### PATCH Endpoints

#### PATCH /movies/update/<movie_id>
Updates movie information given a movie_id and newly updated attribute info.

Sample response:
```
{
    "movie_id": 2,
    "success": true
}
```

#### PATCH /actors/update/<actor_id>
Updates actor information given a actor_id and newly updated attribute info.

Sample response:
```
{
    "actor_id": 2,
    "success": true
}
```

### DELETE Endpoints

#### DELETE /movies/delete/<movie_id>
Deletes a movie entry from the database given the inputted movie_id.

Sample response:
```
{
    "deleted": 1,
    "success": true
}
```

#### DELETE /movies/actors/<actor_id>
Deletes an actor / actress entry from the database given the inputted actor_id.

Sample response:
```
{
    "deleted": 1,
    "success": true
}
```
