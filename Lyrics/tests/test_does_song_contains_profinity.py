import unittest
from src.LyricsProfinity import *
from unittest.mock import patch, Mock


class MyTestCase(unittest.TestCase):

    def test_check_lyrics_for_profinity(self):
        lyrics_without_profinity = "No profinity in this lyrics"
        lyrics_with_profinity = "gun OH NOES A PROFINITY!"
        self.assertFalse(check_lyrics_for_profinity(lyrics_without_profinity))
        self.assertTrue(check_lyrics_for_profinity(lyrics_with_profinity))


    def test_does_song_contains_profinity(self):
        pass


