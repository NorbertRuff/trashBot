DROP TABLE IF EXISTS public.videos;
DROP TABLE IF EXISTS public.challenges;
DROP TABLE IF EXISTS public.rating;

DROP TYPE IF EXISTS challenge_status;
DROP TYPE IF EXISTS challenge_type;
DROP TYPE IF EXISTS challenge_title;


CREATE TABLE videos
(
    id              serial PRIMARY KEY                        NOT NULL,
    video_id        varchar(50)                               NOT NULL UNIQUE,
    title           varchar(100)                              NOT NULL,
    author_name     varchar(50)                               NOT NULL,
    fallback        varchar(100)                              NOT NULL,
    user_id         varchar(50)                               NOT NULL,
    rating          float4                      DEFAULT 0,
    submission_time timestamp without time zone DEFAULT now() NOT NULL
);

CREATE TABLE rating
(
    id       serial PRIMARY KEY NOT NULL,
    video_id varchar(50)        NOT NULL,
    user_id  varchar(50)        NOT NULL,
    rating   integer            NOT NULL
);


INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (2, 'aZqbekC7S7s', 'vicces riport', 'Varga Zoltán', 'vicces riport', 'U03QZB1P5NC', 0,
        '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (3, 'FjTCWLjuBzQ', 'Drunk Guy Goes For More Beer - FULL Version', 'almostamusingvideos',
        'Drunk Guy Goes For More Beer - FULL Version', 'U03QZB1P5NC', 0, '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (4, '-6FfHEXJJOE', 'VHS Kincsek - USA mókus dejópofa KOMMENTÁRRAL!', 'lifeofmatyi',
        'VHS Kincsek - USA mókus dejópofa KOMMENTÁRRAL!', 'U03QZB1P5NC', 0, '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (5, 'QAo_Ycocl1E', 'Africa', 'Toto - Topic', 'Africa', 'U03QZB1P5NC', 0, '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (6, 'D9-voINFkCg', 'Samir....You''re breaking the car!!!', 'Hive Funnies',
        'Samir....You''re breaking the car!!!', 'U03QZB1P5NC', 0, '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (7, 'ZswWnbQl_P4', 'Tough Wank', 'IskuriTube', 'Tough Wank', 'U03QZB1P5NC', 0, '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (8, '5a9KSmsIDxw', 'Tudd meg hogy mi vagyunk a Fidesz!', 'Ricky', 'Tudd meg hogy mi vagyunk a Fidesz!',
        'U03QZB1P5NC', 0, '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (9, 'hWKX2HrkfvA', 'Rugós beke legjobb pillanatok #1', 'ViCc MáNiA', 'Rugós beke legjobb pillanatok #1',
        'U03QZB1P5NC', 0, '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (10, 'Q8E4Byxy2_o', 'Rugós Beke - Himnusz (Teljes)', 'Geri Iski', 'Rugós Beke - Himnusz (Teljes)', 'U03QZB1P5NC',
        0, '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (11, 'xC03hmS1Brk', 'I Kill People', 'JonLajoie', 'I Kill People', 'U03QZB1P5NC', 0,
        '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (12, '-SQVH6zcI1c', 'How to drink whiskey like a sir MEME', 'PauLo', 'How to drink whiskey like a sir MEME',
        'U03QZB1P5NC', 0, '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (13, '23cjXModWpA', 'Cold Blooded Christmas', 'JonLajoie', 'Cold Blooded Christmas', 'U03QZB1P5NC', 0,
        '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (14, 'CXyjyYkUWLY', 'Damu Roland bekattan but it''s vocoded to gangsta''s paradise', 'Ádám Papp',
        'Damu Roland bekattan but it''s vocoded to gangsta''s paradise', 'U03QZB1P5NC', 0,
        '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (15, '1CWZZZ0-3UU', 'How To Tame a Wild Animal', 'HowToBasic', 'How To Tame a Wild Animal', 'U03QZB1P5NC', 0,
        '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (16, '3t678W5zfMA', 'How To Fix a Cracked iPhone Screen', 'HowToBasic', 'How To Fix a Cracked iPhone Screen',
        'U03QZB1P5NC', 0, '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (17, 'E77R0e5bzIs', 'Juice That Makes Your Head Explode', 'TomSka', 'Juice That Makes Your Head Explode',
        'U03QZB1P5NC', 0, '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (18, 'MlZBER_6Tik', 'The Kiffness X Opera Dog - Am I a Good Boi?', 'The Kiffness',
        'The Kiffness X Opera Dog - Am I a Good Boi?', 'U03QZB1P5NC', 0, '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (19, 'Iadu_P7zdhg', 'Firefighter fighting a marijuana fire - very funny', 'VeryFunnyVideoCenter',
        'Firefighter fighting a marijuana fire - very funny', 'U03QZB1P5NC', 0, '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (20, '8ZrQYEbmK88', 'Szögletes Üveggolyó - Ez egy Fa', 'toxicnagas', 'Szögletes Üveggolyó - Ez egy Fa',
        'U03QZB1P5NC', 0, '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (21, 'S5DRe4XoDbE', 'Timár Attila - Gyúrás | Szigorú a test', 'Arax塌煙',
        'Timár Attila - Gyúrás | Szigorú a test', 'U03QZB1P5NC', 0, '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (22, '2svOtXaD3gg', 'Home Stallone [DeepFake]', 'Ctrl Shift Face', 'Home Stallone [DeepFake]', 'U03QZB1P5NC', 0,
        '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (23, 'fnLMELJPHyM', 'Pálinkaivó verseny 2011 Baja', 'Tibor Antal', 'Pálinkaivó verseny 2011 Baja', 'U03QZB1P5NC',
        0, '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (24, '3ZWZ4YUiULg', 'Zolika női ruhában indulna dolgozni!😉😉😉', 'jános vörös',
        'Zolika női ruhában indulna dolgozni!😉😉😉', 'U03QZB1P5NC', 0, '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (25, '4_2ZRHmFg5o', 'Zolika sürű az anyag!', 'jános vörös', 'Zolika sürű az anyag!', 'U03QZB1P5NC', 0,
        '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (26, 'Mvq9U54Ij_U', '" HÁZIBULI "', 'arconporges', '" HÁZIBULI "', 'U03QZB1P5NC', 0,
        '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (27, 'VqvZ1o62lE0', 'Három autó összehasonlítása.wmv', 'Istvánné Gál', 'Három autó összehasonlítása.wmv',
        'U03QZB1P5NC', 0, '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (29, 'y5qe_tLI778', 'BEG - MASSZÍV #1', 'BEGfilm', 'BEG - MASSZÍV #1', 'U03QZB1P5NC', 0,
        '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (30, 'V7llzN-iP98', 'Ja, ék van alatta ?!', 'TheCivilera', 'Ja, ék van alatta ?!', 'U03QZB1P5NC', 0,
        '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (31, '2ft954vXPa4', 'in the deer 2nite', 'Josh Ballico', 'in the deer 2nite', 'U03QZB1P5NC', 0,
        '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (32, 'DSSB9KEzfK4', 'Best of Kathi Béla', 'MVP Paradox', 'Best of Kathi Béla', 'U03QZB1P5NC', 0,
        '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (33, 'i2gNx4-REIA', '“Daddy chill” “what the hell is even that”', 'Frequenzy Genji',
        '“Daddy chill” “what the hell is even that”', 'U03QZB1P5NC', 0, '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (34, '--Vaz9jW054', 'Speak the Hungarian Rapper', 'Peter Prince', 'Speak the Hungarian Rapper', 'U03QZB1P5NC', 0,
        '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (35, 'nkTwwHq4tVw', 'Disney paródiák: Micimackó (By:. Peti)', 'Radics Peti',
        'Disney paródiák: Micimackó (By:. Peti)', 'U03QZB1P5NC', 0, '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (36, 'nHP2VlA35ZA', 'Dolly Rambo - Porszívó', 'ironcopy', 'Dolly Rambo - Porszívó', 'U03QZB1P5NC', 0,
        '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (37, 'CqURMrUG0ek', 'Disney paródiák: Hófehérke (By:. Peti)', 'Radics Peti',
        'Disney paródiák: Hófehérke (By:. Peti)', 'U03QZB1P5NC', 0, '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (38, 'uzf5c1Ya2Sc', 'KAtɕAZSÍRRAL?! Ki étkezik zsírosabban, férfiasabban, MAGYARosabban? Bayer vs. Sziszi',
        'János Egressy', 'KAtɕAZSÍRRAL?! Ki étkezik zsírosabban, férfiasabban, MAGYARosabban? Bayer vs. Sziszi',
        'U03QZB1P5NC', 0, '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (39, 'q-rZqdWvGpo', 'PPAP-Hungarian parody', 'MrGabelot', 'PPAP-Hungarian parody', 'U03QZB1P5NC', 0,
        '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (40, 'PQSCQ9FamRw', 'Fekete Pákó - Tart még tart a party (Official Video)', 'Fekete Pákó Online',
        'Fekete Pákó - Tart még tart a party (Official Video)', 'U03QZB1P5NC', 0, '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (41, 'GJeJVOkHC4U', 'Matisz Nagypapa', 'effigggy', 'Matisz Nagypapa', 'U03QZB1P5NC', 0,
        '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (42, 'ntfNGPDIG00', 'AC DC - Irígyeim Sokan Vagytok (mashup)', 'Pentium 040',
        'AC DC - Irígyeim Sokan Vagytok (mashup)', 'U03QZB1P5NC', 0, '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (43, 'cFXpQ3LVpkY', 'Egs - Ki Ez A Bolond (Prod. b3ncs1)', 'Dodzsem Klub', 'Egs - Ki Ez A Bolond (Prod. b3ncs1)',
        'U03QZB1P5NC', 0, '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (1, 'me5rX7Y9XKU', 'Sad Ending - Cyanide & Happiness Shorts', 'ExplosmEntertainment',
        'Sad Ending - Cyanide & Happiness Shorts', 'U03QZB1P5NC', 3.7, '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (44, 'LZAFo4jXhW0', 'Look at my horse + lyrics [HD]', 'viafiur22301', 'Look at my horse + lyrics [HD]',
        'U03QZB1P5NC', 5, '2022-09-29 16:02:00.289836');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (47, 'TKjJEAVRYAw', 'Fiets Opa Bike Repair What No Money ? Remaster HQ !!!', 'MrLalzor',
        'Fiets Opa Bike Repair What No Money ? Remaster HQ !!!', 'U03NFE52CDU', 0, '2022-11-17 12:57:43.709700');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (48, 'l3qSdWBXQ_M', 'nagymeleghez (animatik)', 'Turai Balázs', 'nagymeleghez (animatik)', 'U03NFE52CDU', 0,
        '2022-11-23 08:33:13.992445');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (49, 'tHLgqfhDFWc', 'HIHETETLEN, ÚJ BOTRÁNY, Cristofel becsicskítja SP-t és Fluort, az új klipje miatt!',
        'Bánk Csutorás', 'HIHETETLEN, ÚJ BOTRÁNY, Cristofel becsicskítja SP-t és Fluort, az új klipje miatt!',
        'U03NFE52CDU', 0, '2022-11-23 08:36:30.092356');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (28, 'DRIhQU0z6es', 'Madam X-otic - Riói szerelem 1.', 'Csibecsabax Mister', 'Madam X-otic - Riói szerelem 1.',
        'U03QZB1P5NC', 4, '2022-09-29 15:51:13.769167');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (46, 'zTcRlfKJgzA', 'MC Isti -  ÍGY ÉL KŐRÖSKÉNYI ISTVÀN VALÓJÀBAN ❗', 'MC Isti (FLACO)',
        'MC Isti -  ÍGY ÉL KŐRÖSKÉNYI ISTVÀN VALÓJÀBAN ❗', 'U045TS1LAGK', 0, '2022-11-16 08:44:14.670984');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (50, 'SZMzh8uDJEc', 'Soerii & Poolek : Tanga (Official Music Video)', 'soeriipoolek',
        'Soerii & Poolek : Tanga (Official Music Video)', 'U03NFE52CDU', 0, '2022-12-03 06:34:41.977773');
INSERT INTO public.videos (id, video_id, title, author_name, fallback, user_id, rating, submission_time)
VALUES (51, 'bNYnVoxu_kA', 'Commando Scientists', 'TheAtomicWaffle', 'Commando Scientists', 'U03NFE52CDU', 0,
        '2023-02-07 21:30:05.834542');



create type challenge_status as enum ('pending', 'approved', 'rejected', 'completed');

create type challenge_type as enum ('picture', 'text');

create type challenge_title as enum (
    'Blast from the past',
    'The best of the best',
    'The worst of the worst',
    'Get to know each other',
    'Pure fantasy',
    'Weird and wonderful',
    'History lesson',
    'Hidden talent',
    'Hidden treasure',
    'First date questions',
    'Undefinable'
    );


CREATE TABLE challenges
(
    id              serial PRIMARY KEY                                NOT NULL,
    title           challenge_title             DEFAULT 'Undefinable' NOT NULL,
    type            challenge_type              DEFAULT 'text'        NOT NULL,
    challenge       text                                              NOT NULL,
    user_id         varchar(50)                                       NOT NULL,
    status          challenge_status            DEFAULT 'pending'     NOT NULL,
    submission_time timestamp without time zone DEFAULT now()         NOT NULL
);


INSERT INTO challenges (title, type, challenge, user_id, status)
VALUES ('Blast from the past', 'picture',
        'Post a picture about yourself in this thread that was taken at least 10 years ago!', 'U03QZB1P5NC',
        'approved'),
       ('The best of the best', 'picture',
        'What is the best thing you have ever eaten? Post a picture about it in the thread!', 'U03QZB1P5NC',
        'approved'),
       ('The worst of the worst', 'picture',
        'Share a picture of your most embarrassing hairstyle or clothes from the past!',
        'U03QZB1P5NC', 'approved'),
       ('Weird and wonderful', 'text', 'Share a picture of the most ridiculous thing you have ever purchased?',
        'U03QZB1P5NC', 'approved'),
       ('Blast from the past', 'picture',
        'Post a picture in this thread about yourself that was taken at least 20 years ago!', 'U03QZB1P5NC',
        'approved'),
       ('The worst of the worst', 'picture', 'Share a picture of the weirdest food combination you ever eaten!',
        'U03QZB1P5NC', 'approved'),
       ('Get to know each other', 'text', 'What was your favorite childhood game or activity?',
        'U03QZB1P5NC', 'approved'),
       ('Get to know each other', 'picture', 'Share your favorite meme!', 'U03QZB1P5NC', 'approved'),
       ('Undefinable', 'picture', 'Share your favorite meme!', 'U03QZB1P5NC', 'approved'),
       ('The best of the best', 'picture',
        'Share a picture of the most beautiful natural landscape you''ve ever visited!', 'U03QZB1P5NC', 'approved'),
       ('Weird and wonderful', 'picture', 'Share a picture of the most unusual item in your house!', 'U03QZB1P5NC',
        'approved'),
       ('Pure fantasy', 'text', 'If you could have any talent or skill (real or fictional), what would it be and why?',
        'U03QZB1P5NC', 'approved'),
       ('First date questions', 'text', 'If you could be any character in history, who would you choose and why?',
        'U03QZB1P5NC', 'approved'),
       ('First date questions', 'text',
        'If you could live in any fictional universe, which one would you choose and why?', 'U03QZB1P5NC', 'approved'),
       ('First date questions', 'text',
        'If you could be any character from a video game, or movie, who would you choose and why?', 'U03QZB1P5NC',
        'approved'),
       ('First date questions', 'text', 'If you could live in any era of history, which one would you choose and why?',
        'U03QZB1P5NC', 'approved'),
       ('First date questions', 'text',
        'If you could live in any TV show or movie universe, which one would you choose and why?', 'U03QZB1P5NC',
        'approved'),
       ('First date questions', 'text',
        'If you could have any job in the world (regardless of qualifications), what would it be and why?',
        'U03QZB1P5NC', 'approved'),
       ('Blast from the past', 'picture', 'Post a picture about yourself in this thread that was taken
       between 2000 and 2010!', 'U03QZB1P5NC', 'approved'),
       ('Blast from the past', 'picture', 'Post a picture about yourself in this thread that was taken
       between 2010 and 2020!', 'U03QZB1P5NC', 'approved'),
       ('Hidden talent', 'picture', 'Post a picture that was taken at a party!', 'U03QZB1P5NC', 'approved'),
       ('Hidden talent', 'text', 'What is your hidden superpower?', 'U03QZB1P5NC', 'approved');
