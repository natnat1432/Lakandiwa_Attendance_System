-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 30, 2023 at 09:33 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `attendance`
--

INSERT INTO `attendance` (`attendanceID`, `id_number`, `time_in`, `countersign_time_in`, `signature_time_in`, `time_out`, `countersign_time_out`, `signature_time_out`, `work_done`, `time_rendered`) VALUES
('ebc794ff', 19924414, '2023-01-30 16:32:56', NULL, NULL, NULL, NULL, NULL, NULL, NULL);

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
  `contact_number` varchar(11) DEFAULT NULL,
  `dp_filename` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `member`
--

INSERT INTO `member` (`id_number`, `password`, `firstname`, `middlename`, `lastname`, `birthdate`, `positionID`, `contact_number`, `dp_filename`) VALUES
(5870324, 'lakandiwa123', 'JUVYL', 'T', 'SABANAL', '1986-09-24', 'eb63899d', '09218611119', '05870324.jpg'),
(18740779, 'lakandiwa123', 'BERNADINE', 'E', 'GARCIA', '1998-08-17', 'deaafd9b', '09672193878', '18740779.jpg'),
(19378843, 'lakandiwa123', 'NINETTE ANN', 'CRUZADA', 'BUGHAO', '2000-07-31', '7c3e93d3', '2147483647', '19378843.jpg'),
(19837277, 'lakandiwa123', 'MARK DENVER ', 'Y', 'HONTIVEROS', '2000-07-08', '72489d17', '09686853871', '19837277.jpg'),
(19886076, 'lakandiwa123', 'ADAM', 'LUCERO', 'SOLON', '2001-06-21', 'dad600ad', '2147483647', '19886076.jpg'),
(19887934, 'lakandiwa123', 'ARRIANE KAYE', 'L', 'RACAZA', '2000-10-03', 'e7eebb52', '2147483647', '19887934.jpg'),
(19887942, 'lakandiwa123', 'HASNA ALTHEA', 'MEDALLO', 'DELOS REYES', '2000-05-01', '7d45d74e', '2147483647', '19887942.jpg'),
(19888593, 'lakandiwa123', 'REMUEL', 'BODERO', 'DELA CRUZ', '2000-02-04', '72489d17', '09151367541', '19888593.jpg'),
(19897826, 'lakandiwa123', 'ANGELA MAE', 'S', 'TORRES', '2001-03-26', 'b3518900', '2147483647', '19897826.jpg'),
(19924414, 'natnat2232000', 'NATHANIEL', 'CABUAL', 'TIEMPO', '2000-02-23', '462b4ec9', '2147483647', '19924414.jpg'),
(19930841, 'lakandiwa123', 'CHRISTIAN JACOB', 'B', 'DEIMOS', '2003-08-27', 'deaafd9b', '09361147032', '19930841.jpg'),
(20220935, 'lakandiwa123', 'KYZEN', 'D', 'BINONDO', '2002-05-02', '22b686ad', '2147483647', '20220935.jpg'),
(20220943, 'lakandiwa123', 'KYLA', 'D', 'BINONDO', '2002-05-02', 'fe4d0272', '2147483647', '20220943.jpg'),
(20227336, 'lakandiwa123', 'TRIXIA GLENN', 'B', 'VELEZ', '2001-12-05', 'ec5ca665', '2147483647', '20227336.jpg'),
(20227955, 'lakandiwa123', 'JOHN CLEISTER', 'C', 'BARRIENTOS', '2002-06-14', 'deaafd9b', '09978600689', '20227955.jpg'),
(20231577, 'lakandiwa123', 'DAVE', 'N', 'RACAZA', '2002-05-12', 'ec5ca665', '2147483647', '20231577.jpg'),
(20233755, 'lakandiwa123', 'SARC FRANCIS ADRIANNE ', 'T', 'AMPO-ON', '2001-10-11', '72489d17', '09203780708', '20233755.jpg'),
(20287140, 'lakandiwa123', 'KARREN MARIE', 'B', 'SISMAR', '2002-04-09', 'deaafd9b', '09755039949', '20287140.jpg'),
(21422456, 'lakandiwa123', 'CATHYRENE', 'A', 'GIMENEZ', '2003-06-10', 'bc343cdb', '2147483647', '21422456.jpg'),
(21427224, 'lakandiwa123', 'LEN', 'D', 'NUÑEZ', '2003-05-21', 'eb63899d', '09490198899', '21427224.jpg'),
(21436266, 'lakandiwa123', 'ARGYLE JOSEPH ', 'M', 'LAURONILLA', '2003-03-14', 'ec5ca665', '09277719121', '21436266.jpg'),
(21436480, 'lakandiwa123', 'MARIE CHASTINE', 'V', 'LANZADERAS', '2002-03-21', 'eb63899d', '09206134009', '21436480.jpg'),
(22702344, 'lakandiwa123', 'ADRIENNE', 'C', 'EYAO', '2003-09-09', 'eb63899d', '09661886312', '22702344.jpg'),
(22713135, 'lakandiwa123', 'NICHOLS JOHN', 'M', 'ILLUT', '2002-09-17', 'deaafd9b', '09519332394', '22713135.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `position`
--

CREATE TABLE `position` (
  `positionID` varchar(50) NOT NULL,
  `position` varchar(50) NOT NULL,
  `position_level` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `position`
--

INSERT INTO `position` (`positionID`, `position`, `position_level`) VALUES
('22b686ad', 'Feature Editor', 'Editorial Board'),
('462b4ec9', 'Graphics Editor', 'Editorial Board'),
('72489d17', 'Cartoonist', 'Senior Staff'),
('7c3e93d3', 'Art Editor', 'Editorial Board'),
('7d45d74e', 'Editor in Chief', 'Editorial Board'),
('9ea3e6db', 'Ethics and Legal Standards Editor', 'Editorial Board'),
('b3518900', 'Planning and Research Director', 'Editorial Board'),
('bc343cdb', 'Finance Manager', 'Editorial Board'),
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
