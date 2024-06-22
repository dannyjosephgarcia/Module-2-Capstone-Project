import logging
from flask import Flask
from container import Container
from routes import external_routes
from routes import internal_routes
from routes.external_routes import external_routes_blueprint
from routes.internal_routes import internal_routes_blueprint


def create_app():
    app = Flask(__name__)
    app.container = Container()
    # TODO: Register the Blueprints imported from the files above
    # ================================ YOUR CODE HERE ============================== #

    app.register_blueprint(external_routes_blueprint)
    app.register_blueprint(internal_routes_blueprint)

    # TODO: Complete the wiring method below by providing the routes to wire to our app
    # ================================ YOUR CODE HERE ============================== #

    app.container.wire(modules=[external_routes.__name__,
                                internal_routes.__name__])
    return app


app = create_app()


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
