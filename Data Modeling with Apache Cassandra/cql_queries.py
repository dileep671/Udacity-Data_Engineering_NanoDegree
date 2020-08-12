
# Drop table queries
artist_song_info_drop = """DROP TABLE IF EXISTS artist_song_info;"""

song_user_info_drop = """DROP TABLE IF EXISTS song_user_info;"""

user_song_history_drop = """DROP TABLE IF EXISTS user_song_history;"""


# Create table queries
artist_song_info_create = (
"""
CREATE TABLE IF NOT EXISTS artist_song_info (
                                    session_id INT,
                                    item_in_session INT,
                                    artist_name VARCHAR,
                                    song_title VARCHAR,
                                    song_duration DECIMAL,
                                    PRIMARY KEY(session_id, item_in_session)
                                    );
""")

song_user_info_create = (
"""
CREATE TABLE IF NOT EXISTS song_user_info (
                                    user_id INT,
                                    session_id INT,
                                    item_in_session INT,
                                    artist_name VARCHAR,
                                    song_title VARCHAR,
                                    user_first_name VARCHAR,
                                    user_last_name VARCHAR,
                                    PRIMARY KEY(user_id, session_id,item_in_session)
                                    );
""")

user_song_history_create = (
"""
CREATE TABLE IF NOT EXISTS user_song_history (
                                    song_title VARCHAR,
                                    user_id INT,
                                    user_first_name VARCHAR,
                                    user_last_name VARCHAR,
                                    PRIMARY KEY(song_title, user_id)
                                    );
""")


# INSERT QUERIES
artist_song_info_insert = ("""
INSERT INTO artist_song_info (
                     session_id,
                     item_in_session,
                     artist_name,
                     song_title,
                     song_duration)
VALUES (
        %(session_id)s,
        %(item_in_session)s,
        %(artist_name)s,
        %(song_title)s,
        %(song_duration)s
        );
""")

song_user_info_insert = ("""
INSERT INTO song_in_user (
                     user_id,
                     session_id,
                     item_in_session,
                     artist_name,
                     song_title,
                     user_first_name,
                     user_last_name)
VALUES (
        %(user_id)s,
        %(session_id)s,
        %(item_in_session)s,
        %(artist_name)s,
        %(song_title)s,
        %(user_first_name)s,
        %(user_last_name)s
        );
""")

user_song_history_insert = ("""
INSERT INTO user_in_song (
                     song_title,
                     user_id,
                     user_first_name,
                     user_last_name)
VALUES (
        %(song_title)s,
        %(user_id)s,
        %(user_first_name)s,
        %(user_last_name)s
        );
""")


# SELECT QUERIES
QUERY_1_SELECT = ("""
SELECT artist_name,
       song_title,
       song_duration
  FROM artist_song_info
 WHERE session_id=338
   AND item_in_session=4;
""")

QUERY_2_SELECT = ("""
SELECT artist_name,
       song_title,
       user_first_name,
       user_last_name
  FROM song_user_info
 WHERE user_id=10
   AND session_id=182;
""")

QUERY_3_SELECT = ("""
SELECT user_first_name,
       user_last_name
  FROM user_song_history
 WHERE song_title = 'All Hands Against His Own';
""")


drop_table_queries = [artist_song_info_drop, song_user_info_drop, user_song_history_drop]

create_table_queries = [artist_song_info_create, song_user_info_create, user_song_history_create]

select_table_queries = [QUERY_1_SELECT, QUERY_2_SELECT, QUERY_3_SELECT]

insert_table_queries = [artist_song_info_insert, song_user_info_insert, user_song_history_insert]