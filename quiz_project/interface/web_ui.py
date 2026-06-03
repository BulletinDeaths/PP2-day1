from flask import Flask, render_template, request, redirect, url_for, session
from business_logic.question_generator import QuestionGenerator
from business_logic.answer_processor import AnswerProcessor
from business_logic.score_manager import ScoreManager

app = Flask(__name__)
app.secret_key = 'a_very_secret_key_for_sessions' # Ключ для шифрования сессий

# Создаем экземпляры классов бизнес-логики один раз при запуске сервера
q_gen = QuestionGenerator()
ans_proc = AnswerProcessor()


@app.route('/', methods=['GET'])
def index():
    """
    Главная страница. Показывает текущий вопрос.
    """
    # Инициализируем состояние игры в сессии пользователя
    if 'score_manager' not in session or 'current_q_num' not in session:
        session['score_manager'] = ScoreManager().__dict__ # Сохраняем атрибуты как словарь
        session['current_q_num'] = 1
        session.modified = True

    total_questions = len(q_gen.questions)
    current_q_num = session['current_q_num']

    if current_q_num > total_questions:
        return redirect(url_for('result'))

    question_data = q_gen.get_random_question()
    return render_template(
        'index.html',
        question=question_data,
        current_q_num=current_q_num,
        total_questions=total_questions
    )


@app.route('/submit', methods=['POST'])
def submit():
    """
    Обрабатывает отправку формы с ответом.
    """
    user_answer = request.form.get('answer')
    # Получаем все поля формы, включая скрытые данные вопроса
    question_data = {k: v for k, v in request.form.items()}

    # Восстанавливаем объект ScoreManager из словаря в сессии
    score_mgr = ScoreManager()
    score_mgr.__dict__.update(session['score_mgr'])

    is_correct = ans_proc.check_answer(question_data, user_answer)
    points = int(question_data['points'])

    if is_correct:
        score_mgr.add_points(points)
    else:
        score_mgr.subtract_points(points)

    # Сохраняем обновленное состояние обратно в сессию
    session['score_mgr'] = score_mgr.__dict__
    session['current_q_num'] += 1
    session.modified = True

    return redirect(url_for('index'))


@app.route('/result')
def result():
    """
    Отображает финальный результат игры.
    """
    final_score = ScoreManager(**session['score_mgr']).get_current_score()
    return render_template('result.html', final_score=final_score)