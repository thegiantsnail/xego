import pygame  # Ensure pygame is imported

class InputHandler:
    def __init__(self):
        self.setup_controller()

    def setup_controller(self):
        if pygame.joystick.get_count() > 0:
            self.controller = pygame.joystick.Joystick(0)
            self.controller.init()
        else:
            self.controller = None

    def update(self):
        """Update the controller state."""
        pygame.event.pump()

    def get_button_press(self):
        """Return the index of the button pressed, if any."""
        if self.controller:
            for i in range(self.controller.get_numbuttons()):
                if self.controller.get_button(i):
                    return i
        return None

    def get_joystick_movement(self):
        """Return joystick axis movements as (pitch, volume)."""
        if self.controller:
            pitch = self.controller.get_axis(1)  # Example: Y-axis for pitch
            volume = self.controller.get_axis(3)  # Example: Z-axis for volume
            return pitch, volume
        return None