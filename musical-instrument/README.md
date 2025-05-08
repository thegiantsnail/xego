# Musical Instrument Project

This project is a simple musical instrument that responds to input from a Bluetooth Xbox 360 controller. It utilizes Pygame for controller input and an audio library for real-time sound playback.

## Project Structure

```
musical-instrument
├── src
│   ├── main.py               # Entry point of the application
│   ├── controller
│   │   ├── input_handler.py   # Handles Xbox 360 controller input
│   │   └── mappings.py        # Maps controller inputs to sounds
│   ├── audio
│   │   ├── sound_player.py     # Plays sounds in real-time
│   │   └── sound_library.py     # Loads and stores sound samples
│   └── utils
│       └── latency_handler.py   # Manages latency in sound playback
├── requirements.txt           # Project dependencies
├── .gitignore                 # Files to ignore in Git
└── README.md                  # Project documentation
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd musical-instrument
   ```

2. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

## Usage Guidelines

1. **Connect your Xbox 360 controller** via Bluetooth.
2. **Run the application**:
   ```
   python src/main.py
   ```
3. **Interact with the instrument** using the controller. Button presses and joystick movements will trigger different sounds.

## Features

- Real-time sound playback using an Xbox 360 controller.
- Customizable mappings for buttons and joystick movements to different notes or sounds.
- Latency management to ensure smooth audio playback.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.