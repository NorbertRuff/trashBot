"""
psycopg2 Data handler for the project.
psycopg2 documentation: https://www.psycopg.org/docs/
"""

from enum import Enum

from psycopg2.extras import RealDictCursor, RealDictRow

from src.data_manager import connection
from src.utils import make_new_timestamp


class ChallengeCategory(Enum):
    """Enum for challenge category"""
    BLAST_FROM_THE_PAST = "Blast from the past"
    THE_BEST_OF_THE_BEST = "The best of the best"
    THE_WORST_OF_THE_WORST = "The worst of the worst"
    GET_TO_KNOW_EACH_OTHER = "Get to know each other"
    PURE_FANTASY = "Pure fantasy"
    WEIRD_AND_WONDERFUL = "Weird and wonderful"
    HISTORY_LESSON = "History lesson"
    HIDDEN_TALENT = "Hidden talent"
    HIDDEN_TREASURE = "Hidden treasure"
    FIRST_DATE_QUESTIONS = "First date questions"
    UNDEFINABLE = "Undefinable"


class ChallengeType(Enum):
    """Enum for challenge type"""
    TEXT = "text"
    PICTURE = "picture"


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
        ORDER BY video_count DESC;
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


@connection.connection_handler
def get_random_challenge(cursor: RealDictCursor) -> RealDictRow:
    """Returns a random challenge that has approved status"""
    query = """
        SELECT *
        FROM challenges
        WHERE status = 'approved'
        OFFSET random() * (select count(*) from challenges)
            limit 1
        """
    cursor.execute(query)
    return cursor.fetchone()


@connection.connection_handler
def update_challenge_status(cursor: RealDictCursor, challenge_id: int, status: str) -> None:
    """Update challenge status"""
    query = """
        UPDATE challenges
        SET status = %(status)s
        WHERE id = %(challenge_id)s;
        """
    cursor.execute(query, {'challenge_id': challenge_id, 'status': status})


@connection.connection_handler
def add_challenge(cursor: RealDictCursor, challenge_type: str, challenge_category: str, challenge_text: str,
                  user_id: str) -> None:
    """Add challenge to the database with pending status"""
    query = """
        INSERT INTO challenges (type, title, challenge, status, user_id)
        VALUES (%(challenge_type)s, %(challenge_category)s, %(challenge_text)s, 'pending', %(user_id)s);
        """
    cursor.execute(query, {'challenge_type': challenge_type, 'challenge_category': challenge_category,
                           'challenge_text': challenge_text, 'user_id': user_id})
