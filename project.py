import sys
import re
import random
import webbrowser
from snake import hungry_snake
from click import click_game

def greeting():
    
    print("Please insert first name and last name, or just first name.")
    while True:
        name=input("Name:").lstrip().rstrip()

        if "," in name.strip():
            last,first=name.split(",")
        
            if not first.strip().isalpha() or not last.strip().isalpha():
                print("Not a name.")
                continue
               
            elif name.count(" ")>1:
                print("Please insert first name and last name, or just first name.")
                continue
        
        elif " " in name:
            first,last=name.split(" ")
                    
            if not first.isalpha() or not last.isalpha():
                print("Not a name.")
                continue
    
        elif not " " in name and not name.isalpha():
            print("Not a name.")
            continue
        
        
        mood= input(f"Hello, {name}, how is your feeling day?")
        if not re.match(r"^(?!\d+$)[A-Za-z\s]*[A-Za-z\W\s_]+$", mood):
            print("Invalid input.")
            continue
    
        else:
            return "♡ Let's start with a survey to see your stress level."
        

def get_answer(answers):
    #questions from PSS4(Cohen et al. 1983)
    questions=["In the last month, how often have you felt that you were unable to control the important things in your life? \nA:Never;\nB:Almost never;\nC:Sometimes; \nD:Fairly often;\nE:Very often\n",
               "In the last month, how often have you felt confident about your ability to handle your personal problems? \nA:Never; \nB:Almost never;\nC:Sometimes;\nD:Fairly often;\nE:Very often\n",
               "In the last month, how often have you felt that things were going your way?\nA:Never;\nB:Almost never;\nC:Sometimes;\nD:Fairly often;\nE:Very often\n",
               "In the last month, how often have you felt difficulties were piling up so high that you could not overcome them?\nA:Never;\nB:Almost never;\nC:Sometimes;\nD:Fairly often;\nE:Very often\n"]
    
    print("Please answer with the correct corresponding letter.")
    for question in questions:
        while True:
            answer=input(question).upper()
            if answer in ["A","B","C","D","E"]:
                answers.append(answer)
                break
                
            print("Invalid answer, please enter A,B,C,D or E.")
    return answers
            
def result(answers):
    Q1_Q4={"A":0,"B":1,"C":2,"D":3,"E":4}
    Q2_Q3={"A":4,"B":3,"C":2,"D":1,"E":0}
    

    Q1=Q1_Q4.get(answers[0])
    Q2=Q2_Q3.get(answers[1])
    Q3=Q2_Q3.get(answers[2])
    Q4=Q1_Q4.get(answers[3])
    result=Q1+Q2+Q3+Q4
    
    if result in range(0,6):
        print(f"Excellent news! Stress level:{result}. \n You are in a state of optimal performance.\n A blank page is now available for you. \n Feel free to use it to document this positive data, or create a to-do list to make the most of your joyful energy.\n Let's make today productive and happy\n")
        return "low"
    
    elif result in range(6,11):
        print(f"How are you feeling? Stress level :{result}.\n This is within a manageable range, but a brief pause is recommended.\n Let's play a game together. I have several ready to launch to help reset your mood.\n")
        return "mid"
    
    elif result in range(11,17):
        print(f"Stress level :{result}.A high stress level has been detected.\n Let's take a break together. It's time to put down your work.\n I am now accessing my database for relaxing music to help you decompress.\n I'm here to help you get back to feeling balanced\n")
        return "high"
        
    
def low_open_file():
    diary= input("Welcome to write anything here.")
    with open("diary.txt", "a") as file:
        file.write(f"{diary}")
    

def mid_game_():
    game=random.choice([hungry_snake,click_game])
    game()
   
        
def high_music():
    url1="https://youtu.be/dImlzN_cqp4?si=hirWoTJ0TOUaC69T"
    url2="https://youtu.be/qYnA9wWFHLI?si=GgKG_H1BQ95dA9GQ"
    url3="https://www.youtube.com/live/LFASWuckB1c?si=O8_o2dOq9O7WNRwb"
    
    music=random.choice([url1,url2,url3])
    webbrowser.open(music)
    
  
def main():
    greeting()
    answers=[]
    answers=get_answer(answers)
    stress_level=result(answers)
    if stress_level=="low":
        low_open_file()
    
    elif stress_level=="mid":
        mid_game_()
        
    elif stress_level=="high":
        high_music()
        
if __name__ == "__main__":    
    main()
    
    