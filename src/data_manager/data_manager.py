"""
psycopg2 Data handler for the project.
psycopg2 documentation: https://www.psycopg.org/docs/
"""

from psycopg2.extras import RealDictCursor, RealDictRow

from src.data_manager import connection
from src.utils import make_new_timestamp


@connection.connection_handler
def video_exists(cursor: RealDictCursor, video_id: str) -> list:
    """Check if the video exists in the database"""
    query = """
        SELECT exists(
            SELECT True
            FROM videos
            WHERE video_id = %(video_id)s);
        """
    cursor.execute(query, {'video_id': video_id})
    return cursor.fetchone()


@connection.connection_handler
def user_already_rated(cursor: RealDictCursor, video_id: str, user_id: str) -> list:
    """Check if user already rated the video"""
    query = """
        SELECT exists(
            SELECT True
            FROM rating
            WHERE video_id = %(video_id)s AND user_id = %(user_id)s);
        """
    cursor.execute(query, {'video_id': video_id, 'user_id': user_id})
    return cursor.fetchone()


@connection.connection_handler
def get_avg_rating(cursor: RealDictCursor, video_id: str) -> list:
    """Returns average rating for a video"""
    query = """
        SELECT avg(rating)
        FROM rating
        WHERE video_id = %(video_id)s;
        """
    cursor.execute(query, {'video_id': video_id})
    return cursor.fetchone()


@connection.connection_handler
def insert_rating(cursor: RealDictCursor, video_id: str, user_id: str, rating: int) -> None:
    """Insert rating to the database"""
    query = """
        INSERT INTO rating (video_id, user_id, rating)
        VALUES (%(video_id)s, %(user_id)s, %(rating)s);
        UPDATE videos
        SET rating = (SELECT avg(rating)
                      FROM rating
                      WHERE video_id = %(video_id)s)
        WHERE video_id = %(video_id)s;
        """
    cursor.execute(query, {'video_id': video_id, 'user_id': user_id, 'rating': rating})


@connection.connection_handler
def update_rating_with_avg(cursor: RealDictCursor, video_id: str) -> None:
    """Update rating with average rating"""
    query = """
        UPDATE videos
        SET rating = (SELECT avg(rating)
                      FROM rating
                      WHERE video_id = %(video_id)s)
        WHERE video_id = %(video_id)s;
        """
    cursor.execute(query, {'video_id': video_id})


@connection.connection_handler
def get_all_videos(cursor: RealDictCursor) -> list:
    """Returns all videos from the database"""
    query = """
        SELECT id, video_id, title, author_name, fallback, user_id, submission_time, rating
        FROM videos
        ORDER BY submission_time DESC;
        """
    cursor.execute(query)
    return cursor.fetchall()


@connection.connection_handler
def get_top_users(cursor: RealDictCursor) -> list:
    """Returns all videos from the database"""
    query = """
        SELECT user_id, count(user_id) as video_count
        FROM videos
        GROUP BY user_id
        ORDER BY video_count DESC
        LIMIT 10;
        """
    cursor.execute(query)
    return cursor.fetchall()


@connection.connection_handler
def get_video_by_id(cursor: RealDictCursor, id: int) -> RealDictRow:
    """Returns videos from the database by id"""
    query = """
        SELECT id, video_id, title, author_name, fallback, user_id, submission_time, rating
        FROM videos
        WHERE id = %(id)s;
        """
    cursor.execute(query, {'id': id})
    return cursor.fetchone()


@connection.connection_handler
def get_video_by_video_id(cursor: RealDictCursor, video_id: int) -> RealDictRow:
    """Returns videos from the database by video_id"""
    query = """
        SELECT id, video_id, title, author_name, fallback, user_id, submission_time, rating
        FROM videos
        WHERE video_id = %(video_id)s;
        """
    cursor.execute(query, {'video_id': video_id})
    return cursor.fetchone()


@connection.connection_handler
def put_video_in_table(cursor: RealDictCursor, video_id: str, title: str, author_name: str, fallback: str,
                       user_id: str) -> None:
    """Put video in the database"""
    timestamp = make_new_timestamp()
    query = """
                INSERT INTO videos
                (video_id, title, author_name, fallback, user_id,  submission_time)
                VALUES (%(video_id)s, %(title)s, %(author_name)s, %(fallback)s, %(user_id)s, %(time)s)
                """
    cursor.execute(query, {'video_id': video_id, 'title': title, 'author_name': author_name, 'fallback': fallback,
                           'user_id': user_id, 'time': timestamp})
