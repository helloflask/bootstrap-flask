from flask import render_template_string


def test_render_sortlink(app, client):
    @app.route("/sortlink")
    def sortlink():
        return render_template_string(
            """
        {% from 'bootstrap4/utils.html' import render_sortlink %}
            {{ render_sortlink('foo') }}
        """
        )

    response = client.get("/sortlink")
    data = response.get_data(as_text=True)
    assert "?sort=foo,asc" in data

    response = client.get("/sortlink?sort=foo,asc")
    data = response.get_data(as_text=True)
    assert "?sort=foo,desc" in data

    response = client.get("/sortlink?sort=foo,desc")
    data = response.get_data(as_text=True)
    assert "?sort=foo,asc" in data
