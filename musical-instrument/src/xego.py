import pygame
from controller.input_handler import InputHandler
from controller.mappings import Mappings
from xid import Xid

def main():
    pygame.init()
    pygame.joystick.init()

    input_handler = InputHandler()
    xid = Xid()  # Initialize the oscillator system
    mappings = Mappings(xid)  # Pass Xid to Mappings

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        input_handler.update()
        button_press = input_handler.get_button_press()
        joystick_movement = input_handler.get_joystick_movement()

        if button_press is not None:
            mappings.handle_button_press(button_press)

        if joystick_movement:
            mappings.handle_joystick_movement(joystick_movement)

        clock.tick(60)

    xid.stop()  # Stop the oscillator when exiting
    pygame.quit()

if __name__ == "__main__":
    main()