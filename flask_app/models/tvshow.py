from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE

class Tvshow:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.network = data['network']
        self.release_date = data['release_date']
        self.description = data['description']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    # validate tv show inputs 
    @staticmethod
    def validate_tvshow( tvshow ):
        is_valid = True
        # test whether a field matches the pattern
        if len(tvshow['title']) < 3:
            flash("Title must be at least 3 characters!","tvshow")
            is_valid = False
        if len(tvshow['network']) < 3:
            flash("Network must be at least 3 characters!","tvshow")
            is_valid = False
        if len(tvshow['description']) < 3:
            flash("Description must be at least 3 characters!","tvshow")
            is_valid = False
        if len(tvshow['release_date']) < 1:
            flash("Invalid Date !","tvshow")
            is_valid = False    
        return is_valid
    
    # get all tv shows created by all users
    @classmethod
    def get_all_tvshows(cls):
        query = "SELECT * FROM tvshows;"
        results = connectToMySQL(DATABASE).query_db(query)
        return results
    
    # get one tv show by id
    @classmethod
    def get_one_tvshow(cls,data):
        query = "SELECT * FROM tvshows WHERE id=%(id)s"
        result = connectToMySQL(DATABASE).query_db(query,data)
        if result:
           return cls(result[0])
        return result
       
    # create tv show    
    @classmethod
    def save_tvshow(cls, data ):
        query = "INSERT INTO tvshows ( title, network, release_date, description, user_id, created_at, updated_at ) VALUES ( %(title)s, %(network)s, %(release_date)s ,%(description)s, %(user_id)s, NOW(), NOW() );"
        return connectToMySQL(DATABASE).query_db( query, data )        

    # delete tv show
    @classmethod
    def delete_tvshow(cls,data):
        # query="DELETE t1, t2 FROM tvshows t1 LEFT JOIN likes t2 ON t1.id = t2.tvshow_id WHERE t1.id = %(id)s AND (t2.tvshow_id = %(id)s OR t2.tvshow_id IS NULL);"
        query="DELETE FROM likes WHERE tvshow_id =  %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        query="DELETE FROM tvshows WHERE tvshows.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        return results
    
    # update tv show
    @classmethod
    def update_tvshow(cls,data):
        query = "update tvshows set title=%(title)s, network=%(network)s, release_date=%(release_date)s, description=%(description)s where id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        return results
    
    # create likes table
    @classmethod
    def tvshow_like(cls,data):
        query = "INSERT INTO likes (user_id, tvshow_id) SELECT %(user_id)s, %(tvshow_id)s WHERE NOT EXISTS (SELECT * FROM likes WHERE user_id =%(user_id)s  and tvshow_id=%(tvshow_id)s );"
        results = connectToMySQL(DATABASE).query_db(query,data)
          
        return results
    
    # if unlike delete row id=tvshow_id from likes table
    @classmethod
    def tvshow_unlike(cls,data):
        query = "delete from likes where (user_id = %(user_id)s and tvshow_id = %(tvshow_id)s);"
        results = connectToMySQL(DATABASE).query_db(query,data)
        return results
    
    # select all user liked tvshows
    @classmethod
    def get_all_user_likes(cls,data):
        query = "SELECT * FROM likes where user_id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        likes_list=[]
        for like in results:
            likes_list.append(like['tvshow_id'])
        return likes_list
    
    # count the number of like(s) for a tvshow
    @classmethod
    def get_number_of_likes(cls,data):
        query = "select count(*) as nb_likes from likes  where tvshow_id=%(id)s group by tvshow_id ;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results) < 1:
           return results 
        return results[0]
    
    
    
    