from typing import List, Tuple, Optional
import numpy as np


class GrotGameSolver:
    """Class with algorithms to solve GROT game
    """
    __slots__ = ["board"]

    def __init__(self, board: List[List] = None):
        self.board = np.array(board)

    def show_board(self) -> np.array:
        """Just return board 
        """
        return self.board

    def find_longest_chain(self, board: Optional[List[List]] = None) -> List[int]:
        """This method look for longest chain in board game.
        get board as argument or given as argument 

        Args:
            board (Optional[List[List]], optional): Board to game. 
            Defaults to board from self.board.

        Returns:
            [x, y, length] type=int: x and y is location of starting point the longest chain
        """
        # prepare list, best alternate I know is to compare every new chain and if new
        # chain is longer then previous the longest, then replace
        score_list = []
        if board is None:
            # get dimensions of board
            dims = len(self.board), len(self.board[0])
            for x in range(dims[0]):
                for y in range(dims[1]):
                    # append *Point(x,y), length of chain
                    score_list.append([x, y,
                                      self.local_chain((x, y))])
        else:
            # the same as above but board from argument
            dims = len(board), len(board[0])
            for x in range(dims[1]):
                for y in range(dims[0]):
                    score_list.append([x, y,
                                      self.local_chain((x, y), board)])

        # sort by length and return the first (longest one)
        score_list.sort(key=lambda x: x[2], reverse=True)
        return score_list[0]

    def local_chain(self, start: Tuple[int],
                    board: Optional[List[List]] = None) -> int:

        if board is None:
            board_copy = np.copy(self.board).T
        else:
            board_copy = np.copy(board).T
        x, y = start
        board_dim = len(board_copy), len(board_copy[y])
        length = 0
        char, board_copy[x, y] = board_copy[x, y], 'x'
        while char != 'x':
            shift = self.shift_to(x, y, char)
            length += 1
            x = shift[0]
            y = shift[1]
            if not self.if_on_board((x, y), board_dim):
                break
            char, board_copy[x, y] = board_copy[x, y], 'x'

        return length

    def next_field(self, x: int, y: int,
                   shift_x: int = 0, shift_y: int = 0) -> Tuple[int]:
        """just increase the proper value (x/y) and return next location of chain

        Args:
            x (int): current x coordinate
            y (int): current y coordinate
            shift_x (int, optional): increse x by this value, default by 0 (neutral).
            shift_y (int, optional): increse y by this value, default by 0 (neutral).

        Returns:
            Tuple[int]: new chain coordinates (x,y) 
        """
        return x+shift_x, y+shift_y

    def shift_to(self, x: int, y: int, char: str) -> Tuple[int]:
        """Convert char/letter to coordinates shift 

        Args:
            x (int): current x coordinate
            y (int): current y coordinate
            char (str): letter as code (u)p, (d)own, (l)eft, (r)ight

        Raises:
            TypeError: when value is not supported but algorithm (not in {u,d,l,r})

        Returns:
            Tuple[int]: nex coordinte to check
        """
        if char == 'r':
            return self.next_field(x, y, shift_x=1)

        elif char == 'l':
            return self.next_field(x, y, shift_x=-1)

        elif char == 'u':
            return self.next_field(x, y, shift_y=-1)

        elif char == 'd':
            return self.next_field(x, y, shift_y=1)

        elif char == 'x':
            return False
        print(char)
        raise TypeError("unsupported value found")

    def if_on_board(self, point: Tuple[int], board_dim: Tuple[int]) -> bool:
        """Return if point is on board or outside

        Args:
            point (Tuple[int]): current localization (x,y)
            board_dim (Tuple[int]): dimension of board

        Returns:
            bool: True -> is on board, False -> is outside
        """
        # check bottom and right side of board
        condition = point[0] < board_dim[0] and point[1] < board_dim[1]
        # above * check top and left
        return condition and point[0] >= 0 and point[1] >= 0


def main():
    sample = [
        ['u', 'd', 'u', 'u'],  # ↑ ↓ ↑ ↑
        ['u', 'r', 'l', 'l'],  # ↑ → ← ←
        ['u', 'u', 'l', 'u'],  # ↑ ↑ ← ↑
        ['l', 'd', 'u', 'l'],  # ← ↓ ↑ ←
    ]
    grot = GrotGameSolver(sample)
    print(grot.find_longest_chain())
    sample_2 = [
        ['u', 'd', 'u', 'u', 'l', 'd'],  # ↑ ↓ ↑ ↑
        ['u', 'r', 'l', 'l', 'u', 'r'],  # ↑ → ← ←
        ['u', 'u', 'l', 'u', 'l', 'u'],  # ↑ ↑ ← ↑
        ['l', 'd', 'u', 'l', 'd', 'u'],  # ← ↓ ↑ ←
    ]
    print(grot.find_longest_chain(sample_2))


if __name__ == "__main__":
    main()
