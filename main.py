import random

def generate_matches(participants):
    random.shuffle(participants)
    matches = []
    
    for i in range(0, len(participants), 2):
        match = (participants[i], participants[i+1])
        matches.append(match)
    
    return matches

def conduct_round(matches):
    winners = []
    
    for match in matches:
        winner = input(f"Who wins between {match[0]} and {match[1]}? ")
        winners.append(winner)
    
    return winners

def run_tournament(participants):
    round_number = 1
    
    while len(participants) > 1:
        print(f"\nRound {round_number}")
        
        matches = generate_matches(participants)
        winners = conduct_round(matches)
        
        participants = winners
        round_number += 1
    
    print(f"\nWinner of the tournament: {participants[0]}")

# Example usage:
participants_list = [f"Player{i}" for i in range(1, 51)]
run_tournament(participants_list)
