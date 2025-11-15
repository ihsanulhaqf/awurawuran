from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/projects')
def projects():
    projects_list = [
        {
            'title': 'Project 1',
            'description': 'Deskripsi project pertama',
            'tech': ['Python', 'Flask', 'HTML/CSS'],
            'link': '#'
        },
        {
            'title': 'Project 2',
            'description': 'Deskripsi project kedua',
            'tech': ['JavaScript', 'React', 'Node.js'],
            'link': '#'
        },
        {
            'title': 'Project 3',
            'description': 'Deskripsi project ketiga',
            'tech': ['Django', 'PostgreSQL', 'Docker'],
            'link': '#'
        }
    ]
    return render_template('projects.html', projects=projects_list)


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
