import pickle

with open('cndnsdASL.pkl', 'rb') as f:
    cndnsdASL = pickle.load(f)

newCndnsdASL = []
for song in cndnsdASL:
    if song[1] != 'Genesis':
        newCndnsdASL.append(song)

f = open("noGenCndnsdASL.pkl","wb")
pickle.dump(newCndnsdASL,f)
f.close()
