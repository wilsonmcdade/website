from flask import Flask, request, render_template
from app import app

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    posts = [
            {
                'url':'rtl',
                'title':'Decoding satellite transmissions recieved by a consumer Software-Defined Radio',
                'para':'I used a 25 dollar software-defined radio connected to homemade antennas in order to recieve radio transmissions from airplanes and satellites.',
                'picsrc':'pic03.jpg',
                'text':[
                    "Slippery when panickin', this seems like surfin' gasoline at the mercy of my discrepancy I've got countless current identities Which one should I pretend to be? Which will be the end of me? Fuck my present coordinates I will 'em dead like, like, like, like, like, like, like it's not what you think fuck you want from us? We're the same as you but we know we're fucked but we came as you, like you know it's us and your mind, not you",
                    "This ghost town's my compound, I'm a saboteur your town's my smoke cloud, I stay at war by night shift I don't exist, chump, saddle up a dust to dust motionless struck belly up your skies are lip balm on my balls elemental cyclotron on white walls i met you and your carne asada to cry fuck everything, now go ahead and pay us for my shrine, wait this ghost town's my compound, I'm a saboteur your town's my smoke cloud, I stay at war by night shift I don't exist, chump, saddle up a dust to dust motionless struck belly up birch wood emoji wrought with human branches your innocence save your hopes, I just throw the dice and I've been like this for my whole fucking life my whole fucking life's your whole fucking life"
                    ]
            }
            ]
    return render_template('index.html', posts=posts)

if __name__ == "__main__":
    app.run(debug=True)
