from flask import Flask, render_template

app = Flask(__name__)



constitution = "B"

@app.route('/')
def index():
    box1_image = f"/static/{constitution}_Party_1/{constitution}_C1.png"
    box2_image = f"/static/{constitution}_Party_1/Party_1.png"
    box5_image = f"/static/{constitution}_Party_2/{constitution}_C2.png"
    box6_image = f"/static/{constitution}_Party_2/Party_2.png"

    box3_text = "yoyoyoyo"
    box7_text = "boboboboob"

    return render_template('index.html', box1_image=box1_image, box2_image=box2_image,
                           box5_image=box5_image, box6_image=box6_image,
                           box3_text=box3_text, box7_text=box7_text)




if __name__ == '__main__':
    app.run(debug=True)
