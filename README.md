# Turn Based 2D RPG with Pygame-CE

A 2D turn-based RPG developed in Python using **Pygame Community Edition (`pygame-ce`)**.

## Setup & Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/drmedrano-dev/proyecto_rpg.git
   cd proyecto_rpg
   ```

2. **Create and activate a virtual environment (recommended):**

   - Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - Mac/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies:**

   ```bash
   pip install pygame-ce
   ```

4. **Run the game:**

   ```bash
   python main.py
   ```

## Project Architecture

- `main.py`: Entry point, game loop, and state machine.
- `config.py`: Global constants (screen dimensions, FPS, colors).
- `src/`: Core object oriented game logic (`entities.py`, `combat.py`, `inventory.py`, `exploration.py`, `ui.py`).
- `assets/`: Sprites, maps, and audio files.