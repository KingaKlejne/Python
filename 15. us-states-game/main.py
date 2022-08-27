import turtle as t
import pandas as pd

screen = t.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)

df = pd.read_csv("50_states.csv")
states_list = df["state"].to_list()
correct_answers = []

while len(correct_answers) < 50:
    answer_state = screen.textinput(title = f"{len(correct_answers)} / 50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in states_list:
        guessed_row = df[df.state == answer_state]
        answer = t.Turtle()
        answer.hideturtle()
        answer.penup()
        answer.setpos(int(guessed_row.x), int(guessed_row.y))
        answer.write(answer_state)
        correct_answers.append(answer_state)


for answer in correct_answers:
    states_list.remove(answer)

df_to_learn = pd.DataFrame(states_list)
df_to_learn.to_csv("States to learn.csv")