class Mappings:
    def __init__(self, xid):
        self.xid = xid  # Reference to the Xid instance
        self.active_oscillators = [True]  # Start with one active oscillator

    def handle_button_press(self, button):
        """Toggle oscillators or change waveforms based on button presses."""
        if button == 0:  # Button 0 toggles the first oscillator
            self.active_oscillators[0] = not self.active_oscillators[0]
            self.xid.toggle_oscillator(0, self.active_oscillators[0])
        elif button == 1:  # Button 1 adds a new oscillator
            self.active_oscillators.append(True)
            self.xid.add_oscillator()
        elif button == 2:  # Button 2 sets the waveform to sine
            self.xid.set_waveform(0, "sine")
        elif button == 3:  # Button 3 sets the waveform to square
            self.xid.set_waveform(0, "square")
        elif button == 4:  # Button 4 sets the waveform to sawtooth
            self.xid.set_waveform(0, "sawtooth")
        elif button == 5:  # Button 5 sets the waveform to triangle
            self.xid.set_waveform(0, "triangle")

    def handle_joystick_movement(self, joystick_data):
        """Map joystick movements to pitch and volume."""
        pitch, volume = joystick_data
        self.xid.set_frequency(440.0 + pitch * 200)  # Adjust pitch (base frequency ±200 Hz)
        self.xid.set_volume(0.5 + volume * 0.5)  # Adjust volume (50% ±50%)