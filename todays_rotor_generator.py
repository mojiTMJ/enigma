
import random
import pickle

# Alphabet String
alphabet = 'abcdefghijklmnopqrstuwxyz'

# Create Random Rotor 1
r1 = list(alphabet)
random.shuffle(r1)
r1 = ''.join(r1)

# Create Random Rotor 2
r2 = list(alphabet)
random.shuffle(r2)
r2 = ''.join(r2)

# Create Random Rotor 3
r3 = list(alphabet)
random.shuffle(r3)
r3 = ''.join(r3)

# Create Pickle file
f = open('./todays_rotor_state.enigma', 'wb')
pickle.dump((r1, r3, r3), f)
f.close
