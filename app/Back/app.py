from flask import Flask, request, jsonify

app = Flask(__name__)

# Credenciales
USER = "admin"
PASSWORD = "1234"

@app.route('/login', methods=['POST'])
def login():
    try:
        # Forzar la interpretación como JSON
        data = request.get_json(force=True)
        
        if not data:
            return jsonify({"error": "No data received"}), 400
            
        if data.get('username') == USER and data.get('password') == PASSWORD:
            return jsonify({"success": True, "message": "Login exitoso"})
        else:
            return jsonify({"success": False, "message": "Credenciales incorrectas"}), 401
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)