import kivy
import random
import os.path
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.uix.dropdown import DropDown
from kivy.config import Config
from kivy.uix.switch import Switch

Config.set('graphics', 'resizable', True)
Window.clearcolor = (0.7, 0.2, 0.7, 0.5)  # color of app background


class Main(FloatLayout):

    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        self.path = "C:\\Users\\ermei\\Desktop\\Music"  # path ΤΡΑΓΟΥΔΙΩΝ
        self.music_order, self.music = os.listdir(self.path), os.listdir(self.path)  # list of the music
        self.i = 0
        self.M = SoundLoader.load(self.path + "\\" + self.music[self.i])  # loading the first song


    def play_song(self):  # PAUSE-START METHOD
        if self.music_button.state == 'down':
            self.M.play()
            print("Song playing is: ", self.music[self.i])
        elif self.music_button.state == 'normal':
            self.M.stop()

    def previous_song(self):  # PREVIOUS SONG
        if self.previous_button.state == "down":
            self.i -= 1
            self.M.stop()
            self.M = SoundLoader.load(self.path + "\\" + self.music[self.i])
            print("Previous song is: ", self.music[self.i])
            self.M.play()

    def next_song(self):  # NEXT SONG
        if self.next_button.state == "down":  # NEXT SONG WITH SHUFFLE
            self.M.stop()
            self.i += 1
            self.M = SoundLoader.load(self.path + "\\" + self.music[self.i])
            print("Next song is: ", self.music[self.i])
            self.M.play()
            self.music_button.state = 'down'

    def shuffle(self):  # SHUFFLE SONGS USING RANDOM MODULE
        if self.shuffle_button.state == "down":
            self.M.stop()
            random.shuffle(self.music)
            print(self.music)
            self.i = random.randrange(len(self.music))
            self.M = SoundLoader.load(self.path + "\\" + self.music[self.i])
            print("Song playing is: ", self.music[self.i])
            self.M.play()
        else:
            self.music = self.music_order



class Mp3(App):
    def build(self):
        return Main()


if __name__ == "__main__":
    Mp3().run()
