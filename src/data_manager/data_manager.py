from src.data_manager import connection
from src.utils import make_new_timestamp
from psycopg2.extras import RealDictCursor


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
    """Get average rating for a video"""
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
    """Get all videos from the database"""
    query = """
        SELECT id, video_id, user_id, submission_time, rating
        FROM videos
        ORDER BY submission_time DESC;
        """
    cursor.execute(query)
    return cursor.fetchall()


@connection.connection_handler
def put_video_in_table(cursor: RealDictCursor, video_id: str, user_id: str) -> None:
    """Put video in the database"""
    timestamp = make_new_timestamp()
    query = """
                INSERT INTO videos
                (video_id, user_id, submission_time)
                VALUES (%(video_id)s, %(user_id)s, %(time)s)
                """
    cursor.execute(query, {'video_id': video_id, 'user_id': user_id, 'time': timestamp})



