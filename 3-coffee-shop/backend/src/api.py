import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

'''
@TODO uncomment the following line to initialize the database
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''
# db_drop_and_create_all()

# ROUTES
'''
@TODO implement endpoint
    GET /drinks
'''


@app.route('/drinks', methods=['GET'])
def get_drinks():
    try:
        drinks = Drink.query.order_by(Drink.id).all()

        return jsonify({
            'success': True,
            'drinks': [drink.short() for drink in drinks]
        })
    except Exception as e:
        print(e)
        abort(404)


'''
@TODO implement endpoint
    GET /drinks-detail
'''


@app.route('/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def get_drinks_detail(jwt):
    try:
        drinks = Drink.query.order_by(Drink.id).all()

        return jsonify({
            'success': True,
            'drinks': [drink.long() for drink in drinks]
        })

    except Exception as e:
        print(e)
        abort(404)


'''
@TODO implement endpoint
    POST /drinks
'''


@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def post_new_drinks(jwt):
    body = request.get_json()

    if not ('title' in body and 'recipe' in body):
        print("body", body)
        abort(422)

    title = body.get('title')
    recipe = body.get('recipe')

    try:
        drink = Drink(
            title=title,
            recipe=json.dumps(recipe))

        drink.insert()

        return jsonify({
            'success': True,
            'drinks': [drink.long()]
        })

    except Exception as e:
        print(e)
        abort(422)


'''
@TODO implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
'''


@app.route('/drinks/<id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drink(jwt, id):
    drink = Drink.query.get(id)

    if drink:
        try:
            body = request.get_json()

            title = body.get('title')
            recipe = body.get('recipe')

            if title:
                drink.title = title
            if recipe:
                drink.recipe = json.dumps(recipe)

            drink.update()

            return jsonify({
                'success': True,
                'drinks': [drink.long()]
            })
        except Exception as e:
            print(e)
            abort(422)

    else:
        abort(404)


'''
@TODO implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id}
    where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks/<id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(jwt, id):
    drink = Drink.query.get(id)

    if drink:
        try:
            drink.delete()

            return jsonify({
                'success': True,
                'delete': id,
            })
        except Exception as e:
            print(e)
            abort(422)

    else:
        abort(404)


# Error Handling
'''
Example error handling for unprocessable entity
'''


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


'''
@TODO implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False,
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''

'''
@TODO implement error handler for 404
    error handler should conform to general task above
'''


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'error': 404,
        'message': 'not found',
    }), 404


'''
@TODO implement error handler for AuthError
    error handler should conform to general task above
'''


@app.errorhandler(AuthError)
def handle_auth_error(x):
    return jsonify({
        'success': False,
        'error': x.status_code,
        'message': x.error,
    })
