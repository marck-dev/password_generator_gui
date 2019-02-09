import eel as app
from core import generator as gen

app.init("app/view")

# func for gen the pass and return
@app.expose
def ev(leng):
    app.setPass(get_pass(leng))
def get_pass( length ):
    pas_gen = gen( length )
    pas_gen.generate() #generate the pass
    password = pas_gen.get_password() # get the pass
    del(pas_gen)
    return password


# init the app
app.start("index.html")

