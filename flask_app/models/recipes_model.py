from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app

class Recipes:
    db = 'recipes_db'

    def __init__( self, data ):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["id"]
        self.instructions = data["id"]
        self.date_name = data["id"]
        self.thirty_min = data["thirty_min"]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']

    @classmethod
    def get_all_by_user_id(cls, data):
        query = """select * from `recipes`
                    where users_id = %(id)s;"""
        result = connectToMySQL(cls.db).query_db(query, data)
        print(f'recipes: {result}')
        return result
    
    @classmethod
    def create(cls, data):
        print('creating recipe')
        query = """insert into `recipes` (name, description, instructions, date_name, thirty_min, users_id)
                    values (%(name)s, %(description)s, %(instructions)s, current_date(), %(thirty_min)s, %(users_id)s);"""
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def update(cls, data):
        query = ''
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def get_by_recipe_id(cls, data):
        query = """select * from recipes
                    where id = %(id)s;"""
        result = connectToMySQL(cls.db).query_db(query, data)
        print(f"result[0] = {result[0]}")
        return result[0]


