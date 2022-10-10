DROP TABLE IF EXISTS public.videos;
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

DROP TABLE IF EXISTS public.rating;
CREATE TABLE rating
(
    id       serial PRIMARY KEY NOT NULL,
    video_id varchar(50)        NOT NULL,
    user_id  varchar(50)        NOT NULL,
    rating   integer            NOT NULL
);


INSERT INTO videos (video_id, title, author_name, fallback, user_id)
VALUES ('me5rX7Y9XKU', 'Sad Ending - Cyanide & Happiness Shorts', 'ExplosmEntertainment',
        'Sad Ending - Cyanide & Happiness Shorts', 'U03QZB1P5NC'),
       ('aZqbekC7S7s', 'vicces riport', 'Varga Zoltán', 'vicces riport', 'U03QZB1P5NC'),
       ('FjTCWLjuBzQ', 'Drunk Guy Goes For More Beer - FULL Version', 'almostamusingvideos',
        'Drunk Guy Goes For More Beer - FULL Version', 'U03QZB1P5NC'),
       ('-6FfHEXJJOE', 'VHS Kincsek - USA mókus dejópofa KOMMENTÁRRAL!', 'lifeofmatyi',
        'VHS Kincsek - USA mókus dejópofa KOMMENTÁRRAL!', 'U03QZB1P5NC'),
       ('QAo_Ycocl1E', 'Africa', 'Toto - Topic', 'Africa', 'U03QZB1P5NC'),
       ('D9-voINFkCg', 'Samir....You''re breaking the car!!!', 'Hive Funnies', 'Samir....You''re breaking the car!!!',
        'U03QZB1P5NC'),
       ('ZswWnbQl_P4', 'Tough Wank', 'IskuriTube', 'Tough Wank', 'U03QZB1P5NC'),
       ('5a9KSmsIDxw', 'Tudd meg hogy mi vagyunk a Fidesz!', 'Ricky', 'Tudd meg hogy mi vagyunk a Fidesz!',
        'U03QZB1P5NC'),
       ('hWKX2HrkfvA', 'Rugós beke legjobb pillanatok #1', 'ViCc MáNiA', 'Rugós beke legjobb pillanatok #1',
        'U03QZB1P5NC'),
       ('Q8E4Byxy2_o', 'Rugós Beke - Himnusz (Teljes)', 'Geri Iski', 'Rugós Beke - Himnusz (Teljes)', 'U03QZB1P5NC'),
       ('xC03hmS1Brk', 'I Kill People', 'JonLajoie', 'I Kill People', 'U03QZB1P5NC'),
       ('-SQVH6zcI1c', 'How to drink whiskey like a sir MEME', 'PauLo', 'How to drink whiskey like a sir MEME',
        'U03QZB1P5NC'),
       ('23cjXModWpA', 'Cold Blooded Christmas', 'JonLajoie', 'Cold Blooded Christmas', 'U03QZB1P5NC'),
       ('CXyjyYkUWLY', 'Damu Roland bekattan but it''s vocoded to gangsta''s paradise', 'Ádám Papp',
        'Damu Roland bekattan but it''s vocoded to gangsta''s paradise', 'U03QZB1P5NC'),
       ('1CWZZZ0-3UU', 'How To Tame a Wild Animal', 'HowToBasic', 'How To Tame a Wild Animal', 'U03QZB1P5NC'),
       ('3t678W5zfMA', 'How To Fix a Cracked iPhone Screen', 'HowToBasic', 'How To Fix a Cracked iPhone Screen',
        'U03QZB1P5NC'),
       ('E77R0e5bzIs', 'Juice That Makes Your Head Explode', 'TomSka', 'Juice That Makes Your Head Explode',
        'U03QZB1P5NC'),
       ('MlZBER_6Tik', 'The Kiffness X Opera Dog - Am I a Good Boi?', 'The Kiffness',
        'The Kiffness X Opera Dog - Am I a Good Boi?', 'U03QZB1P5NC'),
       ('Iadu_P7zdhg', 'Firefighter fighting a marijuana fire - very funny', 'VeryFunnyVideoCenter',
        'Firefighter fighting a marijuana fire - very funny', 'U03QZB1P5NC'),
       ('8ZrQYEbmK88', 'Szögletes Üveggolyó - Ez egy Fa', 'toxicnagas', 'Szögletes Üveggolyó - Ez egy Fa',
        'U03QZB1P5NC'),
       ('S5DRe4XoDbE', 'Timár Attila - Gyúrás | Szigorú a test', 'Arax塌煙', 'Timár Attila - Gyúrás | Szigorú a test',
        'U03QZB1P5NC'),
       ('2svOtXaD3gg', 'Home Stallone [DeepFake]', 'Ctrl Shift Face', 'Home Stallone [DeepFake]', 'U03QZB1P5NC'),
       ('fnLMELJPHyM', 'Pálinkaivó verseny 2011 Baja', 'Tibor Antal', 'Pálinkaivó verseny 2011 Baja', 'U03QZB1P5NC'),
       ('3ZWZ4YUiULg', 'Zolika női ruhában indulna dolgozni!😉😉😉', 'jános vörös',
        'Zolika női ruhában indulna dolgozni!😉😉😉', 'U03QZB1P5NC'),
       ('4_2ZRHmFg5o', 'Zolika sürű az anyag!', 'jános vörös', 'Zolika sürű az anyag!', 'U03QZB1P5NC'),
       ('Mvq9U54Ij_U', '" HÁZIBULI "', 'arconporges', '" HÁZIBULI "', 'U03QZB1P5NC'),
       ('VqvZ1o62lE0', 'Három autó összehasonlítása.wmv', 'Istvánné Gál', 'Három autó összehasonlítása.wmv',
        'U03QZB1P5NC'),
       ('DRIhQU0z6es', 'Madam X-otic - Riói szerelem 1.', 'Csibecsabax Mister', 'Madam X-otic - Riói szerelem 1.',
        'U03QZB1P5NC'),
       ('y5qe_tLI778', 'BEG - MASSZÍV #1', 'BEGfilm', 'BEG - MASSZÍV #1', 'U03QZB1P5NC'),
       ('V7llzN-iP98', 'Ja, ék van alatta ?!', 'TheCivilera', 'Ja, ék van alatta ?!', 'U03QZB1P5NC'),
       ('2ft954vXPa4', 'in the deer 2nite', 'Josh Ballico', 'in the deer 2nite', 'U03QZB1P5NC'),
       ('DSSB9KEzfK4', 'Best of Kathi Béla', 'MVP Paradox', 'Best of Kathi Béla', 'U03QZB1P5NC'),
       ('i2gNx4-REIA', '“Daddy chill” “what the hell is even that”', 'Frequenzy Genji',
        '“Daddy chill” “what the hell is even that”', 'U03QZB1P5NC'),
       ('--Vaz9jW054', 'Speak the Hungarian Rapper', 'Peter Prince', 'Speak the Hungarian Rapper', 'U03QZB1P5NC'),
       ('nkTwwHq4tVw', 'Disney paródiák: Micimackó (By:. Peti)', 'Radics Peti',
        'Disney paródiák: Micimackó (By:. Peti)', 'U03QZB1P5NC'),
       ('nHP2VlA35ZA', 'Dolly Rambo - Porszívó', 'ironcopy', 'Dolly Rambo - Porszívó', 'U03QZB1P5NC'),
       ('CqURMrUG0ek', 'Disney paródiák: Hófehérke (By:. Peti)', 'Radics Peti',
        'Disney paródiák: Hófehérke (By:. Peti)', 'U03QZB1P5NC'),
       ('uzf5c1Ya2Sc', 'KAtɕAZSÍRRAL?! Ki étkezik zsírosabban, férfiasabban, MAGYARosabban? Bayer vs. Sziszi',
        'János Egressy', 'KAtɕAZSÍRRAL?! Ki étkezik zsírosabban, férfiasabban, MAGYARosabban? Bayer vs. Sziszi',
        'U03QZB1P5NC'),
       ('q-rZqdWvGpo', 'PPAP-Hungarian parody', 'MrGabelot', 'PPAP-Hungarian parody', 'U03QZB1P5NC'),
       ('PQSCQ9FamRw', 'Fekete Pákó - Tart még tart a party (Official Video)', 'Fekete Pákó Online',
        'Fekete Pákó - Tart még tart a party (Official Video)', 'U03QZB1P5NC'),
       ('GJeJVOkHC4U', 'Matisz Nagypapa', 'effigggy', 'Matisz Nagypapa', 'U03QZB1P5NC'),
       ('ntfNGPDIG00', 'AC DC - Irígyeim Sokan Vagytok (mashup)', 'Pentium 040',
        'AC DC - Irígyeim Sokan Vagytok (mashup)', 'U03QZB1P5NC'),
       ('cFXpQ3LVpkY', 'Egs - Ki Ez A Bolond (Prod. b3ncs1)', 'Dodzsem Klub', 'Egs - Ki Ez A Bolond (Prod. b3ncs1)',
        'U03QZB1P5NC');

