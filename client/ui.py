from flask import Flask, render_template
import json
app = Flask(__name__)




constitution = "A"
@app.route('/')
def index():
    box1_image = f"/static/{constitution}_Party_1/{constitution}_C1.png"
    box2_image = f"/static/{constitution}_Party_1/Party_1.png"
    box5_image = f"/static/{constitution}_Party_2/{constitution}_C2.png"
    box6_image = f"/static/{constitution}_Party_2/Party_2.png"
    
    name1, party1 = text_P1(constitution)
    box3_text = f"{name1} {party1}"

    name2, party2 = text_P2(constitution)
    box7_text = f"{name2} {party2}"
    
    return render_template('index.html', box1_image=box1_image, box2_image=box2_image,
                           box5_image=box5_image, box6_image=box6_image,
                           box3_text=box3_text, box7_text=box7_text)

def text_P1(constitution):
    with open(f"{constitution}_Party_1.json","r") as file:
        data = json.load(file)
        name1 = data.get("Name")
        party1 = data.get("Party_Name")
    return name1, party1

def text_P2(constitution):
    with open(f"{constitution}_Party_2.json","r") as file:
        data = json.load(file)
        name2 = data.get("Name")
        party2 = data.get("Party_Name")
    return name2, party2
    

if __name__ == '__main__':
    app.run(debug=True)
