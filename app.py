from flask import Flask, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "pulsetweet_admin_secret"

LOGO = "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSiuMR2cDYGg7GZih0jICl9EXUM5tmSdCk70m6Se7smOSafAkNBSeW1HFTWsDda-wlJXsc17zfb"

# ---------------- DATABASE CONNECTION ----------------
mycon = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="yuwin2008",
    database="Pulse"
)
cur = mycon.cursor()

# ---------------- THEME + ICONS ----------------
STYLE = f"""
<link rel="stylesheet"
 href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

<style>
body {{
    margin: 0;
    font-family: 'Segoe UI', Arial;
    background: linear-gradient(to bottom, #f3e7ff, #e6ecf0);
}}

.navbar {{
    background: linear-gradient(90deg, #6a11cb, #2575fc);
    padding: 15px 20px;
    color: white;
    font-size: 22px;
    font-weight: bold;
}}
.navbar img {{
    vertical-align: middle;
    margin-right: 8px;
}}
.navbar a {{
    float: right;
    color: white;
    text-decoration: none;
    margin-left: 20px;
    font-size: 14px;
}}

.container {{
    width: 50%;
    margin: auto;
    margin-top: 25px;
}}

.form-box, .tweet-box {{
    background: white;
    padding: 16px;
    border-radius: 18px;
    margin-bottom: 18px;
    box-shadow: 0 5px 15px rgba(106,17,203,0.25);
}}

.tweet-user {{
    font-weight: bold;
    color: #6a11cb;
}}

.like-btn {{
    color: #9b2cfc;
    text-decoration: none;
    font-weight: bold;
}}

.delete-btn {{
    background: linear-gradient(90deg, #ff416c, #ff4b2b);
    color: white;
    padding: 4px 12px;
    border-radius: 20px;
    text-decoration: none;
    font-size: 12px;
}}

textarea {{
    width: 100%;
    border-radius: 12px;
    padding: 10px;
    border: 1px solid #ccc;
    resize: none;
}}

button {{
    background: linear-gradient(90deg, #6a11cb, #2575fc);
    color: white;
    border: none;
    padding: 9px 18px;
    border-radius: 25px;
    margin-top: 10px;
    float: right;
}}

.card {{
    background: white;
    width: 330px;
    margin: 120px auto;
    padding: 30px;
    border-radius: 18px;
    box-shadow: 0 15px 30px rgba(106,17,203,0.3);
    text-align: center;
}}
.card img {{
    width: 90px;
}}
.card input {{
    width: 92%;
    padding: 10px;
    margin: 10px 0;
}}
.card button {{
    width: 95%;
}}
</style>
"""

# ---------------- HOME ----------------
@app.route('/')
def home():
    return redirect('/login')

# ---------------- REGISTER ----------------
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        cur.execute(
            "INSERT INTO Users (username, password_hash, email) VALUES (%s,%s,%s)",
            (request.form['username'],
             request.form['password'],
             request.form['email'])
        )
        mycon.commit()
        return redirect('/login')

    return f"""
    <html><head>{STYLE}</head><body>
    <div class="card">
        <img src="{LOGO}">
        <h2>Create Account</h2>
        <form method="post">
            <input name="username" placeholder="Username" required>
            <input name="password" type="password" placeholder="Password" required>
            <input name="email" placeholder="Email" required>
            <button><i class="fa-solid fa-user-plus"></i> Register</button>
        </form>
    </div>
    </body></html>
    """

# ---------------- LOGIN ----------------
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        cur.execute(
            "SELECT user_id FROM Users WHERE username=%s AND password_hash=%s",
            (request.form['username'], request.form['password'])
        )
        user = cur.fetchone()
        if user:
            session['user_id'] = user[0]
            session['username'] = request.form['username']
            return redirect('/feed')
        return "<h3 align='center'>Invalid Login</h3>"

    return f"""
    <html><head>{STYLE}</head><body>
    <div class="card">
        <img src="{LOGO}">
        <h2>Pulse</h2>
        <form method="post">
            <input name="username" placeholder="Username">
            <input name="password" type="password" placeholder="Password">
            <button><i class="fa-solid fa-right-to-bracket"></i> Login</button>
        </form>
        <br>
        <a href="/register">Register</a><br><br>
        <a href="/admin">Admin Login</a>
    </div>
    </body></html>
    """

# ---------------- FEED ----------------
@app.route('/feed', methods=['GET','POST'])
def feed():
    if 'user_id' not in session:
        return redirect('/login')

    if request.method == 'POST':
        cur.execute(
            "INSERT INTO Posts (user_id, content) VALUES (%s,%s)",
            (session['user_id'], request.form['tweet'])
        )
        mycon.commit()
        return redirect('/feed')

    cur.execute("""
        SELECT p.post_id, u.username, p.content, p.likes
        FROM Posts p JOIN Users u ON p.user_id=u.user_id
        ORDER BY p.post_id DESC
    """)
    tweets = cur.fetchall()

    html = f"""
    <html><head>{STYLE}</head><body>
    <div class="navbar">
        <img src="{LOGO}" width="32">
        Pulse
        <a href="/logout">Logout</a>
    </div>

    <div class="container">
        <div class="form-box">
            <form method="post">
                <textarea name="tweet" rows="3" maxlength="280"
                placeholder="Share something..."></textarea>
                <button>Post</button>
            </form>
        </div>
    """

    for t in tweets:
        html += f"""
        <div class="tweet-box">
            <div class="tweet-user">@{t[1]}</div>
            {t[2]}<br><br>
            ❤️ {t[3]}
            <a class="like-btn" href="/like/{t[0]}">Like</a>
        </div>
        """

    html += "</div></body></html>"
    return html

# ---------------- LIKE ----------------
@app.route('/like/<int:pid>')
def like(pid):
    cur.execute("UPDATE Posts SET likes = likes + 1 WHERE post_id=%s", (pid,))
    mycon.commit()
    return redirect('/feed')

# ---------------- ADMIN ----------------
@app.route('/admin', methods=['GET','POST'])
def admin():
    if request.method == 'POST' and request.form['password'] == "godofthunder2407":
        session['admin'] = True
        return redirect('/adminpanel')

    return f"""
    <html><head>{STYLE}</head><body>
    <div class="card">
        <img src="{LOGO}">
        <h2>Admin Login</h2>
        <form method="post">
            <input name="password" type="password" placeholder="Admin Password">
            <button>Login</button>
        </form>
    </div>
    </body></html>
    """

# ---------------- ADMIN PANEL ----------------
@app.route('/adminpanel')
def adminpanel():
    if 'admin' not in session:
        return redirect('/admin')

    cur.execute("""
        SELECT p.post_id, u.username, p.content
        FROM Posts p JOIN Users u ON p.user_id=u.user_id
        ORDER BY p.post_id DESC
    """)
    posts = cur.fetchall()

    html = f"""
    <html><head>{STYLE}</head><body>
    <div class="navbar">
        Admin Panel
        <a href="/logout">Logout</a>
    </div>
    <div class="container">
    """

    for p in posts:
        html += f"""
        <div class="tweet-box">
            <b>@{p[1]}</b><br><br>
            {p[2]}<br><br>
            <a class="delete-btn" href="/delete/{p[0]}">Delete</a>
        </div>
        """

    html += "</div></body></html>"
    return html

# ---------------- DELETE ----------------
@app.route('/delete/<int:pid>')
def delete(pid):
    cur.execute("DELETE FROM Posts WHERE post_id=%s", (pid,))
    mycon.commit()
    return redirect('/adminpanel')

# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

# ---------------- RUN ----------------
if __name__ == '__main__':
    app.run(debug=True)
