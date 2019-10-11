from flask_restful import reqparse

signin_parser = reqparse.RequestParser()
signin_parser.add_argument('username', type=str, required=True, help='this is your username')
signin_parser.add_argument('password', type=str, required=True, help='this is your password')

signup_parser = reqparse.RequestParser()
signup_parser.add_argument('username', type=str, required=True, help='this is your username')
signup_parser.add_argument('password', type=str, required=True, help='this is your password')

