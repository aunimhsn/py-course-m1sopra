import json

def swiss_system_func(filepath:str) -> list[list[dict]]:
    with open(filepath, 'r') as f:
        players:list = json.load(f)

    players_sorted = sorted(players, key=lambda x: x['elo_points'])

    s1 = players_sorted[:3]
    s2 = players_sorted[3:]

    versus = [[s1[i], s2[i]] for i in range(0, len(s1))]
    # Équivalent de la liste en compréhension
    # for i in range(0, len(s1)):
    #     versus.append([s1[i], s2[i]])

    return versus

versus = swiss_system_func('./players.json')
with open('versus.json', 'w') as f:
    json.dump(versus, f, indent=4)