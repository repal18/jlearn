
from flask import Flask, render_template, jsonify
import random
from datetime import date

app = Flask(__name__)

# ==========================================
# HALAMAN ASLI J-LEARN
# ==========================================

@app.route("/")
def home():
    return render_template("index.html", active="home")


@app.route("/belajar")
def belajar():
    return render_template("belajar.html", active="belajar")


@app.route("/kana")
def kana():
    return render_template("kana.html", active="belajar")


@app.route("/kosakata")
def kosakata():
    return render_template("kosakata.html", active="kosakata")


@app.route("/dojo")
def dojo():
    return render_template("dojo.html", active="dojo")


@app.route("/progress")
def progress():
    return render_template("progress.html", active="progress")


@app.route("/latihan")
def latihan():
    return render_template("latihan.html", active="latihan")


@app.route("/budaya")
def budaya():
    return render_template("budaya.html", active="budaya")


@app.route("/tentang")
def tentang():
    return render_template("tentang.html", active="tentang")


# ==========================================
# HTMX STUDY TIP
# ==========================================

@app.route("/htmx/tip")
def htmx_tip():
    tips = [
        "Baca kana dengan suara pelan. Mengucapkan membantu menguatkan ingatan.",
        "Coba ingat arti kata sebelum membalik flashcard.",
        "Belajar 10 menit secara konsisten lebih mudah dijaga daripada maraton semalam.",
        "Tulis satu contoh kalimat sederhana dari kosakata yang baru kamu pelajari."
    ]

    return f'''
    <div class="htmx-tip">
        <b>STUDY TIP</b>
        <span>{random.choice(tips)}</span>
    </div>
    '''


# ==========================================
# API STATUS
# ==========================================

@app.route("/api/ping")
def api_ping():
    return jsonify({
        "status": "ok",
        "project": "J-Learn SMKN 1 Lahat BY: King Repalodon",
        "message": "学習を続けよう！"
    })


# ==========================================
# J-STUDIO
# ==========================================

@app.route("/studio")
def studio():
    return render_template("studio.html", active="studio")


@app.route("/simulator")
def simulator():
    return render_template("simulator.html", active="studio")


@app.route("/grammar")
def grammar():
    return render_template("grammar.html", active="studio")


@app.route("/listening")
def listening():
    return render_template("listening.html", active="studio")


# ==========================================
# DAILY CHALLENGE API
# ==========================================

DAILY_CHALLENGES = [
    {
        "title": "The First Greeting",
        "task": "Pilih salam yang tepat untuk pagi hari.",
        "answer": "おはよう",
        "choices": [
            "こんばんは",
            "おはよう",
            "さようなら"
        ],
        "explanation": "おはよう (Ohayou) digunakan untuk menyapa pada pagi hari."
    },
    {
        "title": "At the Café",
        "task": "Kamu ingin meminta air. Pilih kata yang tepat.",
        "answer": "みず",
        "choices": [
            "みず",
            "ねこ",
            "ほん"
        ],
        "explanation": "みず (Mizu) berarti air."
    },
    {
        "title": "Meet a Teacher",
        "task": "Apa arti kata せんせい?",
        "answer": "Guru",
        "choices": [
            "Teman",
            "Guru",
            "Pelajar"
        ],
        "explanation": "せんせい (Sensei) berarti guru atau pengajar."
    },
    {
        "title": "Japanese Classroom",
        "task": "Apa arti がっこう?",
        "answer": "Sekolah",
        "choices": [
            "Rumah",
            "Sekolah",
            "Stasiun"
        ],
        "explanation": "がっこう (Gakkou) berarti sekolah."
    }
]


@app.route("/api/daily-challenge")
def daily_challenge():
    # Tantangan berubah berdasarkan tanggal.
    index = date.today().toordinal() % len(DAILY_CHALLENGES)

    return jsonify(DAILY_CHALLENGES[index])


# ==========================================
# RUN SERVER
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)
