#영구저장 이진모드 접근권장

import pickle
favorite_color = {"lion" : "yellow", "kitty" : "red"}
pickle.dump(favorite_color, open("save.pkl","wb"))
favorite_color_load = pickle.load(open("save.pkl","rb"))
favorite_color_load
# {" kitty" : "red" , "lion" : "yellow"}
print(favorite_color_load["kitty"],favorite_color_load["lion"])

# ('red','yellow')