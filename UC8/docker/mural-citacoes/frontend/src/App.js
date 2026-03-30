import React, { useState, useEffect } from 'react';
import './App.css';

// A URL da API é configurada via variável de ambiente no build.
// Se não estiver definida, usa o endereço padrão do backend.
const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

function App() {
  const [quotes, setQuotes] = useState([]);
  const [author, setAuthor] = useState('');
  const [text, setText] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [submitting, setSubmitting] = useState(false);

  // Busca as citações do backend ao carregar a página
  useEffect(() => {
    fetchQuotes();
  }, []);

  const fetchQuotes = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await fetch(`${API_URL}/api/quotes`);
      if (!response.ok) {
        throw new Error(`Erro ao buscar citações: ${response.status}`);
      }
      const data = await response.json();
      setQuotes(data);
    } catch (err) {
      setError('Não foi possível conectar ao servidor. Verifique se o backend está rodando.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!author.trim() || !text.trim()) return;

    setSubmitting(true);
    try {
      const response = await fetch(`${API_URL}/api/quotes`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ author, text }),
      });
      if (!response.ok) {
        throw new Error('Erro ao salvar a citação.');
      }
      setAuthor('');
      setText('');
      fetchQuotes(); // Recarrega a lista
    } catch (err) {
      setError('Não foi possível salvar a citação.');
      console.error(err);
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="app">
      <header className="app-header">
        <h1>🐳 Mural de Citações</h1>
        <p className="subtitle">Atividade Prática — Docker</p>
      </header>

      <main className="app-main">
        <section className="form-section">
          <h2>Adicionar Nova Citação</h2>
          <form onSubmit={handleSubmit} className="quote-form">
            <div className="form-group">
              <label htmlFor="author">Autor</label>
              <input
                id="author"
                type="text"
                placeholder="Ex: Alan Turing"
                value={author}
                onChange={(e) => setAuthor(e.target.value)}
                required
              />
            </div>
            <div className="form-group">
              <label htmlFor="text">Citação</label>
              <textarea
                id="text"
                placeholder="Digite a citação aqui..."
                value={text}
                onChange={(e) => setText(e.target.value)}
                rows={3}
                required
              />
            </div>
            <button type="submit" disabled={submitting} className="btn-submit">
              {submitting ? 'Salvando...' : 'Adicionar ao Mural'}
            </button>
          </form>
        </section>

        <section className="quotes-section">
          <div className="quotes-header">
            <h2>Citações no Mural</h2>
            <button onClick={fetchQuotes} className="btn-refresh" title="Atualizar">
              ↻ Atualizar
            </button>
          </div>

          {error && (
            <div className="error-box">
              <strong>⚠️ Erro:</strong> {error}
            </div>
          )}

          {loading ? (
            <div className="loading">Carregando citações...</div>
          ) : quotes.length === 0 ? (
            <div className="empty-state">
              <p>Nenhuma citação encontrada.</p>
              <p>Seja o primeiro a adicionar uma!</p>
            </div>
          ) : (
            <div className="quotes-grid">
              {quotes.map((quote) => (
                <div key={quote.id} className="quote-card">
                  <blockquote className="quote-text">"{quote.text}"</blockquote>
                  <cite className="quote-author">— {quote.author}</cite>
                </div>
              ))}
            </div>
          )}
        </section>
      </main>

      <footer className="app-footer">
        <p>
          Backend rodando em: <code>{API_URL}</code>
        </p>
      </footer>
    </div>
  );
}

export default App;
