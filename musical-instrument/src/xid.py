# filepath: c:\Users\thegi\Documents\GitHub\xego\musical-instrument\src\xid.py

import numpy as np
import sounddevice as sd
from audio.sound_library import load_sounds
from audio.sound_player import SoundPlayer

class Xid:
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate
        self.frequency = 440.0  # Default frequency (A4)
        self.volume = 0.5  # Default volume (50%)
        self.running = True

        # Start the audio stream
        self.stream = sd.OutputStream(
            samplerate=self.sample_rate,
            channels=1,
            callback=self.audio_callback
        )
        self.stream.start()

    def audio_callback(self, outdata, frames, time, status):
        """Generate audio samples for the oscillator."""
        t = (np.arange(frames) + time.outputBufferDacTime * self.sample_rate) / self.sample_rate
        waveform = self.volume * np.sin(2 * np.pi * self.frequency * t)
        outdata[:] = waveform.reshape(-1, 1)

    def set_frequency(self, frequency):
        """Set the oscillator frequency."""
        self.frequency = frequency

    def set_volume(self, volume):
        """Set the oscillator volume."""
        self.volume = max(0.0, min(volume, 1.0))  # Clamp volume between 0 and 1

    def stop(self):
        """Stop the audio stream."""
        self.running = False
        self.stream.stop()
        self.stream.close()

    def play_sound(self, button):
        # Play sound logic
        pass

    def handle_joystick(self, movement):
        # Handle joystick movement
        pass