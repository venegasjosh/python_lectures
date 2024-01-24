from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask_app.models import user_model


class Sighting:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.title = data['title']
        self.description = data['description']
        self.location = data['location']
        self.date_seen = data['date_seen']
        self.abducted = data['abducted']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # this method is for validating sightings entries
    @staticmethod
    def validate_sighting(sighting):
        is_valid = True

        if len(sighting['title']) < 3:
            flash("Title must be at least 3 characters long")
            is_valid = False
        if len(sighting['description']) < 10:
            flash("Description must be at least 3 characters long")
            is_valid = False
        if len(sighting['location']) < 3:
            flash("Location must be at least 3 characters long")
            is_valid = False
        if len(sighting['date_seen']) < 3:
            flash("Please enter in a valid date of sighting")
            is_valid = False

        return is_valid

    # CREATE One Sighting Method

    @classmethod
    def create_sighting(cls, data):
        query = '''
    INSERT INTO sightings (user_id, title, description, location, date_seen, abducted)
    VALUES (%(user_id)s, %(title)s, %(description)s, %(location)s, %(date_seen)s, %(abducted)s)
    '''
        results = connectToMySQL(DB).query_db(query, data)

        return results

    # READ ALL Sightings Method

    @classmethod
    def read_all_sightings(cls):
        query = '''
    SELECT * FROM sightings 
    JOIN  users 
    ON sightings.user_id = users.id;
    '''

        results = connectToMySQL(DB).query_db(query)

        all_sightings = []

        for row in results:
            sighting = cls(row)
            # **row reads through and makes a copy of each key value pair in the dictionary
            # user_data = {**row}

            creator_data = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }

            sighting.creator = user_model.User(creator_data)

            all_sightings.append(sighting)

        return all_sightings

    # READ ONE Sighting Method

    @classmethod
    def read_one_sighting(cls, data):

        query = " SELECT * FROM sightings WHERE id = %(id)s;"

        results = connectToMySQL(DB).query_db(query, data)
        print(results)

        return cls(results[0])

    # UPDATE Sighting

    @classmethod
    def update_sighting(cls, data):
        query = """
                UPDATE sightings 
                SET title=%(title)s, description=%(description)s,location=%(location)s, date_seen=%(date_seen)s, abducted=%(abducted)s 
                WHERE id = %(id)s;
                
            """

        results = connectToMySQL(DB).query_db(query, data)
        return results

  # DELETE Sighting
  
    @classmethod
    def delete_sighting(cls, data):
      query = "DELETE FROM sightings WHERE id = %(id)s"
      results = connectToMySQL(DB).query_db(query,data)
      
      if results == None:
        return "success"
      else:
        return "failure"