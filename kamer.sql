-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Gegenereerd op: 25 jan 2023 om 15:31
-- Serverversie: 10.4.27-MariaDB
-- PHP-versie: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `testb`
--

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `kamer`
--

CREATE TABLE `kamer` (
  `Kamer_ID` int(10) NOT NULL,
  `Kamertype` varchar(20) NOT NULL,
  `Prijs` float NOT NULL,
  `Beschrijving` varchar(250) NOT NULL,
  `Kamerfoto``s` varchar(50) NOT NULL COMMENT 'URL-link',
  `kamernummer` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Gegevens worden geëxporteerd voor tabel `kamer`
--

INSERT INTO `kamer` (`Kamer_ID`, `Kamertype`, `Prijs`, `Beschrijving`, `Kamerfoto``s`, `kamernummer`) VALUES
(1, '1 Persoonskamer', 100, 'leeg', 'leeg', 1),
(2, '1 Persoonskamer', 100, 'leeg', 'leeg', 2),
(3, '1 Persoonskamer', 100, 'leeg', 'leeg', 3),
(4, '1 Persoonskamer', 100, 'leeg', 'leeg', 4),
(5, '1 Persoonskamer', 100, 'leeg', 'leeg', 5),
(6, '2 Persoonskamer', 150, 'leeg', 'leeg', 6),
(7, '2 Persoonskamer', 150, 'leeg', 'leeg', 7),
(8, '2 Persoonskamer', 150, 'leeg', 'leeg', 8),
(9, '2 Persoonskamer', 150, 'leeg', 'leeg', 9),
(10, '2 Persoonskamer', 150, 'leeg', 'leeg', 10),
(11, '2 Persoonskamer', 150, 'leeg', 'leeg', 11),
(12, '2 Persoonskamer', 150, 'leeg', 'leeg', 12),
(13, '2 Persoonskamer', 150, 'leeg', 'leeg', 13),
(14, '2 Persoonskamer', 150, 'leeg', 'leeg', 14),
(15, '2 Persoonskamer', 150, 'leeg', 'leeg', 15),
(16, '2 Persoonskamer', 150, 'leeg', 'leeg', 16),
(17, '2 Persoonskamer', 150, 'leeg', 'leeg', 17),
(18, '2 Persoonskamer', 150, 'leeg', 'leeg', 18),
(19, '2 Persoonskamer', 150, 'leeg', 'leeg', 19),
(20, '2 Persoonskamer', 150, 'leeg', 'leeg', 20),
(21, 'Familiekamer', 200, 'leeg', 'leeg', 21),
(22, 'Familiekamer', 200, 'leeg', 'leeg', 22),
(23, 'Familiekamer', 200, 'leeg', 'leeg', 23),
(24, 'Familiekamer', 200, 'leeg', 'leeg', 24),
(25, 'Familiekamer', 200, 'leeg', 'leeg', 25),
(26, 'Familiekamer', 200, 'leeg', 'leeg', 26),
(27, 'Familiekamer', 200, 'leeg', 'leeg', 27),
(28, 'Familiekamer', 200, 'leeg', 'Leeg', 28),
(29, 'Familiekamer', 200, 'leeg', 'leeg', 29),
(30, 'Familiekamer', 200, 'leeg', 'leeg', 30);

--
-- Indexen voor geëxporteerde tabellen
--

--
-- Indexen voor tabel `kamer`
--
ALTER TABLE `kamer`
  ADD PRIMARY KEY (`Kamer_ID`),
  ADD UNIQUE KEY `kamernummer` (`kamernummer`);

--
-- AUTO_INCREMENT voor geëxporteerde tabellen
--

--
-- AUTO_INCREMENT voor een tabel `kamer`
--
ALTER TABLE `kamer`
  MODIFY `Kamer_ID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
