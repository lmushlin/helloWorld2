from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Lily Mushlin! I am adding my first code change.'

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about-css')
def about_css():
    return render_template('about-css.html')

@app.route('/favorite-course', methods=['GET'])
def favorite_course():
    favorite_subject = request.args.get('favorite_subject', '')
    course_number = request.args.get('course_number', '')
    return render_template(
        'favorite-course.html',
        favorite_subject=favorite_subject,
        course_number=course_number
    )


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        first_name = request.form.get('first_name', '')
        last_name = request.form.get('last_name', '')
        email = request.form.get('email', '')
        comments = request.form.get('comments', '')

        # Render contact.html with form_submitted=True to display thank you message
        return render_template(
            'contact.html',
            form_submitted=True,
            first_name=first_name,
            last_name=last_name,
            email=email,
            comments=comments
        )

    # Render contact.html with form_submitted=False on GET request
    return render_template('contact.html', form_submitted=False)


if __name__ == '__main__':
    app.run()