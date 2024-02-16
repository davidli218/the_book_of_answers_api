from flask import Flask

__version__ = '0.1.0'


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///app.sqlite',
        API_TITLE='The book of answers',
        API_VERSION='v1',
        OPENAPI_VERSION='3.0.2',
        OPENAPI_URL_PREFIX='/api/v1/docs',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # Initialize extensions
    from app import extensions as ext
    ext.db.init_app(app)
    ext.api.init_app(app)
    ext.jwt.init_app(app)

    with app.app_context():
        from app import models, data_helper
        ext.db.create_all()

        if ext.db.session.execute(ext.db.select(models.Answer).limit(1)).scalar_one_or_none() is None:
            data_helper.init_database()

    # Register blueprints
    from app import routes
    app.register_blueprint(routes.answer_bp)

    return app
