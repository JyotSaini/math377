import json
from random import randrange

donors = {}

def assignQualityScore():
    return randrange(20)

def buildSet(numPairs, numDeceased):
    for i in range(1, numPairs + 1):        # Living Donors
        donori = {}
        donori['alive'] = True

        for j in range(1, numPairs + 1):    # Assign quality scores for ever donor recipient pair
            if j is not i:
                donori['r' + str(j)] = assignQualityScore()
            # else:
            #     donori['r' + str(j)] = -1

        donors['d' + str(i)] = donori

    for i in range(numPairs + 1, numPairs + numDeceased + 1):   # Deceased Donors
        donori = {}
        donori['alive'] = False

        for j in range(1, numPairs + 1):    # Assign quality scores for ever donor recipient pair
            donori['r' + str(j)] = assignQualityScore()

        donors['d' + str(i)] = donori

def main():
    buildSet(6, 2)

    with open('donors.json', 'w') as outfile:
        json.dump(donors, outfile, indent=4)

    print(donors)

if __name__ == '__main__':
    main()