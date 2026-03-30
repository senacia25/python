-- Cria a tabela de citações se ela não existir
CREATE TABLE IF NOT EXISTS quotes (
    id SERIAL PRIMARY KEY,
    author VARCHAR(100) NOT NULL,
    text TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Insere algumas citações de exemplo para que o mural não comece vazio
INSERT INTO quotes (author, text) VALUES
('Edsger W. Dijkstra', 'Simplicidade é um pré-requisito para a confiabilidade.'),
('Linus Torvalds', 'Falar é fácil. Mostre-me o código.'),
('Grace Hopper', 'É mais fácil pedir perdão do que permissão.'),
('Martin Fowler', 'Qualquer tolo consegue escrever um código que um computador entende. Bons programadores escrevem código que humanos conseguem entender.');
