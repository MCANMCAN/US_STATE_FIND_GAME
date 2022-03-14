from turtle import Turtle ,Screen
import pandas 
turtle=Turtle()
screen= Screen()
screen.setup(600,600)
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
pencil = Turtle()
turtle.color("black")
pencil.penup()
game_on = True 
score = 0 
answer_list = []
text_input = ""
pencil.hideturtle()
data_csv = pandas.read_csv("50_states.csv") 
state_list = data_csv.state.to_list()
#print(df)
correct_answers = []
while game_on == True :  
    if text_input == "Exit":
       game_on = False
       print("text_input")
    else : 
       if score == 0 : 
            text_input = screen.textinput(title="Game Started :)",prompt="Enter your state guess...") 
       else : 
            text_input = screen.textinput(title=f"{score}/50 state found",prompt="Enter your state guess...") 
       text_input = text_input.title()    
       print(text_input)   
       if text_input in state_list and text_input not in correct_answers: 
           correct_row = data_csv[data_csv.state == text_input]
           correct_answers.append(text_input)
           x = int(correct_row["x"])
           y = int(correct_row["y"])
           pencil.goto(x,y)
           pencil.write(f"{text_input.title()}")
           score +=1
missing_answer = [state for state in state_list if state not in correct_answers] 
missing_answer_dict = {"Missing States" : missing_answer}
df = pandas.DataFrame.from_dict(missing_answer_dict)
df.to_csv("gen.csv",index=False,header=True)
screen.exitonclick()
