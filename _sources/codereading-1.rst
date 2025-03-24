Exercise 2: Managing Spotify Databases
================================

You are working for Spotify. One of your coworkers shared the following queries with you, and asked you to interpret the output in a report. However, they did not comment their code, and it looks like they are offline, so you need to figure out what this does.

Look at the code and describe what the queries might be doing.

.. activecode:: streaming_ex
    :language: sql
    :dburl: /_static/spotify.sqlite3

    INSERT INTO Users (username, email, subscription_status) VALUES
    ('alice_music', 'alice@example.com', 'premium'),
    ('bob_rocks', 'bob@example.com', 'free'),
    ('charlie_vibes', 'charlie@example.com', 'free');

    UPDATE Users
    SET subscription_status = 'premium'
    WHERE username = 'bob_rocks';

    INSERT INTO Songs (title, artist, album, listened_by) VALUES
    ('Shape of Sound', 'Echo Beats', 'Rhythm Nation', 150),
    ('Mountain Ride', 'Echo Beats', 'Rhythm Nation', 20),
    ('Flying Through', 'Synth Dreams', 'Neon Lights', 70),
    ('Jazz & Chill', 'Smooth Cats', 'Lounge Vibes', 30),
    ('Night Drive', 'Synth Dreams', 'Neon Lights', 90);

    SELECT title, artist, COUNT(listened_by)
    FROM Songs
    GROUP BY artist


.. shortanswer:: exercise_2_q1

    Enter your description here.


.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:

   If you completed all the activities on this page, click on the arrow on the bottom right to continue.

