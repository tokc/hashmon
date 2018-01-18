def potion(user, opponent):   
    
    if user.hitpoints > user.maxhitpoints:
        pass
    elif user.hitpoints < user.maxhitpoints:
        user.hitpoints += 20

        if user.hipoints > user.maxhipoints:
            user.hitpoints = user.maxhipoints

    return "{} used POTION! HP rose to {}!".format(user.name, user.hitpoints)
