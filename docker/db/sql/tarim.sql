-- MySQL dump 10.13  Distrib 8.0.17, for macos10.14 (x86_64)
--
-- Host: 13.112.7.112    Database: keyboard
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `actions`
--

DROP TABLE IF EXISTS `actions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `actions` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `permission_id` int(11) NOT NULL,
  `name` varchar(500) NOT NULL,
  `slug` varchar(100) NOT NULL,
  `description` varchar(500) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug_UNIQUE` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `actions`
--

LOCK TABLES `actions` WRITE;
/*!40000 ALTER TABLE `actions` DISABLE KEYS */;
INSERT INTO `actions` VALUES (1,17,'Dashboard Access','dashboard.access','','2019-02-28 00:52:36','2019-02-28 03:59:20'),(3,17,'Show statistics','dashboard.statistics','','2019-02-28 00:57:07','2019-02-28 03:59:27'),(12,11,'User Edit','user.edit','','2019-02-28 03:52:42','2019-02-28 04:00:00'),(13,11,'User Delete','user.delete','','2019-02-28 03:57:14','2019-02-28 04:00:10'),(14,12,'Post add','post.add','','2019-02-28 03:57:42','2019-02-28 04:00:15'),(15,12,'Post Edit','post.edit','','2019-02-28 03:58:09','2019-02-28 04:00:21'),(16,13,'Category Add','category.add','','2019-02-28 03:58:40','2019-02-28 04:00:26'),(17,12,'Post Delete','post.delete','','2019-02-28 04:04:24','2019-02-28 04:04:24'),(18,14,'Role Action','role.access','','2019-02-28 04:20:23','2019-03-01 09:12:13'),(19,5,'Permission Action','permission.access','','2019-02-28 04:20:47','2019-03-01 09:12:00'),(20,15,'Action Action','action.access','','2019-02-28 04:21:02','2019-03-01 09:11:48'),(21,13,'Category Delete','category.delete','','2019-02-28 04:25:43','2019-02-28 04:25:43'),(22,13,'Category Edit','category.edit','','2019-02-28 04:26:08','2019-02-28 04:26:08'),(23,18,'Notification Access','notification.access','','2019-03-01 06:58:35','2019-03-01 06:58:35'),(24,11,'User Access','user.access','','2019-03-01 07:06:38','2019-03-01 07:06:38'),(25,11,'User View','user.view','','2019-03-01 09:07:54','2019-03-01 09:07:54'),(26,13,'Category Access','category.access','','2019-03-01 09:13:19','2019-03-01 09:13:19'),(27,12,'Post Access','post.access','','2019-03-01 09:14:55','2019-03-01 09:14:55');
/*!40000 ALTER TABLE `actions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `attachmentable`
--

DROP TABLE IF EXISTS `attachmentable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attachmentable` (
  `id` int(11) NOT NULL,
  `attachmentable_type` varchar(500) NOT NULL,
  `attachmentable_id` int(11) NOT NULL,
  `attachment_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attachmentable`
--

LOCK TABLES `attachmentable` WRITE;
/*!40000 ALTER TABLE `attachmentable` DISABLE KEYS */;
/*!40000 ALTER TABLE `attachmentable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `attachments`
--

DROP TABLE IF EXISTS `attachments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attachments` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `original_name` varchar(100) DEFAULT NULL,
  `mime` varchar(100) DEFAULT NULL,
  `extension` varchar(40) DEFAULT NULL,
  `size` varchar(100) DEFAULT NULL,
  `sort` int(11) DEFAULT NULL,
  `path` varchar(500) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `alt` varchar(500) DEFAULT NULL,
  `hash` varchar(500) DEFAULT NULL,
  `disk` varchar(30) DEFAULT NULL,
  `group` varchar(500) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attachments`
--

LOCK TABLES `attachments` WRITE;
/*!40000 ALTER TABLE `attachments` DISABLE KEYS */;
INSERT INTO `attachments` VALUES (31,8,NULL,'print.png','image/png',NULL,'262059',NULL,'storage/2019/09/16/',NULL,NULL,NULL,'local',NULL,'2019-09-16 03:43:39','2019-09-16 03:43:39',NULL),(32,8,NULL,'variable.png','image/png','png','440753',NULL,'storage/2019/09/16/',NULL,NULL,NULL,'local',NULL,'2019-09-16 03:45:33','2019-09-16 03:45:33',NULL),(33,8,'1cb143c316dd463da11ac195ad862f4d','me.jpg','image/jpeg','jpg','129709',NULL,'storage/2019/09/16/',NULL,NULL,NULL,'local',NULL,'2019-09-16 03:49:54','2019-09-16 03:49:54',NULL),(34,8,'808a8dab59fe418dbac17945859cf968','me.png','image/png','png','476399',NULL,'storage/2019/09/16/',NULL,NULL,NULL,'local',NULL,'2019-09-16 03:51:07','2019-09-16 03:51:07',NULL),(35,8,'869e2b8ac7d94517a2c61dd0b589bf3e','me.jpg','image/jpeg','jpg','129709',NULL,'storage/2019/09/16/',NULL,NULL,NULL,'local',NULL,'2019-09-16 12:28:22','2019-09-16 12:28:22',NULL),(36,8,'46c5e2e5290344c28bb8e25e1d4e3af3','me.jpg','image/jpeg','jpg','129709',NULL,'storage/2019/09/16/',NULL,NULL,NULL,'local',NULL,'2019-09-16 12:38:53','2019-09-16 12:38:53',NULL),(37,8,'0eeaf101eeb64f298d27a29d74666d98','variable.png','image/png','png','440753',NULL,'storage/2019/09/16/',NULL,NULL,NULL,'local',NULL,'2019-09-16 12:39:18','2019-09-16 12:39:18',NULL),(38,8,'a6227e7297da41b5b2827ecd1c388968','me.jpg','image/jpeg','jpg','129709',NULL,'storage/2019/09/16/',NULL,NULL,NULL,'local',NULL,'2019-09-16 12:45:24','2019-09-16 12:45:24',NULL),(39,8,'99c59ea178ca46dabc8c72b26bebd2fb','me.jpg','image/jpeg','jpg','129709',NULL,'storage/2019/09/16/',NULL,NULL,NULL,'local',NULL,'2019-09-16 12:55:46','2019-09-16 12:55:46',NULL),(40,8,'337d6e6f58fa473f8d4d7066ea5f8e17','group_2.png','image/png','png','131434',NULL,'storage/2019/09/21/',NULL,NULL,NULL,'local',NULL,'2019-09-21 09:30:14','2019-09-21 09:30:14',NULL);
/*!40000 ALTER TABLE `attachments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_history`
--

DROP TABLE IF EXISTS `auth_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_history` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `os` varchar(100) DEFAULT NULL,
  `platform` varchar(100) DEFAULT NULL,
  `platform_version` varchar(100) DEFAULT NULL,
  `browser` varchar(100) DEFAULT NULL,
  `browser_version` varchar(10) DEFAULT NULL,
  `ip_address` varchar(100) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_history`
--

LOCK TABLES `auth_history` WRITE;
/*!40000 ALTER TABLE `auth_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `type` varchar(500) NOT NULL,
  `title` varchar(500) NOT NULL,
  `slug` varchar(500) DEFAULT NULL,
  `sort` int(11) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `options` json DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'blog','daily contents','test',NULL,'',NULL,'2019-03-12 07:10:37','2019-03-12 09:18:02'),(2,'blog','test','test',NULL,'',NULL,'2019-03-12 07:15:39','2019-03-12 09:17:48');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category_posts`
--

DROP TABLE IF EXISTS `category_posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category_posts` (
  `category_id` int(11) NOT NULL,
  `post_id` varchar(45) NOT NULL,
  PRIMARY KEY (`category_id`,`post_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category_posts`
--

LOCK TABLES `category_posts` WRITE;
/*!40000 ALTER TABLE `category_posts` DISABLE KEYS */;
INSERT INTO `category_posts` VALUES (1,'10'),(1,'4'),(1,'7'),(1,'8'),(2,'10'),(2,'4'),(2,'6'),(2,'8');
/*!40000 ALTER TABLE `category_posts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `content_field`
--

DROP TABLE IF EXISTS `content_field`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `content_field` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `content_type_id` int(11) NOT NULL,
  `field_type` varchar(100) NOT NULL,
  `title` varchar(500) NOT NULL,
  `place` varchar(45) DEFAULT 'main' COMMENT 'main or side',
  `name` varchar(100) NOT NULL,
  `show_in_table` tinyint(1) DEFAULT '0',
  `sort` int(11) DEFAULT '0',
  `dataattr` varchar(1000) DEFAULT NULL,
  `default_value` varchar(1000) DEFAULT NULL,
  `is_required` tinyint(1) DEFAULT '0',
  `regex` varchar(500) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `content_field`
--

LOCK TABLES `content_field` WRITE;
/*!40000 ALTER TABLE `content_field` DISABLE KEYS */;
INSERT INTO `content_field` VALUES (2,1,'input','Description','main','content.description',1,1,'',NULL,0,'','2019-03-03 02:29:44','2019-03-20 01:44:59'),(3,1,'input','Password','side','content.password',0,4,'',NULL,0,'','2019-03-03 02:30:51','2019-03-20 01:45:48'),(4,1,'datetime','Publish at','side','content.publish_at',0,3,'{\"enable-time\": \"true\",\r\n\"time_24hr\": \"true\",\r\n\"allow-input\": \"true\",\r\n\"date-format\":\"Y-m-d h:i:s\"}',NULL,0,'','2019-03-05 02:37:59','2019-03-20 01:45:06'),(5,1,'tinymce','Content','main','content.content',0,2,'{\"theme\": \"modern\"}',NULL,0,'required|min:10|max:5000','2019-03-05 02:38:25','2019-03-20 01:48:56'),(7,1,'input','cover','side','content.cover',0,6,'',NULL,0,'','2019-03-06 05:19:34','2019-03-20 01:45:40'),(8,2,'input','Title','main','content.title',0,0,'',NULL,0,'','2019-03-06 12:32:18','2019-03-20 03:10:20'),(9,3,'input','Title','main','content.title',0,0,NULL,NULL,0,'0','2019-03-06 12:33:01','2019-03-19 10:41:54'),(10,1,'input','Title','main','content.title',1,0,'',NULL,1,'required','2019-03-11 11:34:59','2019-03-20 03:16:07'),(11,1,'category','Category','side','category',0,7,'',NULL,0,'','2019-03-12 05:27:03','2019-03-20 01:45:21'),(12,1,'tag','Tag','side','tag',0,8,'',NULL,0,'','2019-03-12 05:27:33','2019-03-20 01:45:14'),(13,2,'category','Category','side','content.category',0,0,'',NULL,0,'','2019-03-12 07:33:58','2019-03-20 03:10:31'),(14,1,'upload','Files','side','files',0,5,'{\"name\": \"files\"}',NULL,0,'','2019-03-14 03:24:53','2019-09-16 11:02:32'),(15,2,'input','Keywords','main','Keyword',0,0,'',NULL,0,'','2019-03-20 03:10:11','2019-03-20 03:10:11'),(16,3,'tinymce','Content','main','content.content',0,0,'',NULL,0,'','2019-09-15 08:55:14','2019-09-15 08:56:45');
/*!40000 ALTER TABLE `content_field` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `content_type`
--

DROP TABLE IF EXISTS `content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `content_type` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(500) DEFAULT NULL,
  `slug` varchar(100) DEFAULT NULL,
  `description` varchar(1000) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `content_type`
--

LOCK TABLES `content_type` WRITE;
/*!40000 ALTER TABLE `content_type` DISABLE KEYS */;
INSERT INTO `content_type` VALUES (1,'Blog','blog','Blog posts','2019-03-02 03:43:50','2019-03-10 02:38:16'),(2,'News','news','Latest News','2019-03-02 03:46:25','2019-03-18 13:07:51'),(3,'Pages','pages','test','2019-03-02 03:46:39','2019-03-18 13:20:09');
/*!40000 ALTER TABLE `content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `password_resets`
--

DROP TABLE IF EXISTS `password_resets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `password_resets` (
  `email` int(11) NOT NULL,
  `token` varchar(60) NOT NULL,
  `created_at` varchar(60) NOT NULL,
  `expire_at` varchar(60) NOT NULL,
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `password_resets`
--

LOCK TABLES `password_resets` WRITE;
/*!40000 ALTER TABLE `password_resets` DISABLE KEYS */;
/*!40000 ALTER TABLE `password_resets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permissions`
--

DROP TABLE IF EXISTS `permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `permissions` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(500) NOT NULL,
  `slug` varchar(100) NOT NULL,
  `description` varchar(500) DEFAULT NULL,
  `sort` int(11) DEFAULT '0',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug_UNIQUE` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permissions`
--

LOCK TABLES `permissions` WRITE;
/*!40000 ALTER TABLE `permissions` DISABLE KEYS */;
INSERT INTO `permissions` VALUES (5,'Permission','permission','',6,'2019-02-25 05:10:55','2019-02-28 04:19:15'),(11,'Users','user','',2,'2019-02-28 03:06:08','2019-02-28 04:17:31'),(12,'Posts','post','',3,'2019-02-28 03:06:16','2019-02-28 04:17:40'),(13,'Category','category','',4,'2019-02-28 03:06:26','2019-02-28 04:17:52'),(14,'Role','role','',5,'2019-02-28 03:06:36','2019-02-28 04:19:08'),(15,'Actions','action','',7,'2019-02-28 03:07:02','2019-02-28 04:19:21'),(17,'Dashboard','dashboard','test',1,'2019-02-28 04:14:24','2019-03-18 13:37:17'),(18,'Notification','notification','',1,'2019-03-01 06:58:02','2019-03-01 06:58:14');
/*!40000 ALTER TABLE `permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `posts`
--

DROP TABLE IF EXISTS `posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `posts` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `type` varchar(45) NOT NULL,
  `slug` varchar(500) DEFAULT NULL,
  `content` json DEFAULT NULL,
  `click` int(11) DEFAULT '0',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posts`
--

LOCK TABLES `posts` WRITE;
/*!40000 ALTER TABLE `posts` DISABLE KEYS */;
INSERT INTO `posts` VALUES (5,8,'blog',NULL,'{\"cover\": \"cover\", \"title\": \"test title\", \"content\": \"content\", \"password\": \"test passport\", \"publish_at\": \"2019-03-21 12:00:0\", \"description\": \"description\"}',0,'2019-03-12 06:12:40','2019-06-05 01:50:07',NULL),(6,8,'blog',NULL,'{\"cover\": \"latest content\", \"title\": \"xxxxxxxx\", \"content\": \"<p>fds</p>\", \"password\": \"latest content\", \"publish_at\": \"2019-03-21 3:00:0\", \"description\": \"test desc\"}',0,'2019-03-12 06:26:37','2019-06-05 01:49:40',NULL),(9,8,'blog',NULL,'{\"cover\": \"\", \"title\": \"dsgsdf\", \"content\": \"<p>gfds</p>\", \"password\": \"\", \"publish_at\": \"\", \"description\": \"gf\"}',0,'2019-06-05 02:15:41','2019-06-06 12:09:04',NULL),(10,8,'blog',NULL,'{\"cover\": \"\", \"title\": \"سىناق يازما\", \"content\": \"<p>سىناق يازما</p>\", \"password\": \"\", \"publish_at\": \"\", \"description\": \"سىناق يازما\"}',0,'2019-06-05 02:16:06','2019-09-15 08:49:30',NULL);
/*!40000 ALTER TABLE `posts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role_action`
--

DROP TABLE IF EXISTS `role_action`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `role_action` (
  `role_id` int(11) NOT NULL,
  `action_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role_action`
--

LOCK TABLES `role_action` WRITE;
/*!40000 ALTER TABLE `role_action` DISABLE KEYS */;
INSERT INTO `role_action` VALUES (2,1),(2,3),(2,23),(2,12),(2,13),(2,24),(2,25),(2,14),(2,15),(2,17),(2,27),(2,16),(2,21),(2,22),(2,26),(2,18),(2,19),(2,20),(4,1),(4,3),(4,23);
/*!40000 ALTER TABLE `role_action` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(500) NOT NULL,
  `slug` varchar(100) NOT NULL,
  `description` varchar(500) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug_UNIQUE` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (2,'Manager','manager','','2019-02-25 05:30:15','2019-02-28 05:36:04'),(3,'Writer','writer','Writer','2019-02-25 05:30:32','2019-02-25 05:30:32'),(4,'supervisiour','supervisiour','','2019-02-27 03:42:44','2019-02-28 05:21:50');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `taggable`
--

DROP TABLE IF EXISTS `taggable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `taggable` (
  `post_id` int(11) NOT NULL,
  `tag_id` varchar(45) NOT NULL,
  PRIMARY KEY (`post_id`,`tag_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `taggable`
--

LOCK TABLES `taggable` WRITE;
/*!40000 ALTER TABLE `taggable` DISABLE KEYS */;
INSERT INTO `taggable` VALUES (6,'10'),(6,'8'),(8,'5'),(9,'16'),(9,'5'),(9,'8'),(10,'5');
/*!40000 ALTER TABLE `taggable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tags`
--

DROP TABLE IF EXISTS `tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tags` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `slug` varchar(500) DEFAULT NULL,
  `name` varchar(500) DEFAULT NULL,
  `count` int(11) DEFAULT '0',
  `type` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tags`
--

LOCK TABLES `tags` WRITE;
/*!40000 ALTER TABLE `tags` DISABLE KEYS */;
INSERT INTO `tags` VALUES (5,'test','test',24,NULL),(6,'aaa','aaa',4,NULL),(8,'nur','Nur',13,NULL),(10,'algha','algha',7,NULL),(16,'asa','asa',3,NULL);
/*!40000 ALTER TABLE `tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_device`
--

DROP TABLE IF EXISTS `user_device`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_device` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `os` varchar(60) DEFAULT NULL,
  `model` varchar(60) DEFAULT NULL,
  `version` varchar(60) DEFAULT NULL,
  `token` varchar(200) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_device`
--

LOCK TABLES `user_device` WRITE;
/*!40000 ALTER TABLE `user_device` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_device` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_profile`
--

DROP TABLE IF EXISTS `user_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_profile` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `avatar` varchar(200) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `status` varchar(500) DEFAULT NULL,
  `is_online` tinyint(1) DEFAULT '0',
  `be_notified` tinyint(1) DEFAULT '0',
  `last_seen_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_profile`
--

LOCK TABLES `user_profile` WRITE;
/*!40000 ALTER TABLE `user_profile` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_role`
--

DROP TABLE IF EXISTS `user_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_role` (
  `user_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_role`
--

LOCK TABLES `user_role` WRITE;
/*!40000 ALTER TABLE `user_role` DISABLE KEYS */;
INSERT INTO `user_role` VALUES (17,1),(18,2),(19,2),(22,1),(22,2),(22,3),(9,4),(23,4);
/*!40000 ALTER TABLE `user_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_verification`
--

DROP TABLE IF EXISTS `user_verification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_verification` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `verify_token` varchar(60) DEFAULT NULL,
  `expire_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_verification`
--

LOCK TABLES `user_verification` WRITE;
/*!40000 ALTER TABLE `user_verification` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_verification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `account` varchar(30) DEFAULT NULL,
  `password` varchar(60) NOT NULL,
  `access_token` varchar(100) DEFAULT NULL,
  `locale` varchar(2) DEFAULT 'en',
  `status` tinyint(1) DEFAULT NULL,
  `is_online` tinyint(1) DEFAULT '0',
  `email_verified_at` timestamp NULL DEFAULT NULL,
  `last_login` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NOT NULL,
  `updated_at` timestamp NOT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `is_admin` smallint(6) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (8,'algha','algha@outlook.com','algha','$2y$12$E16iN2jMVDe48bcdLfZu6eWut1HcivsgN1fU/jLxq/0eifVsZnAka','xx','en',1,0,NULL,NULL,'2019-01-23 10:47:24','2019-04-03 06:45:06',NULL,1),(23,'test@gmail.com','test@gmail.com','test@gmail.com','$2b$12$uKYAnUMvPX0rFW4clVfpRenUMHoCKauvaIP3JzSgzSm6W1eIA7LN2',NULL,'en',NULL,0,NULL,NULL,'2019-03-01 13:59:31','2019-03-01 13:59:31',NULL,0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-09-21 18:32:42
