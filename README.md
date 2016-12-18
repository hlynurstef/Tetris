Tetris Revamped
=======
Tetris Revamped(TR) is a clone of the original Tetris,
with main focus on the portable version which was bundled with Gameboy in 1989.

---

Setting up
-------
Unfortunetly there is no executable file available still, but to run TR we first have to install the pygame module which can be done in the following way (assuming you have python3 and pip already installed):

    $ pip install -r requirements.txt

or if you prefer

    $ pip install pygame

---

Getting started
-------
After the requirements have been installed the only thing you need to do is run tetris.py

    $ python tetris.py

or

    $ python3 tetris.py




---

Gameplay
-------
When the game has started the first thing you see is the Title screen.

![Title screen](https://raw.githubusercontent.com/gdgunnars/Tetris/master/images/title_screen.png?token=AD4Zvf5fyuVUm0-ie0mMAGiXuX4S7qaMks5YYFiuwA%3D%3D)

At this stage, there is no 2 player mode but that is something we are working on.

### Controls

You control the Tetramino's in the following way.


Key | Action
------------ | -------------
Left | Moves left
Right | Moves right
Up | Rotates
Down | Soft drop
Space | Hard drop

You also have a few more options keys that you can user


Key | Action
------------ | -------------
Return | Select / Pause
M | Mute music
F | Show fps
Esc | Quit game

### Music selection

![Music selection](https://raw.githubusercontent.com/gdgunnars/Tetris/master/images/type_and_music.png?token=AD4ZvfDD2bFjDlIpE-3gP_9i7Y4p6s3-ks5YYFyrwA%3D%3D)

There is only type A game mode but you can select between three music styles


Known Issues
-------

There is no way to input your name to sign it to your highscore, all scores are assigned to _player_ .
