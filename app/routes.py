from flask import Blueprint, jsonify, request
from .models import db, User, Expense, Income, Investment
from .schemas import user_schema, expenses_schema, incomes_schema, investments_schema
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

api_bp = Blueprint('api', __name__)

@api_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"message": "User already exists"}), 400
    new_user = User(username=data['username'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

@api_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    return jsonify({"message": "Invalid credentials"}), 401

@api_bp.route('/expenses', methods=['GET', 'POST'])
@jwt_required()
def handle_expenses():
    user_id = get_jwt_identity()
    if request.method == 'POST':
        data = request.get_json()
        new_expense = Expense(amount=data['amount'], category=data['category'], user_id=user_id)
        db.session.add(new_expense)
        db.session.commit()
        return jsonify({"message": "Expense added successfully"}), 201

    expenses = Expense.query.filter_by(user_id=user_id).all()
    return expenses_schema.jsonify(expenses), 200

@api_bp.route('/incomes', methods=['GET', 'POST'])
@jwt_required()
def handle_incomes():
    user_id = get_jwt_identity()
    if request.method == 'POST':
        data = request.get_json()
        new_income = Income(amount=data['amount'], source=data['source'], user_id=user_id)
        db.session.add(new_income)
        db.session.commit()
        return jsonify({"message": "Income added successfully"}), 201

    incomes = Income.query.filter_by(user_id=user_id).all()
    return incomes_schema.jsonify(incomes), 200

@api_bp.route('/investments', methods=['GET', 'POST'])
@jwt_required()
def handle_investments():
    user_id = get_jwt_identity()
    if request.method == 'POST':
        data = request.get_json()
        new_investment = Investment(amount=data['amount'], type=data['type'], performance=data['performance'], user_id=user_id)
        db.session.add(new_investment)
        db.session.commit()
        return jsonify({"message": "Investment added successfully"}), 201

    investments = Investment.query.filter_by(user_id=user_id).all()
    return investments_schema.jsonify(investments), 200

@api_bp.route('/dashboard', methods=['GET'])
@jwt_required()
def dashboard():
    user_id = get_jwt_identity()
    expenses = Expense.query.filter_by(user_id=user_id).all()
    incomes = Income.query.filter_by(user_id=user_id).all()
    investments = Investment.query.filter_by(user_id=user_id).all()

    total_expenses = sum(expense.amount for expense in expenses)
    total_incomes = sum(income.amount for income in incomes)
    total_investments = sum(investment.amount for investment in investments)

    return jsonify({
        "total_expenses": total_expenses,
        "total_incomes": total_incomes,
        "total_investments": total_investments,
        "net_worth": total_incomes - total_expenses + total_investments
    }), 200
