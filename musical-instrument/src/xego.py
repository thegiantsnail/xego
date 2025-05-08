import pygame
from controller.input_handler import InputHandler
from xid import Xid

def main():
    pygame.init()
    pygame.joystick.init()

    input_handler = InputHandler()
    xid = Xid()  # Initialize the oscillator system

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        input_handler.update()
        button_press = input_handler.get_button_press()
        joystick_movement = input_handler.get_joystick_movement()

        # Map joystick movement to pitch and volume
        if joystick_movement:
            pitch, volume = joystick_movement
            xid.set_frequency(440.0 + pitch * 200)  # Adjust pitch (base frequency ±200 Hz)
            xid.set_volume(0.5 + volume * 0.5)  # Adjust volume (50% ±50%)

        clock.tick(60)

    xid.stop()  # Stop the oscillator when exiting
    pygame.quit()

if __name__ == "__main__":
    main()