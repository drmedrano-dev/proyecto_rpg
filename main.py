import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BG_COLOR


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Turn-Based RPG - Team Project")
    clock = pygame.time.Clock()

    game_state = "MENU"
    running = True

    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG_COLOR)

        # TODO: uncomment each block as the module gets implemented
        # if game_state == "MENU":
        #     menu.handle_events(events)
        #     menu.update()
        #     menu.render(screen)
        # elif game_state == "EXPLORATION":
        #     world_map.handle_events(events)
        #     world_map.update()
        #     world_map.render(screen)
        # elif game_state == "COMBAT":
        #     combat.handle_events(events)
        #     combat.update()
        #     combat.render(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    run_game()   