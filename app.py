import logging
from flask import Flask
from container import Container
import routes.external_routes
import routes.internal_routes


def create_app():
    app = Flask(__name__)
    app.container = Container()
    # TODO: Register the Blueprints imported from the files above
    # ================================ YOUR CODE HERE ============================== #

    # TODO: Complete the wiring method below by providing the routes to wire to our app
    # ================================ YOUR CODE HERE ============================== #
    app.container.wire(modules=[])
    return app


app = create_app()


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)