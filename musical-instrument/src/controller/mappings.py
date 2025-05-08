class Mappings:
    def __init__(self, xid):
        self.xid = xid  # Reference to the Xid instance
        self.active_oscillators = [False] * 6  # Start with all oscillators inactive

    def handle_button_press(self, button, pressed):
        """Toggle oscillators based on button presses."""
        if 0 <= button < len(self.active_oscillators):  # Ensure button maps to an oscillator
            self.active_oscillators[button] = pressed
            self.xid.toggle_oscillator(button, pressed)

        # Map buttons to waveforms
        if pressed:
            if button == 2:
                self.xid.set_waveform(0, "sine")
            elif button == 3:
                self.xid.set_waveform(0, "square")
            elif button == 4:
                self.xid.set_waveform(0, "sawtooth")
            elif button == 5:
                self.xid.set_waveform(0, "triangle")

    def handle_joystick_movement(self, joystick_data):
        """Map joystick movements to pitch and volume."""
        pitch, volume = joystick_data
        for i in range(len(self.active_oscillators)):
            if self.active_oscillators[i]:  # Only adjust active oscillators
                self.xid.set_frequency(440.0 + pitch * 200, oscillator_index=i)  # Adjust pitch
                self.xid.set_volume(0.5 + volume * 0.5, oscillator_index=i)  # Adjust volume