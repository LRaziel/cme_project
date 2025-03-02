BEGIN;

-- Criar a tabela de usuários se não existir
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role VARCHAR(50) CHECK (role IN ('tecnico', 'enfermagem', 'administrativo')) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Criar a tabela de materiais se não existir
CREATE TABLE IF NOT EXISTS materials (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(100) NOT NULL,
    expiration_date DATE NOT NULL,
    serial VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Criar a tabela de rastreamento dos materiais se não existir
CREATE TABLE IF NOT EXISTS tracking (
    id SERIAL PRIMARY KEY,
    material_id INT REFERENCES materials(id) ON DELETE CASCADE,
    stage VARCHAR(50) CHECK (stage IN ('recebimento', 'lavagem', 'esterilizacao', 'distribuicao')) NOT NULL,
    status VARCHAR(50) CHECK (status IN ('pendente', 'concluido', 'falha')) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Criar a tabela de falhas no processo se não existir
CREATE TABLE IF NOT EXISTS failures (
    id SERIAL PRIMARY KEY,
    tracking_id INT REFERENCES tracking(id) ON DELETE CASCADE,
    reason TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Inserir usuários de teste apenas se a tabela estiver vazia
INSERT INTO users (name, email, password, role)
SELECT 'Admin User', 'admin@email.com', 'admin123', 'administrativo'
WHERE NOT EXISTS (SELECT 1 FROM users);

INSERT INTO users (name, email, password, role)
SELECT 'Técnico João', 'joao@email.com', 'senha123', 'tecnico'
WHERE NOT EXISTS (SELECT 1 FROM users WHERE email = 'joao@email.com');

INSERT INTO users (name, email, password, role)
SELECT 'Enfermeira Ana', 'ana@email.com', 'enf456', 'enfermagem'
WHERE NOT EXISTS (SELECT 1 FROM users WHERE email = 'ana@email.com');

-- Inserir materiais apenas se não existirem
INSERT INTO materials (name, type, expiration_date, serial)
SELECT 'Pinça Cirúrgica', 'Instrumento Cirúrgico', '2025-12-31', 'PINCA123'
WHERE NOT EXISTS (SELECT 1 FROM materials WHERE serial = 'PINCA123');

INSERT INTO materials (name, type, expiration_date, serial)
SELECT 'Bisturi', 'Instrumento Cirúrgico', '2025-06-30', 'BISTURI456'
WHERE NOT EXISTS (SELECT 1 FROM materials WHERE serial = 'BISTURI456');

-- Inserir rastreamento inicial apenas se não existirem registros para o material
INSERT INTO tracking (material_id, stage, status)
SELECT 1, 'recebimento', 'concluido'
WHERE NOT EXISTS (SELECT 1 FROM tracking WHERE material_id = 1 AND stage = 'recebimento');

INSERT INTO tracking (material_id, stage, status)
SELECT 1, 'lavagem', 'pendente'
WHERE NOT EXISTS (SELECT 1 FROM tracking WHERE material_id = 1 AND stage = 'lavagem');

INSERT INTO tracking (material_id, stage, status)
SELECT 2, 'recebimento', 'concluido'
WHERE NOT EXISTS (SELECT 1 FROM tracking WHERE material_id = 2 AND stage = 'recebimento');

-- Inserir falhas apenas se não existirem
INSERT INTO failures (tracking_id, reason)
SELECT 1, 'Material com impurezas detectadas na inspeção.'
WHERE NOT EXISTS (SELECT 1 FROM failures WHERE tracking_id = 1);

COMMIT;
