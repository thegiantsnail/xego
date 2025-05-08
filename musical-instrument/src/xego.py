import pygame
from controller.input_handler import InputHandler
from controller.mappings import Mappings
from xid import Xid

# Constants for the display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FONT_SIZE = 24
BUTTON_LABELS = {
    0: "Toggle Oscillator 1",
    1: "Add Oscillator",
    2: "Set Waveform: Sine",
    3: "Set Waveform: Square",
    4: "Set Waveform: Sawtooth",
    5: "Set Waveform: Triangle",
}

def draw_feedback(screen, font, button_states, joystick_data):
    """Draw the visual feedback on the screen."""
    screen.fill((0, 0, 0))  # Clear the screen with a black background

    # Display button states
    y_offset = 50
    for button, label in BUTTON_LABELS.items():
        color = (0, 255, 0) if button_states.get(button, False) else (255, 0, 0)
        text = font.render(f"Button {button}: {label}", True, color)
        screen.blit(text, (50, y_offset))
        y_offset += 40

    # Display joystick data
    if joystick_data:
        pitch, volume = joystick_data
        pitch_text = font.render(f"Pitch: {pitch:.2f}", True, (255, 255, 255))
        volume_text = font.render(f"Volume: {volume:.2f}", True, (255, 255, 255))
        screen.blit(pitch_text, (50, y_offset))
        screen.blit(volume_text, (50, y_offset + 40))

    pygame.display.flip()  # Update the display

def main():
    pygame.init()
    pygame.joystick.init()

    # Initialize the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Xego Controller Feedback")
    font = pygame.font.Font(None, FONT_SIZE)

    input_handler = InputHandler()
    xid = Xid()  # Initialize the oscillator system
    mappings = Mappings(xid)  # Pass Xid to Mappings

    clock = pygame.time.Clock()

    # Persist button states across frames
    button_states = {button: False for button in BUTTON_LABELS.keys()}

    running = True
    while running:
        joystick_data = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.JOYBUTTONDOWN:
                button_states[event.button] = True  # Update button state
                mappings.handle_button_press(event.button, True)
            elif event.type == pygame.JOYBUTTONUP:
                button_states[event.button] = False  # Update button state
                mappings.handle_button_press(event.button, False)

        joystick_movement = input_handler.get_joystick_movement()
        if joystick_movement:
            joystick_data = joystick_movement
            mappings.handle_joystick_movement(joystick_movement)

        # Draw the feedback on the screen
        draw_feedback(screen, font, button_states, joystick_data)

        clock.tick(60)

    xid.stop()  # Stop the oscillator when exiting
    pygame.quit()

if __name__ == "__main__":
    main()