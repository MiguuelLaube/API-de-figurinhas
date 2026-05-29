-- ============================================================
-- Script SQL - API Figurinhas da Copa
-- Importar no phpMyAdmin do XAMPP
-- ============================================================

-- Criar o banco de dados (caso não exista)
CREATE DATABASE IF NOT EXISTS db_time
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_general_ci;

USE db_time;

-- Criar a tabela de figurinhas
CREATE TABLE IF NOT EXISTS tb_figurinhas (
    cod_figurinha INT AUTO_INCREMENT PRIMARY KEY,
    nome_jogador VARCHAR(100) NOT NULL,
    pais VARCHAR(50) NOT NULL,
    posicao VARCHAR(50) NOT NULL,
    numero_camisa INT NOT NULL,
    raridade VARCHAR(20) NOT NULL DEFAULT 'Comum',
    repetida TINYINT(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================================
-- Popular com figurinhas da Copa do Mundo
-- ============================================================

INSERT INTO tb_figurinhas (nome_jogador, pais, posicao, numero_camisa, raridade, repetida) VALUES
-- 🇧🇷 Brasil
('Neymar Jr', 'Brasil', 'Atacante', 10, 'Lendária', 0),
('Vinícius Jr', 'Brasil', 'Atacante', 7, 'Rara', 0),
('Casemiro', 'Brasil', 'Meio-campo', 5, 'Comum', 1),
('Alisson', 'Brasil', 'Goleiro', 1, 'Rara', 0),
('Marquinhos', 'Brasil', 'Defensor', 4, 'Comum', 0),

-- 🇦🇷 Argentina
('Lionel Messi', 'Argentina', 'Atacante', 10, 'Lendária', 0),
('Ángel Di María', 'Argentina', 'Atacante', 11, 'Rara', 1),
('Emiliano Martínez', 'Argentina', 'Goleiro', 23, 'Rara', 0),
('Rodrigo De Paul', 'Argentina', 'Meio-campo', 7, 'Comum', 0),
('Julián Álvarez', 'Argentina', 'Atacante', 9, 'Comum', 1),

-- 🇫🇷 França
('Kylian Mbappé', 'França', 'Atacante', 10, 'Lendária', 0),
('Antoine Griezmann', 'França', 'Atacante', 7, 'Rara', 0),
('Hugo Lloris', 'França', 'Goleiro', 1, 'Comum', 1),
('N''Golo Kanté', 'França', 'Meio-campo', 13, 'Rara', 0),
('Ousmane Dembélé', 'França', 'Atacante', 11, 'Comum', 0),

-- 🇩🇪 Alemanha
('Manuel Neuer', 'Alemanha', 'Goleiro', 1, 'Rara', 0),
('Joshua Kimmich', 'Alemanha', 'Meio-campo', 6, 'Rara', 1),
('Jamal Musiala', 'Alemanha', 'Meio-campo', 14, 'Comum', 0),

-- 🇪🇸 Espanha
('Pedri', 'Espanha', 'Meio-campo', 26, 'Rara', 0),
('Gavi', 'Espanha', 'Meio-campo', 9, 'Comum', 0),
('Álvaro Morata', 'Espanha', 'Atacante', 7, 'Comum', 1),

-- 🏴 Inglaterra
('Harry Kane', 'Inglaterra', 'Atacante', 9, 'Lendária', 0),
('Jude Bellingham', 'Inglaterra', 'Meio-campo', 22, 'Rara', 0),
('Bukayo Saka', 'Inglaterra', 'Atacante', 7, 'Comum', 0),

-- 🇵🇹 Portugal
('Cristiano Ronaldo', 'Portugal', 'Atacante', 7, 'Lendária', 0),
('Bruno Fernandes', 'Portugal', 'Meio-campo', 8, 'Rara', 1),
('Bernardo Silva', 'Portugal', 'Meio-campo', 10, 'Comum', 0),

-- 🇭🇷 Croácia
('Luka Modrić', 'Croácia', 'Meio-campo', 10, 'Lendária', 0),

-- 🇺🇾 Uruguai
('Federico Valverde', 'Uruguai', 'Meio-campo', 15, 'Rara', 0);
