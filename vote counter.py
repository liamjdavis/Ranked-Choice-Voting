import names
import random


class Ballot:
    def __init__(self, firstChoice, secondChoice, thirdChoice, fourthChoice):
        self.firstChoice = firstChoice
        self.secondChoice = secondChoice
        self.thirdChoice = thirdChoice
        self.fourthChoice = fourthChoice


def main():
    candidates = createCandidates()
    ballots = createBallots(100, candidates)

    # sort ballots by first choice vote
    sortedBallots = sortBallots(ballots, candidates)
    # eliminate candidate with least first choice votes
    # add second choice votes to other candidates

    # check for winner

    # eliminate the candidate with the least first choice votes

    # assign votes of eliminated candidates to the highest ranked remaining candidate


def createCandidates():
    candidates = []

    # assign random name to 4 candidates
    for i in range(4):
        name = names.get_full_name
        candidates.append(name)

    return candidates


def createBallots(numBallots, candidates):
    ballots = []

    # create four random unique votes
    for i in range(numBallots):
        randInt1 = getRandInt(0, len(candidates), -1, -1, -1)
        randInt2 = getRandInt(0, len(candidates), randInt1, -1, -1)
        randInt3 = getRandInt(0, len(candidates), randInt1, randInt2, -1)
        randInt4 = getRandInt(0, len(candidates), randInt1, randInt2, randInt3)

        ballot = Ballot(candidates[randInt1], candidates[randInt2], candidates[randInt3], candidates[randInt4])
        ballots.append(ballot)

    return ballots


def sortBallots(ballots, candidates):
    sortedBallots = {}

    for ballot in ballots:
        firstChoice = ballot.firstChoice
        index_toAppend = candidates.index(firstChoice in candidates)
        sortedBallots[index_toAppend].insert(0, ballot)

    return sortedBallots


def getRandInt(start, end, exclude1, exclude2, exclude3):
    while True:
        random_value = random.randint(start, end)
        if random_value not in (exclude1 or exclude2 or exclude3):
            return random_value
