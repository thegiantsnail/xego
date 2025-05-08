# filepath: c:\Users\thegi\Documents\GitHub\xego\musical-instrument\src\xid.py

import numpy as np
import sounddevice as sd
from audio.sound_library import load_sounds
from audio.sound_player import SoundPlayer

class Xid:
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate
        self.oscillators = [{"frequency": 440.0, "volume": 0.5, "active": True, "waveform": "sine"}]  # Default oscillator
        self.running = True

        # Start the audio stream
        self.stream = sd.OutputStream(
            samplerate=self.sample_rate,
            channels=1,
            callback=self.audio_callback
        )
        self.stream.start()

    def audio_callback(self, outdata, frames, time, status):
        """Generate audio samples for all active oscillators."""
        t = (np.arange(frames) + time.outputBufferDacTime * self.sample_rate) / self.sample_rate
        waveform = np.zeros(frames)
        for osc in self.oscillators:
            if osc["active"]:
                if osc["waveform"] == "sine":
                    waveform += osc["volume"] * np.sin(2 * np.pi * osc["frequency"] * t)
                elif osc["waveform"] == "square":
                    waveform += osc["volume"] * np.sign(np.sin(2 * np.pi * osc["frequency"] * t))
                elif osc["waveform"] == "sawtooth":
                    waveform += osc["volume"] * 2 * (t * osc["frequency"] % 1) - 1
                elif osc["waveform"] == "triangle":
                    waveform += osc["volume"] * 2 * np.abs(2 * (t * osc["frequency"] % 1) - 1) - 1
        outdata[:] = waveform.reshape(-1, 1)

    def set_frequency(self, frequency, oscillator_index=0):
        """Set the frequency of a specific oscillator."""
        if 0 <= oscillator_index < len(self.oscillators):
            self.oscillators[oscillator_index]["frequency"] = frequency

    def set_volume(self, volume, oscillator_index=0):
        """Set the volume of a specific oscillator."""
        if 0 <= oscillator_index < len(self.oscillators):
            self.oscillators[oscillator_index]["volume"] = max(0.0, min(volume, 1.0))

    def toggle_oscillator(self, oscillator_index, active):
        """Toggle an oscillator on or off."""
        if 0 <= oscillator_index < len(self.oscillators):
            self.oscillators[oscillator_index]["active"] = active

    def add_oscillator(self, frequency=440.0, volume=0.5, waveform="sine"):
        """Add a new oscillator."""
        self.oscillators.append({"frequency": frequency, "volume": volume, "active": True, "waveform": waveform})

    def set_waveform(self, oscillator_index, waveform):
        """Set the waveform of a specific oscillator."""
        if 0 <= oscillator_index < len(self.oscillators):
            if waveform in ["sine", "square", "sawtooth", "triangle"]:
                self.oscillators[oscillator_index]["waveform"] = waveform

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