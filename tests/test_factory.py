import os
import tempfile

import pytest

from app import create_app
from app.extensions import db


@pytest.mark.parametrize('app_config, is_testing', [
    ({}, False),
    ({'TESTING': True}, True),
])
def test_config(app_config, is_testing):
    db_fd, db_path = tempfile.mkstemp()

    inst = create_app({'SQLALCHEMY_DATABASE_URI': f'sqlite:///{db_path}', **app_config})
    assert inst.testing == is_testing

    with inst.app_context():
        db.engine.dispose()

    os.close(db_fd)
    os.unlink(db_path)
