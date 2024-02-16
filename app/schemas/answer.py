import marshmallow as ma


class AnswerSchema(ma.Schema):
    answer = ma.fields.Str()
