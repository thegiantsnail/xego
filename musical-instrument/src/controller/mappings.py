# This file contains mappings of controller inputs to musical notes or sounds.

controller_mappings = {
    'A': 'C4',  # Button A maps to Middle C
    'B': 'D4',  # Button B maps to D4
    'X': 'E4',  # Button X maps to E4
    'Y': 'F4',  # Button Y maps to F4
    'LB': 'G4',  # Left Bumper maps to G4
    'RB': 'A4',  # Right Bumper maps to A4
    'LT': 'B4',  # Left Trigger maps to B4
    'RT': 'C5',  # Right Trigger maps to C5
    'LEFT_STICK_UP': 'E5',  # Joystick up maps to E5
    'LEFT_STICK_DOWN': 'D5',  # Joystick down maps to D5
    'LEFT_STICK_LEFT': 'C5',  # Joystick left maps to C5
    'LEFT_STICK_RIGHT': 'B4',  # Joystick right maps to B4
    'RIGHT_STICK_UP': 'F5',  # Joystick up maps to F5
    'RIGHT_STICK_DOWN': 'E5',  # Joystick down maps to E5
    'RIGHT_STICK_LEFT': 'D5',  # Joystick left maps to D5
    'RIGHT_STICK_RIGHT': 'C5',  # Joystick right maps to C5
}

class Mappings:
    def __init__(self, xid):
        self.xid = xid  # Reference to the Xid instance
        self.active_oscillators = [True]  # Start with one active oscillator

    def handle_button_press(self, button):
        """Toggle oscillators or perform other actions based on button presses."""
        if button == 0:  # Example: Button 0 toggles the first oscillator
            self.active_oscillators[0] = not self.active_oscillators[0]
            self.xid.toggle_oscillator(0, self.active_oscillators[0])
        elif button == 1:  # Example: Button 1 adds a new oscillator
            self.active_oscillators.append(True)
            self.xid.add_oscillator()

    def handle_joystick_movement(self, joystick_data):
        """Map joystick movements to pitch and volume."""
        pitch, volume = joystick_data
        self.xid.set_frequency(440.0 + pitch * 200)  # Adjust pitch (base frequency ±200 Hz)
        self.xid.set_volume(0.5 + volume * 0.5)  # Adjust volume (50% ±50%)