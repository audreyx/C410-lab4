from flask import Flask, request, redirect, url_for
app = Flask(__name__)
tasks = []

@app.route('/')
def hello():
    return '<h1>Welcome to Flask lab!</h1>'

@app.route('/task1', methods = ['GET', 'POST'])
def task():
    # POST
    if request.method == 'POST':
        category = request.form['category']
        priority = request.form['priority']# my
        description = request.form['description']# my
        tasks.append({'category':category})
        tasks.append({'priority':priority}) # my
        tasks.append({'description':description}) # my
        return redirect(url_for('task')) # task is function name
    
    # GET
    resp = '''
    <form action="" method=post>
    <p>Category: <input type=text name=category></p>
    <p><input type=submit value=Add></p>
    </form>
    '''
    
    resp = resp + '''
    <table border="1" cellpadding="3">    
        <tbody>
           <tr>
              <th>Category</th>
           </tr>
    '''
    
    for task in tasks:
        resp = resp + "<tr><td>%s</td></tr>" % (task['category'])
    resp = resp + '</tbody></table>'
    return resp

if __name__ == '__main__':
    app.debug = True
    app.run()


