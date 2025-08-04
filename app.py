from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h2>Welcome to Path Traversal Lab 🔓</h2>
        <p>Try visiting: <code>/view?filename=passwd.txt</code></p>
    '''

@app.route('/view')
def view_file():
    filename = request.args.get('filename', '')
    try:
        base_path = os.path.abspath(".")  # All files inside 'files' folder
        file_path = os.path.abspath(os.path.join(base_path, filename))

        if not file_path.startswith(base_path):
            return "Hacking attempt blocked ❌"

        return send_from_directory(base_path, filename)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
