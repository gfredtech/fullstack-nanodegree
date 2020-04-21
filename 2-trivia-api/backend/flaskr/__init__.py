import random
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    # Set up CORS. Allow '*' for origins.
    # Delete the sample route after completing the TODOs
    CORS(app)

    # Use the after_request decorator to set Access-Control-Allow
    @app.after_request
    def add_access_control(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'ContentType,Authorization, True')

        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,POST,PUT,DELETE,UPDATE,OPTIONS')

        return response

    # Create an endpoint to handle GET requests for all available categories.
    @app.route('/categories', methods=['GET'])
    def get_categories():
        categories = Category.query.order_by(Category.type).all()

        if len(categories) == 0:
            abort(404)

        return jsonify({'success': True, 'categories': {
            category.id: category.type for category in categories
        }})

    # Create an endpoint to handle GET requests for questions
    @app.route('/questions', methods=['GET'])
    def get_questions():
        all_questions = Question.query.order_by(Question.id).all()
        page = request.args.get('page', 1, type=int)

        # Setting start / end points based on static
        # QUESTIONS_PER_PAGE variable
        start = (page - 1) * QUESTIONS_PER_PAGE
        end = start + QUESTIONS_PER_PAGE

        # Applying pagination to incoming question set
        questions = [question.format() for question in all_questions]
        paginated_questions = questions[start:end]

        categories = Category.query.order_by(Category.type).all()

        if len(paginated_questions) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'questions': paginated_questions,
            'total_questions': len(all_questions),
            'categories': {category.id: category.type
                           for category in categories},
            'current_category': None
        })

    # Create an endpoint to DELETE question using a question ID.
    @app.route('/questions/<question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            question = Question.query.get(question_id)

            question.delete()

            return jsonify({
                'success': True,
                'deleted': question_id
            })
        except BaseException:
            abort(422)

    # Endpoint to POST new question
    @app.route('/questions', methods=['POST'])
    def create_question():

        body = request.get_json()
        question = body.get('question')
        answer = body.get('answer')
        difficulty = body.get('difficulty')
        category = body.get('category')

        if not (question and answer and difficulty and category):
            abort(422)

        try:
            new_question = Question(question=question,
                                    answer=answer,
                                    difficulty=difficulty,
                                    category=category)

            new_question.insert()

            return jsonify({
                'success': True,
                'created': new_question.id
            })

        except BaseException:
            abort(422)

    # POST endpoint to get questions based on search term
    @app.route('/questions/search', methods=['POST'])
    def search_questions():
        body = request.get_json()

        search_term = body.get('search_term')
        print(search_term)

        if search_term:
            search_results = Question.query.filter(
                Question.question.ilike(f'%{search_term}%')).all()

            return jsonify({
                'success': True,
                'questions': [question.format()
                              for question in search_results],
                'total_questions': len(search_results),
                'current_category': None
            })

        abort(404)

    # Get questions by category
    @app.route('/categories/<int:category_id>/questions', methods=['GET'])
    def get_category_questions(category_id):
        questions = Question.query.filter(
            Question.category == category_id).all()

        if len(questions) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'questions': [question.format() for question in questions],
            'total_questions': len(questions),
            'current_category': category_id
        })

    # POST endpoint to play quiz
    @app.route('/quiz', methods=['POST'])
    def play_quiz():

        try:
            # Getting body data from POST request
            body = request.get_json()

            # Ensuring data is present from POST request
            if not ('quiz_category' in body and 'previous_questions' in body):
                abort(422)

            # Pulling information from data body into respective variables
            category = body.get('quiz_category')
            previous_questions = body.get('previous_questions')

            # Defining behavior for what to return based on where a user is at
            # in their quiz
            if category['type'] == 'click':
                available_questions = Question.query.filter(
                    Question.id.notin_(previous_questions)).all()
            else:
                available_questions = Question.query.filter_by(
                    category=category['id']).filter(
                    Question.id.notin_(
                        previous_questions)).all()

            # Getting random question from list of available_questions
            new_question = available_questions[random.randrange(
                0, len(available_questions))].format() if \
                len(available_questions) > 0 else None

            # Returning successful information
            return jsonify({
                'success': True,
                'question': new_question
            })
        # Handling error scenarios
        except BaseException:
            abort(422)

    # Error handlers
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'Bad Request',
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Resource Not Found'
        }), 404

    @app.errorhandler(422)
    def unable_to_process(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'Unable to process request'
        }), 422

    @app.errorhandler(500)
    def unable_to_process(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'Internal Server Error'
        }), 500

    return app
