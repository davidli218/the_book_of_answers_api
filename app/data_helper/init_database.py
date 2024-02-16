from pathlib import Path

from app.extensions import db
from app.models import Answer

txt_file = Path(__file__).parent / 'src' / 'answers.txt'


def init_database():
    with open(txt_file, 'r', encoding='utf-8') as f:
        for ans in set(line.strip() for line in f):
            db.session.add(Answer(answer=ans))

    db.session.commit()
