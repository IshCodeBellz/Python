import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
given_answers = []
score = 0

while len(given_answers) < 50:
    answer_state = screen.textinput(title=f"{len(given_answers)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "exit":
        # missing_states = []
        # for state in all_states:
        #     if state not in given_answers:
        #         missing_states.append(state)
        missing_states = [state for state in all_states if state not in given_answers]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        print(missing_states)
        break

    if answer_state in all_states:
        given_answers.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(answer_state)
        print("Correct")

screen.exitonclick()