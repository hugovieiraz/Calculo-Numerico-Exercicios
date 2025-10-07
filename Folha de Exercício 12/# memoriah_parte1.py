# app.py
from flask import Flask, render_template, request, redirect, url_for, session

# Cria a aplicação Flask
app = Flask(__name__)
# Chave secreta para gerenciar a sessão do usuário (essencial para guardar a pontuação)
app.secret_key = 'sua_chave_secreta_super_dificil'

# --- DADOS DO QUIZ ---
# Em um projeto real, isso viria de um banco de dados.
# Por enquanto, vamos deixar aqui para simplificar.
QUIZ_PERGUNTAS = [
    {
        "id": 1,
        "texto": "Qual destas é a Segunda Lei de Newton?",
        "opcoes": ["A) Princípio da Inércia", "B) Princípio Fundamental da Dinâmica", "C) Princípio da Ação e Reação"],
        "resposta_correta": "B) Princípio Fundamental da Dinâmica"
    },
    {
        "id": 2,
        "texto": "Qual a unidade de medida de Força no Sistema Internacional?",
        "opcoes": ["A) Pascal", "B) Joule", "C) Newton"],
        "resposta_correta": "C) Newton"
    },
    {
        "id": 3,
        "texto": "A energia associada ao movimento dos corpos é chamada de:",
        "opcoes": ["A) Energia Potencial", "B) Energia Cinética", "C) Energia Térmica"],
        "resposta_correta": "B) Energia Cinética"
    }
]

# --- ROTAS DO SITE ---

# Rota para a página inicial
@app.route('/')
def index():
    # Renderiza o arquivo HTML da página inicial
    return render_template('index.html')

# Rota para iniciar o quiz (limpa os dados da sessão)
@app.route('/start')
def start_quiz():
    session['pontuacao'] = 0
    session['moedas_laps'] = 0
    session['pergunta_atual_id'] = 0 # Usaremos o índice da lista
    return redirect(url_for('pergunta'))

# Rota principal do quiz
@app.route('/quiz', methods=['GET', 'POST'])
def pergunta():
    pergunta_id = session.get('pergunta_atual_id', 0)

    # Se o quiz acabou, redireciona para a página de resultados
    if pergunta_id >= len(QUIZ_PERGUNTAS):
        return redirect(url_for('resultado'))

    pergunta_atual = QUIZ_PERGUNTAS[pergunta_id]

    # Se o usuário enviou uma resposta (método POST)
    if request.method == 'POST':
        resposta_usuario = request.form.get('resposta')
        
        # Verifica se a resposta está correta
        if resposta_usuario == pergunta_atual['resposta_correta']:
            session['pontuacao'] += 100
            session['moedas_laps'] += 25
        
        # Avança para a próxima pergunta
        session['pergunta_atual_id'] += 1
        return redirect(url_for('pergunta'))

    # Se for apenas para carregar a página (método GET)
    return render_template('quiz.html', pergunta=pergunta_atual)

# Rota para a página de resultados
@app.route('/resultado')
def resultado():
    pontuacao = session.get('pontuacao', 0)
    laps = session.get('moedas_laps', 0)
    return render_template('resultado.html', pontuacao_final=pontuacao, laps_ganhos=laps)

# Roda a aplicação
if __name__ == '__main__':
    app.run(debug=True)