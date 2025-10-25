from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        operation = data.get('operation')
        value1 = float(data.get('value1', 0))
        value2 = data.get('value2')
        
        result = None
        
        # Operações básicas
        if operation == 'add':
            result = value1 + float(value2)
        elif operation == 'subtract':
            result = value1 - float(value2)
        elif operation == 'multiply':
            result = value1 * float(value2)
        elif operation == 'divide':
            if float(value2) == 0:
                return jsonify({'error': 'Divisão por zero'}), 400
            result = value1 / float(value2)
        elif operation == 'percentage':
            # Calcula X% de Y (exemplo: 10% de 298 = 29.8)
            result = (value1 * float(value2)) / 100
        
        # Operações científicas
        elif operation == 'sqrt':
            if value1 < 0:
                return jsonify({'error': 'Raiz de número negativo'}), 400
            result = math.sqrt(value1)
        elif operation == 'sin':
            result = math.sin(math.radians(value1))
        elif operation == 'cos':
            result = math.cos(math.radians(value1))
        elif operation == 'tan':
            result = math.tan(math.radians(value1))
        else:
            return jsonify({'error': 'Operação inválida'}), 400
        
        # Arredondar para evitar erros de ponto flutuante
        result = round(result, 10)
        
        return jsonify({'result': result})
    
    except ValueError:
        return jsonify({'error': 'Valor inválido'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
