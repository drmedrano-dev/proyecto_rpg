# main.py
import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BG_COLOR


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Turn-Based RPG - Team Project")
    clock = pygame.time.Clock()

    # Game State Machine: "MENU", "EXPLORATION", "COMBAT"
    game_state = "EXPLORATION"

    running = True
    while running:
        # Capture all events once per frame
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        # Clear screen before rendering current state
        screen.fill(BG_COLOR)

        # State Machine Orchestrator (3 phases per active state)
        if game_state == "EXPLORATION":
            # handle_exploration_events(events)
            # update_exploration()
            # render_exploration(screen)
            pass
        elif game_state == "COMBAT":
            # handle_combat_events(events)
            # update_combat()
            # render_combat(screen)
            pass

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    run_game()