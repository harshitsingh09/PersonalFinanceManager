from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)

class ExpenseSchema(Schema):
    id = fields.Int(dump_only=True)
    amount = fields.Float(required=True)
    category = fields.Str(required=True)
    date = fields.DateTime(dump_only=True)
    user_id = fields.Int(dump_only=True)

class IncomeSchema(Schema):
    id = fields.Int(dump_only=True)
    amount = fields.Float(required=True)
    source = fields.Str(required=True)
    date = fields.DateTime(dump_only=True)
    user_id = fields.Int(dump_only=True)

class InvestmentSchema(Schema):
    id = fields.Int(dump_only=True)
    amount = fields.Float(required=True)
    type = fields.Str(required=True)
    date = fields.DateTime(dump_only=True)
    performance = fields.Float(required=True)
    user_id = fields.Int(dump_only=True)

user_schema = UserSchema()
expenses_schema = ExpenseSchema(many=True)
incomes_schema = IncomeSchema(many=True)
investments_schema = InvestmentSchema(many=True)
