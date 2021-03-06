import pytest

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, '/Users/HomeFolder/projects/Forest_Game_v2/Forest_Game_v2')
from lexicon import Lexicon

# THIS ENTIRE THING HAS TO BE UPDATED B/C I CHANGED HOW I INPUT THE INPUT into
# THE LEXICON CLASS YOOOOOOOOO

# 
# @pytest.fixture
# def fixtcha_():
#     global lexicon


def test_directions():
    usr_inp = "north"
    lexicon = Lexicon(usr_input)
    assert lexicon.scan() == [('direction', 'north')]
#     result = lexicon.scan("north northburger south east")
#     assert result == [('direction', 'north'),
#                             ('error', 'northburger'),
#                             ('direction', 'south'),
#                             ('direction', 'east')]
# def test_verbs(fixtcha_):
#     assert lexicon.scan("go") == [('verb', 'go')]
#     result = lexicon.scan("go kill eat")
#     assert result == [('verb', 'go'),
#                          ('verb', 'kill'),
#                          ('verb', 'eat')]
# #
# def test_stops(fixtcha_):
#     assert lexicon.scan("the") == [('stop', 'the')]
#     result = lexicon.scan("the in of")
#     assert result == [('stop', 'the'),
#                           ('stop', 'in'),
#                           ('stop', 'of')]
#
# def test_nouns(fixtcha_):
#     assert lexicon.scan("bear") == [('noun', 'bear')]
#     result = lexicon.scan("bear princess")
#     assert result == [('noun', 'bear'),
#                           ('noun', 'princess')]
#
# def test_nouns(fixtcha_):
#     assert lexicon.scan("1234") == [('number', 1234)]
#     result = lexicon.scan("3 91234")
#     assert result == [('number', 3),
#                           ('number', 91234)]
#
# def test_errors(fixtcha_):
#     assert lexicon.scan("ASDFADFASDF") == [('error', 'ASDFADFASDF')]
#     result = lexicon.scan("bear IAS princess")
#     assert result == [('noun', 'bear'),
#                           ('error', 'IAS'),
#                           ('noun', 'princess')]
