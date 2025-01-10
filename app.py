# app.py

from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import os

# language.py'deki çeviri sözlüğü
from language import translations

# python/main.py içindeki analiz fonksiyonları
from python.main import perform_analysis_once, run_analysis

app = Flask(__name__)
app.secret_key = "super_secret_key_123"  # Session için bir secret key gerekli

# Sunucu başlamadan önce "main.py" analizini bir kez yap
perform_analysis_once()


@app.before_request
def set_default_language():
    """
    Her istek öncesi, session'da 'lang' yoksa, varsayılan 'tr' yapıyoruz.
    """
    if 'lang' not in session:
        session['lang'] = 'tr'


@app.route("/change_language", methods=["POST"])
def change_language():
    """
    Dil değiştirildiğinde, seçilen dili session'a kaydediyoruz,
    sonra geldiğimiz sayfaya geri dönüyoruz.
    """
    selected_lang = request.form.get("language", "")
    if selected_lang in ["tr", "en"]:
        session['lang'] = selected_lang
    return redirect(request.referrer or url_for('index'))


@app.route("/")
def index():
    lang = session.get('lang', 'tr')
    common_texts = translations[lang]['common']
    page_texts = translations[lang]['index']
    return render_template("index.html",
                           common=common_texts,
                           texts=page_texts)


@app.route("/hakkinda")
def hakkinda():
    lang = session.get('lang', 'tr')
    common_texts = translations[lang]['common']
    page_texts = translations[lang]['about']
    return render_template("hakkında.html",
                           common=common_texts,
                           texts=page_texts)


@app.route("/veriMadenciligi")
def veriMadenciligi():
    lang = session.get('lang', 'tr')
    common_texts = translations[lang]['common']
    page_texts = translations[lang]['veriMadenciligi']
    return render_template("veriMadenciliği.html",
                           common=common_texts,
                           texts=page_texts)


# Grafik buton tıklayınca tetiklenen endpoint
@app.route("/show_graph")
def show_graph():
    graph_type = request.args.get("graph_type", "")
    img_path = run_analysis(graph_type)
    return jsonify({"img_path": img_path})


if __name__ == "__main__":
    app.run(debug=True)
