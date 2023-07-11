from flask import render_template, request
from app import app
from .forms import SignUpForm, SearchForm
import requests, json


@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/signup', methods=["GET", "POST"])
def signup_page():
    form = SignUpForm()
    print(request)
    if request.method == "POST":
        if form.validate():
            username = form.username.data
            password = form.password.data
            email = form.email.data
            print(username, email, password)
        else:
            print('Form invalid')
    return render_template('signup.html', form = form)

@app.route('/lookup', methods=["GET", "POST"])
def lookup_page():
    form = SearchForm()
    if request.method == "POST":
        output = {}

        search_query = (form.query.data).lower()
        poke_info = requests.get(f"https://pokeapi.co/api/v2/pokemon/{search_query}").json()
        poke_sprites = requests.get(f"https://pokeapi.co/api/v2/pokemon-form/{search_query}/").json()

        poke_name = poke_info['forms'][0]['name']
        poke_ability = poke_info['abilities'][0]['ability']['name']
        poke_def = poke_info['stats'][2]['base_stat']
        poke_att = poke_info['stats'][1]['base_stat']
        poke_hp = poke_info['stats'][0]['base_stat']
        poke_sprite_male = poke_sprites['sprites']['front_shiny']
        poke_sprite_female = poke_sprites['sprites']['front_shiny_female']

        output.update({'Name':poke_name,'Ability':poke_ability,'Base HP':poke_hp,'Base Attack':poke_att,'Base Defense':poke_def,'Male Shiny Sprite':poke_sprite_male,'Female Shiny Sprite':poke_sprite_female})
        
        return output
    return render_template('lookup.html', form=form)

# @app.route('/lookup_result', methods=["GET"])
# def lookup_result():
#     response = print(requests.get("https://pokeapi.co/api/v2/pokemon/mankey").json()['base_experience'])
#     return render_template('lookup_result.html')


    