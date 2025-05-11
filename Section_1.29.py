import pickle

scores = {
    'player1': 1500,
    'player2': 2300,
    'player3': 1900
}

# Save
with open("scores.pkl", "wb") as f:
    pickle.dump(scores, f)

# Load
with open("scores.pkl", "rb") as f:
    loaded_scores = pickle.load(f)

print("Loaded scores:", loaded_scores)
