"""Wordle Interface Module."""
from typing import List
import pygame
from words import get_random_word

WIDTH = 400
HEIGH = 300


class Wordle:
    def __init__(self, word_length: int = 5, max_attempts: int = 5) -> None:
        self.word_length = word_length
        self.max_attempts = max_attempts
        self.grid = [["" for _ in range(word_length)] for _ in range(max_attempts)]
        self.current_attempt = 0
        self._secret_word = get_random_word()

    def check_word(self, guess: str) -> List[str]:
        square_colors = []
        for idx, letter in enumerate(guess):
            if letter == self._secret_word[idx]:
                square_colors.append("green")
            elif letter in self._secret_word:
                square_colors.append("yellow")
            else:
                square_colors.append("gray")
        return square_colors
    
    def place_grid(self) -> None:
        ...

    def flip_squares(self) -> None:
        ...

    def win_animation(self) -> None:
        ...

    def defeat_animation(self) -> None:
        ...

    def run(self) -> None:
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGH))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    print(f"{event.key} was pressed.")

        pygame.quit()

def main() -> int:
    wordle = Wordle()
    wordle.run()
    return 0


if __name__ == "__main__":
    SystemExit(main())
