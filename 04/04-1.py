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
    Checks for a bingo in a given set of bingo boards, where a bingo is declared
    when a row or column contains exactly five matches. It returns a tuple indicating
    a bingo win, along with the winning row, column, board, unmarked numbers, and
    the sum of unmarked numbers.

    Args:
        matches (numpy.ndarray): 2D array where each element represents whether a
            number on a bingo board has been matched (1) or not (0).
        boards (List[np.ndarray]): Represented as a 2D NumPy array, where each row
            corresponds to a bingo board.

    Returns:
        Tuple[bool,Optional[ndarray],Optional[ndarray],ndarray,int]: A boolean
        indicating whether a bingo has been found,
        a 1D array representing the winning row or column,
        a 2D array representing the entire winning board,
        a 2D array of unmarked numbers on the winning board,
        and the sum of the unmarked numbers on the winning board.

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