from src.data_manager import connection
from src.utils import make_new_timestamp


@connection.connection_handler
def video_exists(cursor, video_id):
    query = """
        SELECT exists(
            SELECT True
            FROM videos
            WHERE video_id = %(video_id)s);
        """
    cursor.execute(query, {'video_id': video_id})
    return cursor.fetchone()


@connection.connection_handler
def get_all_videos(cursor):
    query = """
        SELECT id, video_id, user_id, submission_time, rating
        FROM videos
        ORDER BY submission_time DESC;
        """
    cursor.execute(query)
    return cursor.fetchall()


@connection.connection_handler
def put_video_in_table(cursor, video_id, user_id):
    timestamp = make_new_timestamp()
    query = """
                INSERT INTO videos
                (video_id, user_id, submission_time)
                VALUES (%(video_id)s, %(user_id)s, %(time)s)
                """
    cursor.execute(query, {'video_id': video_id, 'user_id': user_id, 'time': timestamp})



