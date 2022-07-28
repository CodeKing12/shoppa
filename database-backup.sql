-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: localhost    Database: shoppa
-- ------------------------------------------------------
-- Server version	8.0.29-0ubuntu0.20.04.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounts_addressbook`
--

DROP TABLE IF EXISTS `accounts_addressbook`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_addressbook` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `address` varchar(250) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_addressbook`
--

LOCK TABLES `accounts_addressbook` WRITE;
/*!40000 ALTER TABLE `accounts_addressbook` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_addressbook` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_apiuser`
--

DROP TABLE IF EXISTS `accounts_apiuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_apiuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `product_groups` json NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `accounts_apiuser_user_id_1bd682e5_fk_accounts_customaccount_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_customaccount` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_apiuser`
--

LOCK TABLES `accounts_apiuser` WRITE;
/*!40000 ALTER TABLE `accounts_apiuser` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_apiuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_cart`
--

DROP TABLE IF EXISTS `accounts_cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_cart` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_cart_user_id_18c76270_fk_accounts_customaccount_id` (`user_id`),
  CONSTRAINT `accounts_cart_user_id_18c76270_fk_accounts_customaccount_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_customaccount` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_cart`
--

LOCK TABLES `accounts_cart` WRITE;
/*!40000 ALTER TABLE `accounts_cart` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_cartdetails`
--

DROP TABLE IF EXISTS `accounts_cartdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_cartdetails` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `color` varchar(18) NOT NULL,
  `cart_id` bigint NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_cartdetails_cart_id_6dfecbe3_fk_accounts_cart_id` (`cart_id`),
  KEY `accounts_cartdetails_product_id_af0399bc_fk_products_product_id` (`product_id`),
  CONSTRAINT `accounts_cartdetails_cart_id_6dfecbe3_fk_accounts_cart_id` FOREIGN KEY (`cart_id`) REFERENCES `accounts_cart` (`id`),
  CONSTRAINT `accounts_cartdetails_product_id_af0399bc_fk_products_product_id` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_cartdetails`
--

LOCK TABLES `accounts_cartdetails` WRITE;
/*!40000 ALTER TABLE `accounts_cartdetails` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_cartdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_customaccount`
--

DROP TABLE IF EXISTS `accounts_customaccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_customaccount` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `username` varchar(70) DEFAULT NULL,
  `phone_number` varchar(17) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `address` varchar(250) NOT NULL,
  `is_apiuser` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_customaccount`
--

