import pickle

# Zustand laden
with open('saved_state.pkl', 'rb') as f:
    loaded_state = pickle.load(f)

print("Loaded state:", loaded_state)
print("User:", loaded_state["user"])
