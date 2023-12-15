from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/add')
def add():
    try:
        a = int(request.args['a'])
        b = int(request.args['b'])
        return str(operations.add(a,b))
    except ValueError as e: 
        return 'Invalid value for query parameter'
    
@app.route('/sub')
def sub():
    try:
        a = int(request.args['a'])
        b = int(request.args['b'])
        return str(operations.sub(a,b))
    except ValueError as e: 
        return 'Invalid value for query parameter'
    
@app.route('/mult')
def mult():
    try:
        a = int(request.args['a'])
        b = int(request.args['b'])
        return str(operations.mult(a,b))
    except ValueError as e: 
        return 'Invalid value for query parameter'
    
@app.route('/div')
def div():
    try:
        a = int(request.args['a'])
        b = int(request.args['b'])
        return str(int(operations.div(a,b)))
    except ValueError as e: 
        return 'Invalid value for query parameter'
    except ZeroDivisionError as e:
        return 'Invalid value for (b) parameter: cannot be zero'
    
@app.route('/math/<op>')
def all_ops(op):
    try:
        a = int(request.args['a'])
        b = int(request.args['b'])
        ops = {
            'add': operations.add,
            'sub': operations.sub,
            'mult': operations.mult,
            'div': operations.div,
        }
        return str(int(ops.get(op)(a,b)))
    except TypeError as e:
        return 'Invalid value for math operation'
    except ValueError as e: 
        return 'Invalid value for query parameter'
    except ZeroDivisionError as e:
        return 'Invalid value for (b) parameter: cannot be zero'
    