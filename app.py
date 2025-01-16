from flask import Flask, render_template, request
import sqlite3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Vaada World!"

if __name__ == "__main__":
    # 0.0.0.0 ile Flask'ı dış bağlantılara aç ve Render'ın beklentisi olan 5000 portunda çalıştır
    app.run(host="0.0.0.0", port=5000)

app = Flask(__name__)

# Veritabanı bağlantısı ve tablo oluşturma
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            referrals INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

# Flask başlarken veritabanını başlat
init_db()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/game")
def game():
    return render_template("game.html")

@app.route("/rank")
def rank():
    # Kullanıcıları referans sayısına göre sıralıyoruz
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT username, referrals FROM users ORDER BY referrals DESC")
    sorted_users = cursor.fetchall()
    conn.close()
    return render_template("rank.html", users=sorted_users)

@app.route("/add_referral", methods=["POST"])
def add_referral():
    username = request.form.get("username")  # Kullanıcı adı formdan alınır
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Kullanıcı varsa referans sayısını artır, yoksa yeni kullanıcı ekle
    cursor.execute("""
        INSERT INTO users (username, referrals)
        VALUES (?, 1)
        ON CONFLICT(username) DO UPDATE SET referrals = referrals + 1
    """, (username,))
    conn.commit()
    conn.close()
    return "Referral added successfully!"

if __name__ == "__main__":
    app.run(debug=True)
