-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 08-Ago-2024 às 14:14
-- Versão do servidor: 10.4.27-MariaDB
-- versão do PHP: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `puromilho`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `retorno`
--

CREATE TABLE `retorno` (
  `id` int(11) NOT NULL,
  `nomeVendedor` varchar(40) NOT NULL,
  `qtdMilho` int(3) NOT NULL,
  `qtdCanjicaPequena` int(3) NOT NULL,
  `qtdCanjicaGrande` int(3) NOT NULL,
  `qtdPamonha` int(3) NOT NULL,
  `qtdBoloMilho` int(3) NOT NULL,
  `qtdBoloMacaxeira` int(3) NOT NULL,
  `qtdPeDeMoleque` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `saida`
--

CREATE TABLE `saida` (
  `id` int(8) NOT NULL,
  `nomeVendedor` varchar(40) NOT NULL,
  `qtdMilho` int(3) NOT NULL,
  `qtdCanjicaPequena` int(3) NOT NULL,
  `qtdCanjicaGrande` int(3) NOT NULL,
  `qtdPamonha` int(3) NOT NULL,
  `qtdBoloMilho` int(3) NOT NULL,
  `qtdBoloMacaxeira` int(3) NOT NULL,
  `qtdPeDeMoleque` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `valores`
--

CREATE TABLE `valores` (
  `id` int(11) NOT NULL,
  `vlrMilho` float NOT NULL,
  `vlrCanjicaPequena` float NOT NULL,
  `vlrCanjicaGrande` float NOT NULL,
  `vlrPamonha` float NOT NULL,
  `vlrBoloMilho` float NOT NULL,
  `vlrBoloMacaxeira` float NOT NULL,
  `vlrPeDeMoleque` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `vendedor`
--

CREATE TABLE `vendedor` (
  `id` int(3) NOT NULL,
  `nomeVendedor` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `retorno`
--
ALTER TABLE `retorno`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `saida`
--
ALTER TABLE `saida`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `valores`
--
ALTER TABLE `valores`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `vendedor`
--
ALTER TABLE `vendedor`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `retorno`
--
ALTER TABLE `retorno`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `saida`
--
ALTER TABLE `saida`
  MODIFY `id` int(8) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `valores`
--
ALTER TABLE `valores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `vendedor`
--
ALTER TABLE `vendedor`
  MODIFY `id` int(3) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
