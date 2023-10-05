def rpg(exp,reward,threshold):
    if (exp+reward)>= threshold:
        print(True)
    else:
        print(False)
rpg(10,5,15)
