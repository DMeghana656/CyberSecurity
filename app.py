from flask import render_template, request, redirect, url_for, session, flash
from config import app, mysql
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute(
            """
            SELECT * FROM users
            WHERE username=%s AND password=%s
            """,
            (username, password)
        )
        user = cur.fetchone()
        if user:
            session['username'] = username
            cur.execute(
                "INSERT INTO logs(username,activity) VALUES(%s,%s)",
                (username, "Logged In")
            )
            mysql.connection.commit()
            return redirect('/dashboard')
        else:
            flash("Invalid Username or Password")
    return render_template('login.html')
@app.route('/logout')
def logout():
    username = session.get('username')
    if username:
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO logs(username,activity) VALUES(%s,%s)",
            (username, "Logged Out")
        )
        mysql.connection.commit()
    session.clear()
    return redirect('/')
@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect('/')
    cur = mysql.connection.cursor()
    cur.execute("SELECT COUNT(*) FROM assets")
    asset_count = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM vpcs")
    vpc_count = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM security_rules")
    rule_count = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM alerts")
    alert_count = cur.fetchone()[0]
    return render_template(
        'dashboard.html',
        asset_count=asset_count,
        vpc_count=vpc_count,
        rule_count=rule_count,
        alert_count=alert_count
    )
@app.route('/assets')
def assets():
    if 'username' not in session:
        return redirect('/')
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM assets")
    data = cur.fetchall()
    return render_template(
        'assets.html',
        assets=data
    )
@app.route('/add_asset', methods=['POST'])
def add_asset():
    asset_name = request.form['asset_name']
    asset_type = request.form['asset_type']
    location = request.form['location']
    status = request.form['status']
    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO assets(asset_name,asset_type,location,status)
        VALUES(%s,%s,%s,%s)
    """, (asset_name, asset_type, location, status))
    mysql.connection.commit()
    return redirect('/assets')
@app.route('/vpcs')
def vpcs():
    if 'username' not in session:
        return redirect('/')
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM vpcs")
    data = cur.fetchall()
    return render_template(
        'vpcs.html',
        vpcs=data
    )
@app.route('/add_vpc', methods=['POST'])
def add_vpc():
    vpc_name = request.form['vpc_name']
    subnet = request.form['subnet']
    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO vpcs(vpc_name,subnet) VALUES(%s,%s)",
        (vpc_name, subnet)
    )
    mysql.connection.commit()
    return redirect('/vpcs')
@app.route('/security_groups')
def security_groups():
    if 'username' not in session:
        return redirect('/')
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM security_rules")
    data = cur.fetchall()
    return render_template(
        'security_groups.html',
        rules=data
    )
@app.route('/add_rule', methods=['POST'])
def add_rule():
    port = request.form['port']
    protocol = request.form['protocol']
    action = request.form['action']
    cur = mysql.connection.cursor()
    cur.execute(
        """
        INSERT INTO security_rules(port,protocol,action)
        VALUES(%s,%s,%s)
        """,
        (port, protocol, action)
    )
    mysql.connection.commit()
    return redirect('/security_groups')
@app.route('/alerts')
def alerts():
    if 'username' not in session:
        return redirect('/')
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM alerts")
    data = cur.fetchall()
    return render_template(
        'alerts.html',
        alerts=data
    )
@app.route('/add_alert', methods=['POST'])
def add_alert():
    message = request.form['message']
    severity = request.form['severity']
    cur = mysql.connection.cursor()
    cur.execute(
        """
        INSERT INTO alerts(message,severity)
        VALUES(%s,%s)
        """,
        (message, severity)
    )
    mysql.connection.commit()
    return redirect('/alerts')
@app.route('/logs')
def logs():
    if 'username' not in session:
        return redirect('/')
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT *
        FROM logs
        ORDER BY created_at DESC
    """)
    data = cur.fetchall()
    return render_template(
        'logs.html',
        logs=data
    )
@app.route('/testdb')
def testdb():
    cur = mysql.connection.cursor()
    cur.execute("SELECT DATABASE();")
    db = cur.fetchone()
    return f"Connected to: {db}"
if __name__ == '__main__':
    app.run(debug=True)