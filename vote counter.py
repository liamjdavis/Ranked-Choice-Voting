import names
import random
import sys

class Ballot():
    def __init__(self, firstChoice, secondChoice, thirdChoice):
        self.firstChoice = firstChoice
        self.secondChoice = secondChoice
        self.thirdCHoice = thirdChoice

def main():
    candidates = createCandidates(5)
    ballots = createBallots(100, candidates)
    candidates_afterFirstElim = elim_lowFirstChoice(candidates, ballots)

def createCandidates(numCandidates):
    candidates = []

    # assign random name to candidate
    for i in range (numCandidates):
        name = names.get_full_name
        candidates.append(name)

    return candidates

def createBallots(numBallots, candidates):
    ballots = []

    # create three random unique votes
    for i in range (numBallots):
        randInt1 = getRandInt(0, len(candidates), -1, -1)
        randInt2 = getRandInt(0, len(candidates), randInt1, -1)
        randInt3 = getRandInt(0, len(candidates), randInt1, randInt2)

        ballot = Ballot(candidates[randInt1], candidates[randInt2], candidates[randInt3])
        ballots.append(ballot)
    
    return ballots

def elim_lowFirstChoice(candidates, ballots):
    # create list to tally votes
    votes = [None for _ in range(len(candidates))]
    ballotsFirstChoice = [None for _ in range(len(candidates))]

    # iterate through ballots
    for ballot in ballots:
        vote = ballot.firstChoice
        index = candidates.index(vote)
        votes[index] += 1
    
    # eliminate candidate with lowest number of votes
    min = sys.maxsize
    indexLowest = -1

    for i in range (len(votes)):
        if votes[i] < min:
            min = votes[i]

    indexLowest = votes.index(min)
    newCandidates = candidates
    del newCandidates[indexLowest]
    return newCandidates

def getRandInt(start, stop, exclude, exclude1):
    while True:
        num = random.randint(start, stop)
        if num != (exclude or exclude1):
            return num