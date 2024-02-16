from flask.views import MethodView
from flask_smorest import Blueprint

from app.extensions import db
from app.models import Answer
from app.schemas import AnswerSchema

answer_bp = Blueprint('answer', 'answer', url_prefix='/api/v1/answer')


@answer_bp.route('')
class AnswerAPI(MethodView):
    @answer_bp.response(200, AnswerSchema)
    def get(self):
        return db.session.execute(
            db.select(Answer).order_by(db.func.random()).limit(1)
        ).scalar_one()
