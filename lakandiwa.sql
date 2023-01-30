-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 27, 2023 at 11:45 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `lakandiwa`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE `attendance` (
  `attendanceID` varchar(50) NOT NULL,
  `id_number` int(8) NOT NULL,
  `time_in` datetime DEFAULT NULL,
  `countersign_time_in` int(8) DEFAULT NULL,
  `signature_time_in` int(8) DEFAULT NULL,
  `time_out` datetime DEFAULT NULL,
  `countersign_time_out` int(8) DEFAULT NULL,
  `signature_time_out` int(8) DEFAULT NULL,
  `work_done` varchar(255) DEFAULT NULL,
  `time_rendered` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `attendance`
--

INSERT INTO `attendance` (`attendanceID`, `id_number`, `time_in`, `countersign_time_in`, `signature_time_in`, `time_out`, `countersign_time_out`, `signature_time_out`, `work_done`, `time_rendered`) VALUES
('36cb0a7c', 20227336, '2023-01-27 22:24:17', NULL, 19924414, '2023-01-27 22:24:26', NULL, 19924414, 'asdasd', '00:00:09'),
('3fb43cc3', 20227336, '2023-01-27 22:28:52', NULL, 19924414, '2023-01-27 22:29:05', NULL, 19924414, 'sadasds', '00:00:13'),
('49b32323', 20227336, '2023-01-27 18:11:52', 20231577, 19924414, '2023-01-27 18:16:04', NULL, 19924414, 'Making BB', '00:04:12'),
('4da1ad6e', 20227336, '2023-01-27 22:27:02', NULL, 19924414, '2023-01-27 22:27:12', NULL, 19924414, 'sdsadasd', '00:00:10'),
('567404d0', 20227336, '2023-01-27 22:26:42', NULL, 19924414, '2023-01-27 22:26:55', NULL, 19924414, 'asdasd', '00:00:13'),
('642a8b5a', 20227336, '2023-01-27 22:28:02', NULL, 19924414, '2023-01-27 22:28:12', NULL, 19924414, 'asdasd', '00:00:10'),
('7677ecbf', 20227336, '2023-01-27 22:28:31', NULL, 19924414, '2023-01-27 22:28:39', NULL, 19924414, 'asdasd', '00:00:08'),
('787eb8af', 20227336, '2023-01-27 22:30:47', NULL, 19924414, '2023-01-27 22:30:57', NULL, 19924414, 'adxsad', '00:00:10'),
('88bcf9d6', 20227336, '2023-01-27 22:22:37', NULL, 19924414, '2023-01-27 22:23:29', NULL, 19924414, 'sasaa', '00:00:52'),
('a6667ae1', 20227336, '2023-01-27 22:24:46', NULL, 19924414, '2023-01-27 22:24:53', NULL, 19924414, 'dasc', '00:00:07'),
('a67a8de8', 20227336, '2023-01-27 22:25:10', NULL, 19924414, '2023-01-27 22:25:20', NULL, 19924414, 'asdasd', '00:00:10'),
('b5419bb0', 20227336, '2023-01-27 22:25:48', NULL, 19924414, '2023-01-27 22:25:56', NULL, 19924414, 'asdsd', '00:00:08'),
('ba108dd5', 20227336, '2023-01-27 22:25:32', NULL, 19924414, '2023-01-27 22:25:41', NULL, 19924414, 'adsadas', '00:00:09'),
('c68e51d8', 20227336, '2023-01-27 22:30:31', NULL, 19924414, '2023-01-27 22:30:39', NULL, 19924414, 'asds', '00:00:08'),
('cb2da4bb', 20227336, '2023-01-27 22:30:14', NULL, 19924414, '2023-01-27 22:30:23', NULL, 19924414, 'sdasd', '00:00:09'),
('d16c1bb8', 20227336, '2023-01-27 15:49:34', NULL, 19924414, '2023-01-27 16:39:14', 20231577, 19924414, 'Making BB', '00:49:40'),
('edc2bea9', 20227336, '2023-01-27 22:26:11', NULL, 19924414, '2023-01-27 22:26:29', NULL, 19924414, 'asdasd', '00:00:18'),
('edcd7a90', 20227336, '2023-01-27 22:23:40', NULL, 19924414, '2023-01-27 22:23:49', NULL, 19924414, 'sdasdas', '00:00:09'),
('f42b2879', 20227336, '2023-01-27 18:19:07', NULL, 19924414, '2023-01-27 18:20:40', NULL, 19924414, 'Writing', '00:01:33'),
('fd3078d6', 20227336, '2023-01-27 22:23:59', NULL, 19924414, '2023-01-27 22:24:10', NULL, 19924414, 'sdadsad', '00:00:11');

-- --------------------------------------------------------

--
-- Table structure for table `member`
--

CREATE TABLE `member` (
  `id_number` int(8) NOT NULL,
  `password` varchar(255) NOT NULL,
  `firstname` varchar(255) NOT NULL,
  `middlename` varchar(255) DEFAULT NULL,
  `lastname` varchar(255) NOT NULL,
  `birthdate` date NOT NULL,
  `positionID` varchar(50) NOT NULL,
  `contact_number` int(11) DEFAULT NULL,
  `dp_filename` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `member`
--

INSERT INTO `member` (`id_number`, `password`, `firstname`, `middlename`, `lastname`, `birthdate`, `positionID`, `contact_number`, `dp_filename`) VALUES
(19887942, 'lakandiwa123', 'HASNA ALTHEA', 'MEDALLO', 'DELOS REYES', '2000-05-01', '7d45d74e', 2147483647, '19887942.jpg'),
(19924414, 'lakandiwa123', 'NATHANIEL', 'CABUAL', 'TIEMPO', '2000-02-23', '462b4ec9', 2147483647, '19924414.jpg'),
(20220943, 'lakandiwa123', 'KYLA', 'D', 'BINONDO', '2002-05-02', 'fe4d0272', 2147483647, '20220943.jpg'),
(20227336, 'lakandiwa123', 'TRIXIA GLENN', 'B', 'VELEZ', '2001-12-05', 'ec5ca665', 2147483647, '20227336.jpg'),
(20231577, 'lakandiwa123', 'DAVE', 'N', 'RACAZA', '2002-05-12', 'ec5ca665', 2147483647, '20231577.jpg'),
(21422456, 'lakandiwa123', 'CATHYRENE ', 'A', 'GIMENEZ', '2003-06-03', 'bc343cdb', 2147483647, '21422456.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `position`
--

CREATE TABLE `position` (
  `positionID` varchar(50) NOT NULL,
  `position` varchar(50) NOT NULL,
  `position_level` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `position`
--

INSERT INTO `position` (`positionID`, `position`, `position_level`) VALUES
('22b686ad', 'Feature Editor', 'Editorial Board'),
('462b4ec9', 'Graphics Editor', 'Editorial Board'),
('72489d17', 'Cartoonist', 'Senior Staff'),
('7c3e93d3', 'Art Editor', 'Editorial Board'),
('7d45d74e', 'Editor in Chief', 'Editorial Board'),
('b3518900', 'Planning and Research Director', 'Editorial Board'),
('bc343cdb', 'Finance Manager', 'Editorial Board'),
('c22dc245', 'Creative Director', 'Editorial Board'),
('dad600ad', 'Photo Editor', 'Editorial Board'),
('deaafd9b', 'Photojournalist', 'Senior Staff'),
('e7eebb52', 'Online Editor', 'Editorial Board'),
('eb63899d', 'Layout Artist', 'Senior Staff'),
('ec5ca665', 'Writer', 'Senior Staff'),
('fe4d0272', 'Managing Director', 'Editorial Board');

-- --------------------------------------------------------

--
-- Table structure for table `position_level`
--

CREATE TABLE `position_level` (
  `position_level` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `position_level`
--

INSERT INTO `position_level` (`position_level`) VALUES
('Editorial Board'),
('Junior Staff'),
('Senior Staff');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `attendance`
--
ALTER TABLE `attendance`
  ADD PRIMARY KEY (`attendanceID`),
  ADD KEY `id_number` (`id_number`),
  ADD KEY `signature_time_in` (`signature_time_in`),
  ADD KEY `signature_time_out` (`signature_time_out`),
  ADD KEY `countersign_time_in` (`countersign_time_in`),
  ADD KEY `countersign_time_out` (`countersign_time_out`);

--
-- Indexes for table `member`
--
ALTER TABLE `member`
  ADD PRIMARY KEY (`id_number`),
  ADD KEY `positionID` (`positionID`);

--
-- Indexes for table `position`
--
ALTER TABLE `position`
  ADD PRIMARY KEY (`positionID`),
  ADD KEY `position_level` (`position_level`);

--
-- Indexes for table `position_level`
--
ALTER TABLE `position_level`
  ADD UNIQUE KEY `position_level` (`position_level`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `attendance`
--
ALTER TABLE `attendance`
  ADD CONSTRAINT `attendance_ibfk_1` FOREIGN KEY (`id_number`) REFERENCES `member` (`id_number`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `attendance_ibfk_2` FOREIGN KEY (`signature_time_in`) REFERENCES `member` (`id_number`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `attendance_ibfk_3` FOREIGN KEY (`signature_time_out`) REFERENCES `member` (`id_number`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `attendance_ibfk_4` FOREIGN KEY (`countersign_time_in`) REFERENCES `member` (`id_number`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `attendance_ibfk_5` FOREIGN KEY (`countersign_time_out`) REFERENCES `member` (`id_number`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `member`
--
ALTER TABLE `member`
  ADD CONSTRAINT `member_ibfk_1` FOREIGN KEY (`positionID`) REFERENCES `position` (`positionID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `position`
--
ALTER TABLE `position`
  ADD CONSTRAINT `position_ibfk_1` FOREIGN KEY (`position_level`) REFERENCES `position_level` (`position_level`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
