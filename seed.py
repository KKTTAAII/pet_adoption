from models import db,  connect_db, Pet


pet = Pet(name="Evie", species="lab/pit", 
photo_url=("https://scontent.fbkk5-7.fna.fbcdn.net/v/t1.6435-9/57203886_10219447323399692_50700"
        "9164032081920_n.jpg?_nc_cat=107&ccb=1-5&_nc_sid=84a396&_nc_ohc=l3HPE"
        "0i43-IAX92Ttr7&_nc_ht=scontent.fbkk5-7.fna&oh=20752200d516c1a02b84c4"
        "4f8c3e23b7&oe=61861CB3"), age=4, 
        notes="Evie loves chicken strips and likes other dogs and children")