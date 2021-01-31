import chess
import chss
import chess.pgn as p
from colour import Color

class Game:
    def __init__(self):
        self.game = p.Game()
        self.board = chess.Board()
        self.svg = chss.board(board=self.board)

    def write_game(self):
        print(self.game, file=open("game", "w"), end="\n\n")

    def read_game(self):
        self.game = p.read_game(open("game"))

    def make_svg(self, metadata: False):
        colors = {
            "square light": "#FFF",
            "square dark": "#e6e6e6"
        }
        arrows = []
        color_check = True
        total_moves = 0
        # must count the moves to generate colors
        for move in self.game.mainline_moves():
            total_moves += 1
        start_black = Color("#d9eef2")
        color_black = list(start_black.range_to(Color("#1a444c"), int(total_moves/2 + 1)))
        start_white = Color("#fad8d1")
        color_white = list(start_white.range_to(Color("#5c180a"), int(total_moves/2 + 1)))
        color_black.reverse()
        color_white.reverse()
        for move in self.game.mainline_moves():
            self.board.push(move)
            if color_check:
                color = color_black.pop()
                color_check = False
            else:
                color = color_white.pop()
                color_check = True
            arrows.append(chss.Arrow(move.from_square, move.to_square, color=color.get_hex()))
        self.svg = chss.board(None, colors=colors, coordinates=False, arrows=arrows)
        if metadata:
            pass
        f = open("game.svg", "w+")
        f.write(self.svg)
        f.close()


if __name__ == "__main__":
    game = Game()
    game.read_game()
    game.make_svg(metadata=True)
