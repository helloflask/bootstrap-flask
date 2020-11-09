from flask import current_app, flash, render_template_string, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import BooleanField, FileField, HiddenField, MultipleFileField,\
    PasswordField, RadioField, StringField, SubmitField
from wtforms.validators import DataRequired


class TestRender():
    def test_render_field(self, app, client, hello_form):
        @app.route('/field')
        def test():
            form = hello_form()
            return render_template_string('''
            {% from 'bootstrap/form.html' import render_field %}
            {{ render_field(form.username) }}
            {{ render_field(form.password) }}
            ''', form=form)

        response = client.get('/field')
        data = response.get_data(as_text=True)
        assert '<input class="form-control" id="username" name="username"' in data
        assert '<input class="form-control" id="password" name="password"' in data

    def test_render_form(self, app, client, hello_form):
        @app.route('/form')
        def test():
            form = hello_form()
            return render_template_string('''
                    {% from 'bootstrap/form.html' import render_form %}
                    {{ render_form(form) }}
                    ''', form=form)

        response = client.get('/form')
        data = response.get_data(as_text=True)
        assert '<input class="form-control" id="username" name="username"' in data
        assert '<input class="form-control" id="password" name="password"' in data

    def test_render_form_row(self, app, client, hello_form):
        @app.route('/form')
        def test():
            form = hello_form()
            return render_template_string('''
                    {% from 'bootstrap/form.html' import render_form_row %}
                    {{ render_form_row([form.username, form.password]) }}
                    ''', form=form)
        response = client.get('/form')
        data = response.get_data(as_text=True)
        assert '<div class="form-row">' in data
        assert '<div class="col">' in data

    def test_render_form_row_row_class(self, app, client, hello_form):
        @app.route('/form')
        def test():
            form = hello_form()
            return render_template_string('''
                    {% from 'bootstrap/form.html' import render_form_row %}
                    {{ render_form_row([form.username, form.password], row_class='row') }}
                    ''', form=form)
        response = client.get('/form')
        data = response.get_data(as_text=True)
        assert '<div class="row">' in data

    def test_render_form_row_col_class_default(self, app, client, hello_form):
        @app.route('/form')
        def test():
            form = hello_form()
            return render_template_string('''
                    {% from 'bootstrap/form.html' import render_form_row %}
                    {{ render_form_row([form.username, form.password], col_class_default='col-md-6') }}
                    ''', form=form)
        response = client.get('/form')
        data = response.get_data(as_text=True)
        assert '<div class="col-md-6">' in data

    def test_render_form_row_col_map(self, app, client, hello_form):
        @app.route('/form')
        def test():
            form = hello_form()
            return render_template_string('''
                    {% from 'bootstrap/form.html' import render_form_row %}
                    {{ render_form_row([form.username, form.password], col_map={'username': 'col-md-6'}) }}
                    ''', form=form)
        response = client.get('/form')
        data = response.get_data(as_text=True)
        assert '<div class="col">' in data
        assert '<div class="col-md-6">' in data

    def test_render_pager(self, app, client):
        db = SQLAlchemy(app)

        class Message(db.Model):
            id = db.Column(db.Integer, primary_key=True)

        @app.route('/pager')
        def test():
            db.drop_all()
            db.create_all()
            for i in range(100):
                m = Message()
                db.session.add(m)
            db.session.commit()
            page = request.args.get('page', 1, type=int)
            pagination = Message.query.paginate(page, per_page=10)
            messages = pagination.items
            return render_template_string('''
                            {% from 'bootstrap/pagination.html' import render_pager %}
                            {{ render_pager(pagination) }}
                            ''', pagination=pagination, messages=messages)

        response = client.get('/pager')
        data = response.get_data(as_text=True)
        assert '<nav aria-label="Page navigation">' in data
        assert 'Previous' in data
        assert 'Next' in data
        assert '<li class="page-item disabled">' in data

        response = client.get('/pager?page=2')
        data = response.get_data(as_text=True)
        assert '<nav aria-label="Page navigation">' in data
        assert 'Previous' in data
        assert 'Next' in data
        assert '<li class="page-item disabled">' not in data

    def test_render_pagination(self, app, client):
        db = SQLAlchemy(app)

        class Message(db.Model):
            id = db.Column(db.Integer, primary_key=True)

        @app.route('/pagination')
        def test():
            db.drop_all()
            db.create_all()
            for i in range(100):
                m = Message()
                db.session.add(m)
            db.session.commit()
            page = request.args.get('page', 1, type=int)
            pagination = Message.query.paginate(page, per_page=10)
            messages = pagination.items
            return render_template_string('''
                                    {% from 'bootstrap/pagination.html' import render_pagination %}
                                    {{ render_pagination(pagination) }}
                                    ''', pagination=pagination, messages=messages)

        response = client.get('/pagination')
        data = response.get_data(as_text=True)
        assert '<nav aria-label="Page navigation">' in data
        assert '<a class="page-link" href="#">1 <span class="sr-only">(current)</span></a>' in data
        assert '10</a>' in data

        response = client.get('/pagination?page=2')
        data = response.get_data(as_text=True)
        assert '<nav aria-label="Page navigation">' in data
        assert '1</a>' in data
        assert '<a class="page-link" href="#">2 <span class="sr-only">(current)</span></a>' in data
        assert '10</a>' in data

    def test_render_nav_item(self, app, client):
        @app.route('/nav_item')
        def test():
            return render_template_string('''
                    {% from 'bootstrap/nav.html' import render_nav_item %}
                    {{ render_nav_item('test', 'Home') }}
                    ''')

        response = client.get('/nav_item')
        data = response.get_data(as_text=True)
        assert '<a class="nav-item nav-link active"' in data

    def test_render_breadcrumb_item(self, app, client):
        @app.route('/breadcrumb_item')
        def test():
            return render_template_string('''
                    {% from 'bootstrap/nav.html' import render_breadcrumb_item %}
                    {{ render_breadcrumb_item('test', 'Home') }}
                    ''')

        response = client.get('/breadcrumb_item')
        data = response.get_data(as_text=True)
        assert '<li class="breadcrumb-item active"  aria-current="page">' in data

    def test_render_static(self, app, client):
        @app.route('/test_static')
        def test():
            return render_template_string('''
                            {% from 'bootstrap/utils.html' import render_static %}
                            {{ render_static('css', 'test.css') }}
                            {{ render_static('js', 'test.js') }}
                            {{ render_static('icon', 'test.ico') }}
                            ''')

        response = client.get('/test_static')
        data = response.get_data(as_text=True)
        assert '<link rel="stylesheet" href="/static/test.css" type="text/css">' in data
        assert '<script type="text/javascript" src="/static/test.js"></script>' in data
        assert '<link rel="icon" href="/static/test.ico">' in data

    def test_render_messages(self, app, client):
        @app.route('/messages')
        def test_messages():
            flash('test message', 'danger')
            return render_template_string('''
                            {% from 'bootstrap/utils.html' import render_messages %}
                            {{ render_messages() }}
                            ''')

        @app.route('/container')
        def test_container():
            flash('test message', 'danger')
            return render_template_string('''
                            {% from 'bootstrap/utils.html' import render_messages %}
                            {{ render_messages(container=True) }}
                            ''')

        @app.route('/dismissible')
        def test_dismissible():
            flash('test message', 'danger')
            return render_template_string('''
                            {% from 'bootstrap/utils.html' import render_messages %}
                            {{ render_messages(dismissible=True) }}
                            ''')

        @app.route('/dismiss_animate')
        def test_dismiss_animate():
            flash('test message', 'danger')
            return render_template_string('''
                            {% from 'bootstrap/utils.html' import render_messages %}
                            {{ render_messages(dismissible=True, dismiss_animate=True) }}
                            ''')

        response = client.get('/messages')
        data = response.get_data(as_text=True)
        assert '<div class="alert alert-danger"' in data

        response = client.get('/container')
        data = response.get_data(as_text=True)
        assert '<div class="container flashed-messages">' in data

        response = client.get('/dismissible')
        data = response.get_data(as_text=True)
        assert 'alert-dismissible' in data
        assert '<button type="button" class="close" data-dismiss="alert"' in data
        assert 'fade show' not in data

        response = client.get('/dismiss_animate')
        data = response.get_data(as_text=True)
        assert 'alert-dismissible', data
        assert '<button type="button" class="close" data-dismiss="alert"' in data
        assert 'fade show' in data

    # test WTForm fields for render_form and render_field
    def test_render_form_enctype(self, app, client):
        class SingleUploadForm(FlaskForm):
            avatar = FileField('Avatar')

        class MultiUploadForm(FlaskForm):
            photos = MultipleFileField('Multiple photos')

        @app.route('/single')
        def single():
            form = SingleUploadForm()
            return render_template_string('''
            {% from 'bootstrap/form.html' import render_form %}
            {{ render_form(form) }}
            ''', form=form)

        @app.route('/multi')
        def multi():
            form = SingleUploadForm()
            return render_template_string('''
            {% from 'bootstrap/form.html' import render_form %}
            {{ render_form(form) }}
            ''', form=form)

        response = client.get('/single')
        data = response.get_data(as_text=True)
        assert 'multipart/form-data' in data

        response = client.get('/multi')
        data = response.get_data(as_text=True)
        assert 'multipart/form-data' in data

    # test render_kw class for WTForms field
    def test_form_render_kw_class(self, app, client):

        class TestForm(FlaskForm):
            username = StringField('Username')
            password = PasswordField('Password', render_kw={'class': 'my-password-class'})
            submit = SubmitField(render_kw={'class': 'my-awesome-class'})

        @app.route('/render_kw')
        def render_kw():
            form = TestForm()
            return render_template_string('''
            {% from 'bootstrap/form.html' import render_form %}
            {{ render_form(form) }}
            ''', form=form)

        response = client.get('/render_kw')
        data = response.get_data(as_text=True)
        assert 'class="form-control"' in data
        assert 'class="form-control "' not in data
        assert 'class="form-control my-password-class"' in data
        assert 'my-awesome-class' in data
        assert 'btn' in data

    # test WTForm field description for BooleanField
    def test_form_description_for_booleanfield(self, app, client):

        class TestForm(FlaskForm):
            remember = BooleanField('Remember me', description='Just check this')

        @app.route('/description')
        def description():
            form = TestForm()
            return render_template_string('''
            {% from 'bootstrap/form.html' import render_form %}
            {{ render_form(form) }}
            ''', form=form)

        response = client.get('/description')
        data = response.get_data(as_text=True)
        assert 'Remember me' in data
        assert '<small class="form-text text-muted">Just check this</small>' in data

    def test_button_size(self, app, client, hello_form):
        assert current_app.config['BOOTSTRAP_BTN_SIZE'] == 'md'
        current_app.config['BOOTSTRAP_BTN_SIZE'] = 'lg'

        @app.route('/form')
        def test():
            form = hello_form()
            return render_template_string('''
            {% from 'bootstrap/form.html' import render_form %}
            {{ render_form(form) }}
            ''', form=form)

        response = client.get('/form')
        data = response.get_data(as_text=True)
        assert 'btn-lg' in data

        @app.route('/form2')
        def test_overwrite():
            form = hello_form()
            return render_template_string('''
            {% from 'bootstrap/form.html' import render_form %}
            {{ render_form(form, button_size='sm') }}
            ''', form=form)

        response = client.get('/form2')
        data = response.get_data(as_text=True)
        assert 'btn-lg' not in data
        assert 'btn-sm' in data

    def test_button_style(self, app, client, hello_form):
        assert current_app.config['BOOTSTRAP_BTN_STYLE'] == 'primary'
        current_app.config['BOOTSTRAP_BTN_STYLE'] = 'secondary'

        @app.route('/form')
        def test():
            form = hello_form()
            return render_template_string('''
            {% from 'bootstrap/form.html' import render_form %}
            {{ render_form(form) }}
            ''', form=form)

        response = client.get('/form')
        data = response.get_data(as_text=True)
        assert 'btn-secondary' in data

        @app.route('/form2')
        def test_overwrite():
            form = hello_form()
            return render_template_string('''
            {% from 'bootstrap/form.html' import render_form %}
            {{ render_form(form, button_style='success') }}
            ''', form=form)

        response = client.get('/form2')
        data = response.get_data(as_text=True)
        assert 'btn-primary' not in data
        assert 'btn-success' in data

        @app.route('/form3')
        def test_button_map():
            form = hello_form()
            return render_template_string('''
            {% from 'bootstrap/form.html' import render_form %}
            {{ render_form(form, button_map={'submit': 'warning'}) }}
            ''', form=form)

        response = client.get('/form3')
        data = response.get_data(as_text=True)
        assert 'btn-primary' not in data
        assert 'btn-warning' in data

    def test_error_message_for_radiofield_and_booleanfield(self, app, client):
        class TestForm(FlaskForm):
            remember = BooleanField('Remember me', validators=[DataRequired()])
            option = RadioField(choices=[('dog', 'Dog'), ('cat', 'Cat'),
                                         ('bird', 'Bird'), ('alien', 'Alien')],
                                validators=[DataRequired()])

        @app.route('/error', methods=['GET', 'POST'])
        def error():
            form = TestForm()
            if form.validate_on_submit():
                pass
            return render_template_string('''
            {% from 'bootstrap/form.html' import render_form %}
            {{ render_form(form) }}
            ''', form=form)

        response = client.post('/error', follow_redirects=True)
        data = response.get_data(as_text=True)
        assert 'This field is required' in data

    def test_render_simple_table(self, app, client):
        db = SQLAlchemy(app)

        class Message(db.Model):
            id = db.Column(db.Integer, primary_key=True)
            text = db.Column(db.Text)

        @app.route('/table')
        def test():
            db.drop_all()
            db.create_all()
            for i in range(10):
                m = Message(text='Test message {}'.format(i+1))
                db.session.add(m)
            db.session.commit()
            page = request.args.get('page', 1, type=int)
            pagination = Message.query.paginate(page, per_page=10)
            messages = pagination.items
            titles = [('id', '#'), ('text', 'Message')]
            return render_template_string('''
                                    {% from 'bootstrap/table.html' import render_table %}
                                    {{ render_table(messages, titles) }}
                                    ''', titles=titles, messages=messages)

        response = client.get('/table')
        data = response.get_data(as_text=True)
        assert '<table class="table">' in data
        assert '<th scope="col">#</th>' in data
        assert '<th scope="col">Message</th>' in data
        assert '<th scope="col">Message</th>' in data
        assert '<th scope="row">1</th>' in data
        assert '<td>Test message 1</td>' in data

    def test_render_customized_table(self, app, client):
        db = SQLAlchemy(app)

        class Message(db.Model):
            id = db.Column(db.Integer, primary_key=True)
            text = db.Column(db.Text)

        @app.route('/table')
        def test():
            db.drop_all()
            db.create_all()
            for i in range(10):
                m = Message(text='Test message {}'.format(i+1))
                db.session.add(m)
            db.session.commit()
            page = request.args.get('page', 1, type=int)
            pagination = Message.query.paginate(page, per_page=10)
            messages = pagination.items
            titles = [('id', '#'), ('text', 'Message')]
            return render_template_string('''
                                    {% from 'bootstrap/table.html' import render_table %}
                                    {{ render_table(messages, titles, table_classes='table-striped',
                                    header_classes='thead-dark', caption='Messages') }}
                                    ''', titles=titles, messages=messages)

        response = client.get('/table')
        data = response.get_data(as_text=True)
        assert '<table class="table table-striped">' in data
        assert '<thead class="thead-dark">' in data
        assert '<caption>Messages</caption>' in data

    def test_render_responsive_table(self, app, client):
        db = SQLAlchemy(app)

        class Message(db.Model):
            id = db.Column(db.Integer, primary_key=True)
            text = db.Column(db.Text)

        @app.route('/table')
        def test():
            db.drop_all()
            db.create_all()
            for i in range(10):
                m = Message(text='Test message {}'.format(i+1))
                db.session.add(m)
            db.session.commit()
            page = request.args.get('page', 1, type=int)
            pagination = Message.query.paginate(page, per_page=10)
            messages = pagination.items
            titles = [('id', '#'), ('text', 'Message')]
            return render_template_string('''
                                    {% from 'bootstrap/table.html' import render_table %}
                                    {{ render_table(messages, titles, responsive=True,
                                    responsive_class='table-responsive-sm') }}
                                    ''', titles=titles, messages=messages)

        response = client.get('/table')
        data = response.get_data(as_text=True)
        assert '<div class="table-responsive-sm">' in data

    def test_build_table_titles(self, app, client):
        db = SQLAlchemy(app)

        class Message(db.Model):
            id = db.Column(db.Integer, primary_key=True)
            text = db.Column(db.Text)

        @app.route('/table')
        def test():
            db.drop_all()
            db.create_all()
            for i in range(10):
                m = Message(text='Test message {}'.format(i+1))
                db.session.add(m)
            db.session.commit()
            page = request.args.get('page', 1, type=int)
            pagination = Message.query.paginate(page, per_page=10)
            messages = pagination.items
            return render_template_string('''
                                    {% from 'bootstrap/table.html' import render_table %}
                                    {{ render_table(messages) }}
                                    ''', messages=messages)

        response = client.get('/table')
        data = response.get_data(as_text=True)
        assert '<table class="table">' in data
        assert '<th scope="col">#</th>' in data
        assert '<th scope="col">Text</th>' in data
        assert '<th scope="col">Text</th>' in data
        assert '<th scope="row">1</th>' in data
        assert '<td>Test message 1</td>' in data

    def test_build_table_titles_with_empty_data(self, app, client):

        @app.route('/table')
        def test():
            messages = []
            return render_template_string('''
                                    {% from 'bootstrap/table.html' import render_table %}
                                    {{ render_table(messages) }}
                                    ''', messages=messages)

        response = client.get('/table')
        assert response.status_code == 200

    def test_render_table_with_actions(self, app, client):
        db = SQLAlchemy(app)

        class Message(db.Model):
            id = db.Column(db.Integer, primary_key=True)
            text = db.Column(db.Text)

        @app.route('/table/<message_id>/view')
        def test_view_message(message_id):
            return 'Viewing {}'.format(message_id)

        @app.route('/table')
        def test():
            db.drop_all()
            db.create_all()
            for i in range(10):
                m = Message(text='Test message {}'.format(i+1))
                db.session.add(m)
            db.session.commit()
            page = request.args.get('page', 1, type=int)
            pagination = Message.query.paginate(page, per_page=10)
            messages = pagination.items
            titles = [('id', '#'), ('text', 'Message')]
            return render_template_string('''
                                    {% from 'bootstrap/table.html' import render_table %}
                                    {{ render_table(messages, titles, show_actions=True,
                                    view_url=url_for('test_view_message', message_id=':primary_key')) }}
                                    ''', titles=titles, messages=messages)

        response = client.get('/table')
        data = response.get_data(as_text=True)
        assert '<a href="/table/1/view">' in data
        assert '<img src="/bootstrap/static/img/view.svg" alt="View">' in data

    def test_render_hidden_errors(self, app, client):
        class TestForm(FlaskForm):
            hide = HiddenField('Hide', validators=[DataRequired('Hide field is empty.')])
            submit = SubmitField()

        @app.route('/error', methods=['GET', 'POST'])
        def error():
            form = TestForm()
            if form.validate_on_submit():
                pass
            return render_template_string('''
            {% from 'bootstrap/form.html' import render_field, render_hidden_errors %}
            <form method="post">
                {{ form.hidden_tag() }}
                {{ render_hidden_errors(form) }}
                {{ render_field(form.submit) }}
            </form>
            ''', form=form)

        response = client.post('/error', follow_redirects=True)
        data = response.get_data(as_text=True)
        assert 'Hide field is empty.' in data

    def test_render_icon(self, app, client):
        @app.route('/icon')
        def icon():
            return render_template_string('''
            {% from 'bootstrap/utils.html' import render_icon %}
                {{ render_icon('heart') }}
            ''')

        @app.route('/icon-size')
        def icon_size():
            return render_template_string('''
            {% from 'bootstrap/utils.html' import render_icon %}
                {{ render_icon('heart', 32) }}
            ''')

        @app.route('/icon-style')
        def icon_style():
            return render_template_string('''
            {% from 'bootstrap/utils.html' import render_icon %}
                {{ render_icon('heart', color='primary') }}
            ''')

        @app.route('/icon-color')
        def icon_color():
            return render_template_string('''
            {% from 'bootstrap/utils.html' import render_icon %}
                {{ render_icon('heart', color='green') }}
            ''')

        response = client.get('/icon')
        data = response.get_data(as_text=True)
        assert 'bootstrap-icons.svg#heart' in data
        assert 'width="1em"' in data
        assert 'height="1em"' in data

        response = client.get('/icon-size')
        data = response.get_data(as_text=True)
        assert 'bootstrap-icons.svg#heart' in data
        assert 'width="32"' in data
        assert 'height="32"' in data

        response = client.get('/icon-style')
        data = response.get_data(as_text=True)
        assert 'bootstrap-icons.svg#heart' in data
        assert 'text-primary' in data

        response = client.get('/icon-color')
        data = response.get_data(as_text=True)
        assert 'bootstrap-icons.svg#heart' in data
        assert 'style="color: green"' in data

    def test_render_icon_config(self, app, client):
        app.config['BOOTSTRAP_ICON_SIZE'] = 100
        app.config['BOOTSTRAP_ICON_COLOR'] = 'success'

        @app.route('/icon')
        def icon():
            return render_template_string('''
            {% from 'bootstrap/utils.html' import render_icon %}
                {{ render_icon('heart') }}
            ''')

        response = client.get('/icon')
        data = response.get_data(as_text=True)
        assert 'width="100"' in data
        assert 'height="100"' in data
        assert 'text-success' in data
