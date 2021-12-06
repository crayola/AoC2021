import logging
import numpy as np
FORMAT = '%(asctime)s %(message)s %(name)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

logger = logging.getLogger(__name__)

logger.info("info log")
logger.warning("warn log")

def parse_board(boardstr):
    return [[int(y) for y in x.split()] for x in boardstr.split('\n')]

def check_bingos(matches, boards, bingos):
    matched = None
    for b in range(matches.shape[0]):
        for i in range(matches.shape[1]):
            if sum(matches[b,i]) == 5:
                if b not in bingos:
                    bingos = bingos.union({b})
                    matched = b
        for j in range(matches.shape[1]):
            if sum(matches[b,:,j]) == 5:
                if b not in bingos:
                    bingos = bingos.union({b})
                    matched = b
    return (bingos, matched)




if __name__ == "__main__":
    with open("04/input-04.txt", 'r') as f:
        numbers_to_call = [int(x) for x in f.readline().strip().split(',')]
        boards = np.array([parse_board(x) for x in f.read().strip().split('\n\n')])
    matches = 0 * boards
    bingos = set()
    for called_num in numbers_to_call:
        print(called_num)
        matches += (boards == called_num)
        bingos, matched = check_bingos(matches, boards, bingos)
        print(bingos)
        if len(bingos) == boards.shape[0]:
            b = matched
            unmarked = boards[b] * (1-matches[b])
            sum_unmarked = sum(sum(unmarked))
            break
    print(called_num, boards[b], unmarked)
    print(called_num * sum_unmarked)

logger.info("end")







