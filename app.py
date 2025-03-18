from flask import Flask, request, render_template
import requests

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/z-fithers')
def z_fithers():
    return render_template('perguntas-z.html')

@app.route('/fithers')
def fithers():
    return render_template('perguntas-fither.html')

@app.route('/respostas-z', methods=['GET', 'POST'])
def respostas_z():

    if request.method == 'POST':

        resposta1 = int(request.form['q1'])
        resposta2 = int(request.form['q2'])
        resposta3 = int(request.form['q3'])
        resposta4 = int(request.form['q4'])
        resposta5 = int(request.form['q5'])

        soma_resposta = resposta1 + resposta2 + resposta3 + resposta4 + resposta5

        print(soma_resposta)
        # goku
        if soma_resposta <= 13:
            nome = 'goku'

            API_ENDPOINT = f'https://dragonball-api.com/api/characters?name={nome}'

            response = requests.get(API_ENDPOINT)
            if response.status_code == 200:
                data = response.json()

                nome = data[0]['name']
                imagem = data[0]['image']
            
                return render_template('resposta-z.html', nome=nome, imagem=imagem)
            else:
                print(response.status_code)
                return render_template('resposta-z.html', erro='Erro! não foi possivel gerar seu personagem!')
        # vegeta
        if soma_resposta <= 16:
            nome = 'vegeta'

            API_ENDPOINT = f'https://dragonball-api.com/api/characters?name={nome}'

            response = requests.get(API_ENDPOINT)
            if response.status_code == 200:
                data = response.json()

                nome = data[0]['name']
                imagem = data[0]['image']
            
                return render_template('resposta-z.html', nome=nome, imagem=imagem)
            else:
                print(response.status_code)
                return render_template('resposta-z.html', erro='Erro! não foi possivel gerar seu personagem!')
        # gohan
        if soma_resposta <= 19:
            nome = 'gohan'

            API_ENDPOINT = f'https://dragonball-api.com/api/characters?name={nome}'

            response = requests.get(API_ENDPOINT)
            if response.status_code == 200:
                data = response.json()

                nome = data[0]['name']
                imagem = data[0]['image']
            
                return render_template('resposta-z.html', nome=nome, imagem=imagem)
            else:
                print(response.status_code)
                return render_template('resposta-z.html', erro='Erro! não foi possivel gerar seu personagem!')
        
        # gotenks
        if soma_resposta <= 22:
            nome = 'gotenks'

            API_ENDPOINT = f'https://dragonball-api.com/api/characters?name={nome}'

            response = requests.get(API_ENDPOINT)
            if response.status_code == 200:
                data = response.json()

                nome = data[0]['name']
                imagem = data[0]['image']
            
                return render_template('resposta-z.html', nome=nome, imagem=imagem)
            else:
                print(response.status_code)
                return render_template('resposta-z.html', erro='Erro! não foi possivel gerar seu personagem!')
        
        # trunks
        if soma_resposta <= 25:
            nome = 'trunks'

            API_ENDPOINT = f'https://dragonball-api.com/api/characters?name={nome}'

            response = requests.get(API_ENDPOINT)
            if response.status_code == 200:
                data = response.json()

                nome = data[0]['name']
                imagem = data[0]['image']
            
                return render_template('resposta-z.html', nome=nome, imagem=imagem)
            else:
                print(response.status_code)
                return render_template('resposta-z.html', erro='Erro! não foi possivel gerar seu personagem!')
        
        # bardock
        if soma_resposta <= 28:
            nome = 'bardock'

            API_ENDPOINT = f'https://dragonball-api.com/api/characters?name={nome}'

            response = requests.get(API_ENDPOINT)
            if response.status_code == 200:
                data = response.json()

                nome = data[0]['name']
                imagem = data[0]['image']
            
                return render_template('resposta-z.html', nome=nome, imagem=imagem)
            else:
                print(response.status_code)
                return render_template('resposta-z.html', erro='Erro! não foi possivel gerar seu personagem!')
        
        # raditz
        if soma_resposta <= 31:
            nome = 'raditz'

            API_ENDPOINT = f'https://dragonball-api.com/api/characters?name={nome}'

            response = requests.get(API_ENDPOINT)
            if response.status_code == 200:
                data = response.json()

                nome = data[0]['name']
                imagem = data[0]['image']
            
                return render_template('resposta-z.html', nome=nome, imagem=imagem)
            else:
                print(response.status_code)
                return render_template('resposta-z.html', erro='Erro! não foi possivel gerar seu personagem!')
        
        # gogeta
        if soma_resposta <= 34:
            nome = 'gogeta'

            API_ENDPOINT = f'https://dragonball-api.com/api/characters?name={nome}'

            response = requests.get(API_ENDPOINT)
            if response.status_code == 200:
                data = response.json()

                nome = data[0]['name']
                imagem = data[0]['image']
            
                return render_template('resposta-z.html', nome=nome, imagem=imagem)
            else:
                print(response.status_code)
                return render_template('resposta-z.html', erro='Erro! não foi possivel gerar seu personagem!')
        
        

        # vegetto
        if soma_resposta <= 37:
                nome = 'vegetto'

                API_ENDPOINT = f'https://dragonball-api.com/api/characters?name={nome}'

                response = requests.get(API_ENDPOINT)
                if response.status_code == 200:
                    data = response.json()

                    nome = data[0]['name']
                    imagem = data[0]['image']
                
                    return render_template('resposta-z.html', nome=nome, imagem=imagem)
                else:
                    print(response.status_code)
                    return render_template('resposta-z.html', erro='Erro! não foi possivel gerar seu personagem!')
        # broly
        if soma_resposta <= 40:
                nome = 'broly'

                API_ENDPOINT = f'https://dragonball-api.com/api/characters?name={nome}'

                response = requests.get(API_ENDPOINT)
                if response.status_code == 200:
                    data = response.json()

                    nome = data[0]['name']
                    imagem = data[0]['image']
                
                    return render_template('resposta-z.html', nome=nome, imagem=imagem)
                else:
                    print(response.status_code)
                    return render_template('resposta-z.html', erro='Erro! não foi possivel gerar seu personagem!')
                
    return render_template('resposta-z.html')            

if __name__ == '__main__':
    app.run(debug=True)
