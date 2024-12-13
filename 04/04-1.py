import logging
import numpy as np
FORMAT = '%(asctime)s %(message)s %(name)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

logger = logging.getLogger(__name__)

logger.info("info log")
logger.warning("warn log")

def parse_board(boardstr):
    return [[int(y) for y in x.split()] for x in boardstr.split('\n')]

def check_bingo(matches, boards):
    """
    Checks if a bingo is won by summing the elements in each row and column of a
    bingo board, based on the provided `matches` and `boards`. It returns True
    along with the winning row, column, board, and the sum of unmarked numbers if
    a win is detected, or False otherwise.

    Args:
        matches (ndarray): Used to check for bingo on a 2D array of bingo boards.
            It is likely a binary matrix where 1 indicates a match and 0 indicates
            no match. Its shape is assumed to be (number of boards, number of rows/columns).
        boards (Any): Represented as a collection of 2D arrays, each with 5 rows
            and 5 columns, where each element represents a square on a bingo board.

    Returns:
        Tuple[bool,Optional[ndarray],Optional[ndarray],ndarray,int]: A boolean
        indicating whether bingo was found,
        an optional column of numbers that won,
        an optional entire winning board,
        a 2D array of unmarked numbers on the winning board,
        and the sum of the unmarked numbers.

    """
    for b in range(matches.shape[0]):
        for i in range(matches.shape[1]):
            if sum(matches[b,i]) == 5:
                unmarked = boards[b] * (1-matches[b])
                sum_unmarked = sum(sum(unmarked))
                return (True, boards[b,i,:], boards[b], unmarked, sum_unmarked)
        for j in range(matches.shape[1]):
            if sum(matches[b,:,j]) == 5:
                unmarked = boards[b] * (1-matches[b])
                sum_unmarked = sum(sum(unmarked))
                return (True, boards[b,:,j], boards[b], unmarked, sum_unmarked)
    return (False, None, None, None, None)




if __name__ == "__main__":
    with open("04/input-04.txt", 'r') as f:
        numbers_to_call = [int(x) for x in f.readline().strip().split(',')]
        boards = np.array([parse_board(x) for x in f.read().strip().split('\n\n')])
    matches = 0 * boards
    for called_num in numbers_to_call:
        print(called_num)
        matches += (boards == called_num)
        (is_bingo, line_matched, board, unmarked, sum_unmarked) = check_bingo(matches, boards)
        if is_bingo:
            break
    print(called_num, line_matched, board)
    print(called_num * sum_unmarked)


logger.info("end")