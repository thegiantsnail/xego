class SoundPlayer:
    def __init__(self, sound_library):
        self.sound_library = sound_library

    def play_sound(self, note):
        if note in self.sound_library:
            sound = self.sound_library[note]
            sound.play()

    def stop_sound(self, note):
        if note in self.sound_library:
            sound = self.sound_library[note]
            sound.stop()