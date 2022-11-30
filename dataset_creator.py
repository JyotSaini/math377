import json
from random import random

donors = {}
recipients = {}

def livingDonorAge():
    # Collected donor age statistics from following link:
    # https://optn.transplant.hrsa.gov/data/view-data-reports/center-data/
    rand = random()
    print(rand)
    if rand <= 0.41:                    # 41% chance to be 18-34
        return (random() * 17) + 18     # Uniform distribution within age group
    elif rand <= 0.86:                  # 45% chance to be 35-49
        return (random() * 15) + 35
    elif rand <= 0.99:                  # 13% chance to be 50-64
        return (random() * 15) + 50
    else:                               # 1% chance to be 65-80
        return (random() * 15) + 65

def deceasedDonorAge():
    # Collected donor age statistics from following link:
    # https://optn.transplant.hrsa.gov/data/view-data-reports/center-data/
    rand = random()
    print(rand)
    if rand <= 0.36:                    # 36% chance to be 18-34
        return (random() * 17) + 18     # Uniform distribution within age group
    elif rand <= 0.69:                  # 33% chance to be 35-49
        return (random() * 15) + 35
    elif rand <= 0.96:                  # 27% chance to be 50-64
        return (random() * 15) + 50
    else:                               # 4% chance to be 65-80
        return (random() * 15) + 65

def recipientAge():
    # Collected recipient age statistics from following link:
    # https://optn.transplant.hrsa.gov/data/view-data-reports/center-data/
    rand = random()
    print(rand)
    if rand <= 0.19:                    # 19% chance to be 18-34
        return (random() * 17) + 18     # Uniform distribution within age group
    elif rand <= 0.49:                  # 30% chance to be 35-49
        return (random() * 15) + 35
    elif rand <= 0.86:                  # 37% chance to be 50-64
        return (random() * 15) + 50
    else:                               # 14% chance to be 65-80
        return (random() * 15) + 65

def recipientABO():
    # Collected recipient ABO statistics from following link:
    # https://optn.transplant.hrsa.gov/data/view-data-reports/center-data/
    rand = random()
    print(rand)
    if rand <= 0.47:                    # 47% chance to have O blood type
        return 'O'
    elif rand <= 0.82:                  # 35% chance to have A blood type
        return 'A'
    elif rand <= 0.95:                  # 13% chance to have B blood type
        return 'B'
    else:                               # 5% chance to have AB blood type
        return 'AB'

def donorABO():
    # Collected general population ABO statistics from following link:
    # https://www.blood.ca/en/blood/donating-blood/what-my-blood-type
    rand = random()
    print(rand)
    if rand <= 0.46:                    # 46% chance to have O blood type
        return 'O'
    elif rand <= 0.88:                  # 42% chance to have A blood type
        return 'A'
    elif rand <= 0.97:                  # 9% chance to have B blood type
        return 'B'
    else:                               # 3% chance to have AB blood type
        return 'AB'

def buildSet(numPairs, numDeceased):
    for i in range(1, numPairs + 1):
        print(livingDonorAge())

def main():
    buildSet(20, 1)

if __name__ == '__main__':
    main()