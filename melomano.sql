-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-07-2025 a las 10:12:46
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `melomano`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `album`
--

CREATE TABLE `album` (
  `id` int(11) NOT NULL,
  `titulo` varchar(65) NOT NULL,
  `año` int(11) NOT NULL,
  `descripcion` text DEFAULT NULL,
  `medio` enum('CD','Cassette','Vinilo','Digital','Otro') NOT NULL,
  `usuario_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `album_artista`
--

CREATE TABLE `album_artista` (
  `album_id` int(11) NOT NULL,
  `artista_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `album_cancion`
--

CREATE TABLE `album_cancion` (
  `album_id` int(11) NOT NULL,
  `cancion_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `artista`
--

CREATE TABLE `artista` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `artista`
--

INSERT INTO `artista` (`id`, `nombre`) VALUES
(1, 'Queen'),
(2, 'Adele'),
(3, 'Coldplay'),
(4, 'Shakira'),
(5, 'Diomedes Diaz'),
(7, 'bad buny');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cancion`
--

CREATE TABLE `cancion` (
  `id` int(11) NOT NULL,
  `titulo` varchar(65) NOT NULL,
  `duracion_min` int(11) NOT NULL,
  `duracion_seg` int(11) NOT NULL,
  `interprete_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `cancion`
--

INSERT INTO `cancion` (`id`, `titulo`, `duracion_min`, `duracion_seg`, `interprete_id`) VALUES
(1, 'Bohemian Rhapsody', 5, 55, 1),
(2, 'Rolling in the Deep', 3, 48, 2),
(3, 'Viva La Vida', 4, 2, 3),
(4, 'Hips Don’t Lie', 3, 38, 4),
(5, 'Let It Be', 4, 3, 5),
(6, 'Yellow', 4, 29, 3),
(7, 'Shape of You', 4, 24, 2),
(8, 'Waka Waka', 3, 20, 4),
(9, 'Hey Jude', 7, 11, 5),
(10, 'Under Pressure', 4, 10, 1),
(11, 'Don’t Stop Me Now', 3, 29, 1),
(12, 'Someone Like You', 4, 45, 2),
(13, 'Fix You', 4, 55, 3),
(14, 'Whenever, Wherever', 3, 16, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `apellido` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `name`, `apellido`, `email`, `password`) VALUES
(17, 'Erick', 'López', 'eri@gmail.com', '$2b$12$6EpvUqA6arFHcaq4MShL2OIQ4ZSAe71.QxNXbQzzl6ZS6Khqv5TTS');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `album`
--
ALTER TABLE `album`
  ADD PRIMARY KEY (`id`),
  ADD KEY `usuario_id` (`usuario_id`);

--
-- Indices de la tabla `album_artista`
--
ALTER TABLE `album_artista`
  ADD PRIMARY KEY (`album_id`,`artista_id`),
  ADD KEY `artista_id` (`artista_id`);

--
-- Indices de la tabla `album_cancion`
--
ALTER TABLE `album_cancion`
  ADD PRIMARY KEY (`album_id`,`cancion_id`),
  ADD KEY `cancion_id` (`cancion_id`);

--
-- Indices de la tabla `artista`
--
ALTER TABLE `artista`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `cancion`
--
ALTER TABLE `cancion`
  ADD PRIMARY KEY (`id`),
  ADD KEY `interprete_id` (`interprete_id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `album`
--
ALTER TABLE `album`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de la tabla `artista`
--
ALTER TABLE `artista`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `cancion`
--
ALTER TABLE `cancion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `album`
--
ALTER TABLE `album`
  ADD CONSTRAINT `album_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`);

--
-- Filtros para la tabla `album_artista`
--
ALTER TABLE `album_artista`
  ADD CONSTRAINT `album_artista_ibfk_1` FOREIGN KEY (`album_id`) REFERENCES `album` (`id`),
  ADD CONSTRAINT `album_artista_ibfk_2` FOREIGN KEY (`artista_id`) REFERENCES `artista` (`id`);

--
-- Filtros para la tabla `album_cancion`
--
ALTER TABLE `album_cancion`
  ADD CONSTRAINT `album_cancion_ibfk_1` FOREIGN KEY (`album_id`) REFERENCES `album` (`id`),
  ADD CONSTRAINT `album_cancion_ibfk_2` FOREIGN KEY (`cancion_id`) REFERENCES `cancion` (`id`);

--
-- Filtros para la tabla `cancion`
--
ALTER TABLE `cancion`
  ADD CONSTRAINT `cancion_ibfk_1` FOREIGN KEY (`interprete_id`) REFERENCES `artista` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
