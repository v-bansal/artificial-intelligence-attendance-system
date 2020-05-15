-- phpMyAdmin SQL Dump
-- version 4.0.4
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 13, 2020 at 09:33 AM
-- Server version: 5.6.12-log
-- PHP Version: 5.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `python-face`
--
CREATE DATABASE IF NOT EXISTS `python-face` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `python-face`;

-- --------------------------------------------------------

--
-- Table structure for table `attandance_data`
--

CREATE TABLE IF NOT EXISTS `attandance_data` (
  `id` int(8) NOT NULL AUTO_INCREMENT,
  `personal_no` varchar(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `section` varchar(20) NOT NULL,
  `att_date` date NOT NULL,
  `time_in` time NOT NULL,
  `time_out` time NOT NULL,
  `desig` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `personal_no` (`personal_no`),
  UNIQUE KEY `personal_no_2` (`personal_no`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;

--
-- Dumping data for table `attandance_data`
--

INSERT INTO `attandance_data` (`id`, `personal_no`, `name`, `section`, `att_date`, `time_in`, `time_out`, `desig`) VALUES
(10, '123', '', '', '2020-05-13', '02:13:44', '00:00:00', '');

-- --------------------------------------------------------

--
-- Table structure for table `reg_users`
--

CREATE TABLE IF NOT EXISTS `reg_users` (
  `id` int(8) NOT NULL DEFAULT '0',
  `personal_no` varchar(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `section` varchar(20) NOT NULL,
  `desig` varchar(50) NOT NULL,
  `reg_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `personal_no` (`personal_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
