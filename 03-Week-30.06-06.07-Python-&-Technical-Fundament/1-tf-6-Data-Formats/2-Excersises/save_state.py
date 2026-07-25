import pickle

# Anwendungszustand
app_state = {
    "user": "rick",
    "level": 5,
    "inventory": ["grandson", "time-machine"]
}

# Zustand speichern
with open('saved_state.pkl', 'wb') as f:
    pickle.dump(app_state, f)

print("State saved.")
