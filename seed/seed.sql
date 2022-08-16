DROP TABLE IF EXISTS public.videos;
CREATE TABLE videos
(
    id              serial                                    NOT NULL,
    video_id        varchar(50)                               NOT NULL UNIQUE,
    user_id         varchar(50)                               NOT NULL,
    rating          integer                     DEFAULT 0,
    submission_time timestamp without time zone DEFAULT now() NOT NULL
);

INSERT INTO videos (video_id, user_id)
VALUES ('me5rX7Y9XKU', 'U03QZB1P5NC'),
       ('aZqbekC7S7s', 'U03QZB1P5NC'),
       ('FjTCWLjuBzQ', 'U03QZB1P5NC'),
       ('-6FfHEXJJOE', 'U03QZB1P5NC'),
       ('QAo_Ycocl1E', 'U03QZB1P5NC'),
       ('D9-voINFkCg', 'U03QZB1P5NC'),
       ('ZswWnbQl_P4', 'U03QZB1P5NC'),
       ('5a9KSmsIDxw', 'U03QZB1P5NC'),
       ('hWKX2HrkfvA', 'U03QZB1P5NC'),
       ('Q8E4Byxy2_o', 'U03QZB1P5NC'),
       ('xC03hmS1Brk', 'U03QZB1P5NC'),
       ('-SQVH6zcI1c', 'U03QZB1P5NC'),
       ('23cjXModWpA', 'U03QZB1P5NC'),
       ('CXyjyYkUWLY', 'U03QZB1P5NC'),
       ('1CWZZZ0-3UU', 'U03QZB1P5NC'),
       ('3t678W5zfMA', 'U03QZB1P5NC'),
       ('E77R0e5bzIs', 'U03QZB1P5NC'),
       ('MlZBER_6Tik', 'U03QZB1P5NC'),
       ('Iadu_P7zdhg', 'U03QZB1P5NC'),
       ('8ZrQYEbmK88', 'U03QZB1P5NC'),
       ('S5DRe4XoDbE', 'U03QZB1P5NC'),
       ('2svOtXaD3gg', 'U03QZB1P5NC'),
       ('fnLMELJPHyM', 'U03QZB1P5NC');