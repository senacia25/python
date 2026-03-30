import os
import psycopg2
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

# Habilita o CORS para permitir que o frontend acesse a API
CORS(app)

def get_db_connection():
    """Cria e retorna uma conexão com o banco de dados."""
    try:
        conn = psycopg2.connect(
            host=os.environ.get("DB_HOST", "localhost"),
            database=os.environ.get("DB_NAME", "mural_db"),
            user=os.environ.get("DB_USER", "user"),
            password=os.environ.get("DB_PASSWORD", "password")
        )
        return conn
    except psycopg2.OperationalError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

@app.route("/api/health")
def health_check():
    """Verifica a saúde da API e a conexão com o banco."""
    conn = get_db_connection()
    if conn:
        conn.close()
        return jsonify({"status": "ok", "database": "connected"})
    else:
        return jsonify({"status": "error", "database": "disconnected"}), 500

@app.route("/api/quotes", methods=["GET"])
def get_quotes():
    """Retorna todas as citações do banco de dados."""
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Falha na conexão com o banco de dados"}), 500
    
    quotes = []
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, author, text, created_at FROM quotes ORDER BY created_at DESC;")
            rows = cur.fetchall()
            for row in rows:
                quotes.append({
                    "id": row[0],
                    "author": row[1],
                    "text": row[2],
                    "created_at": row[3]
                })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()
        
    return jsonify(quotes)

@app.route("/api/quotes", methods=["POST"])
def add_quote():
    """Adiciona uma nova citação ao banco de dados."""
    data = request.get_json()
    if not data or "author" not in data or "text" not in data:
        return jsonify({"error": "Dados inválidos"}), 400

    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Falha na conexão com o banco de dados"}), 500

    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO quotes (author, text) VALUES (%s, %s) RETURNING id;",
                (data["author"], data["text"])
            )
            new_id = cur.fetchone()[0]
            conn.commit()
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

    return jsonify({"id": new_id, "author": data["author"], "text": data["text"]}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
