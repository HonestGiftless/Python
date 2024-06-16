# You will not pass

import pickle

def filter_dump(filename, objects, typename):
    with open(filename, "wb") as file:
        result = [i for i in objects if type(i) is typename]
        pickle.dump(result, file)