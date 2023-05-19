from build_game import play_game

score = play_game()


with open("highscore.txt","r") as f:
    content = f.readline()
    if score > int(content):
        with open("highscore.txt", "w") as f2:
            f2.write(str(score))
