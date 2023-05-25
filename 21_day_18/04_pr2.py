from build_game import play_game


score = play_game()
flag = False
with open("Highscore.txt","r") as f:
    old_score = f.read()
    if old_score < str(score) :
        flag = True

if flag:
    with open("Heighscore.txt","w") as f:
        f.write(str(score))
