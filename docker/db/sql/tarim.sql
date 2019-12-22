-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: db
-- Generation Time: Dec 22, 2019 at 01:03 PM
-- Server version: 8.0.18
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tarim`
--

-- --------------------------------------------------------

--
-- Table structure for table `actions`
--

CREATE TABLE `actions` (
  `id` int(10) UNSIGNED NOT NULL,
  `permission_id` int(11) NOT NULL,
  `name` varchar(500) NOT NULL,
  `slug` varchar(100) NOT NULL,
  `description` varchar(500) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `actions`
--

INSERT INTO `actions` (`id`, `permission_id`, `name`, `slug`, `description`, `created_at`, `updated_at`) VALUES
(1, 17, 'Dashboard Access', 'dashboard.access', '', '2019-02-28 00:52:36', '2019-02-28 03:59:20'),
(3, 17, 'Show statistics', 'dashboard.statistics', '', '2019-02-28 00:57:07', '2019-02-28 03:59:27'),
(12, 11, 'User Edit', 'user.edit', '', '2019-02-28 03:52:42', '2019-02-28 04:00:00'),
(13, 11, 'User Delete', 'user.delete', '', '2019-02-28 03:57:14', '2019-02-28 04:00:10'),
(14, 12, 'Post add', 'post.add', '', '2019-02-28 03:57:42', '2019-02-28 04:00:15'),
(15, 12, 'Post Edit', 'post.edit', '', '2019-02-28 03:58:09', '2019-02-28 04:00:21'),
(16, 13, 'Category Add', 'category.add', '', '2019-02-28 03:58:40', '2019-02-28 04:00:26'),
(17, 12, 'Post Delete', 'post.delete', '', '2019-02-28 04:04:24', '2019-02-28 04:04:24'),
(18, 14, 'Role Action', 'role.access', '', '2019-02-28 04:20:23', '2019-03-01 09:12:13'),
(19, 5, 'Permission Action', 'permission.access', '', '2019-02-28 04:20:47', '2019-03-01 09:12:00'),
(20, 15, 'Action Action', 'action.access', '', '2019-02-28 04:21:02', '2019-03-01 09:11:48'),
(21, 13, 'Category Delete', 'category.delete', '', '2019-02-28 04:25:43', '2019-02-28 04:25:43'),
(22, 13, 'Category Edit', 'category.edit', '', '2019-02-28 04:26:08', '2019-02-28 04:26:08'),
(23, 18, 'Notification Access', 'notification.access', '', '2019-03-01 06:58:35', '2019-03-01 06:58:35'),
(24, 11, 'User Access', 'user.access', '', '2019-03-01 07:06:38', '2019-03-01 07:06:38'),
(25, 11, 'User View', 'user.view', '', '2019-03-01 09:07:54', '2019-03-01 09:07:54'),
(26, 13, 'Category Access', 'category.access', '', '2019-03-01 09:13:19', '2019-03-01 09:13:19'),
(27, 12, 'Post Access', 'post.access', '', '2019-03-01 09:14:55', '2019-03-01 09:14:55');

-- --------------------------------------------------------

--
-- Table structure for table `attachmentable`
--

CREATE TABLE `attachmentable` (
  `id` int(11) NOT NULL,
  `attachmentable_type` varchar(500) NOT NULL,
  `attachmentable_id` int(11) NOT NULL,
  `attachment_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `attachments`
--

CREATE TABLE `attachments` (
  `id` int(11) UNSIGNED NOT NULL,
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
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `attachments`
--

INSERT INTO `attachments` (`id`, `user_id`, `name`, `original_name`, `mime`, `extension`, `size`, `sort`, `path`, `description`, `alt`, `hash`, `disk`, `group`, `created_at`, `updated_at`, `deleted_at`) VALUES
(31, 8, NULL, 'print.png', 'image/png', NULL, '262059', NULL, 'storage/2019/09/16/', NULL, NULL, NULL, 'local', NULL, '2019-09-16 03:43:39', '2019-09-16 03:43:39', NULL),
(32, 8, NULL, 'variable.png', 'image/png', 'png', '440753', NULL, 'storage/2019/09/16/', NULL, NULL, NULL, 'local', NULL, '2019-09-16 03:45:33', '2019-09-16 03:45:33', NULL),
(33, 8, '1cb143c316dd463da11ac195ad862f4d', 'me.jpg', 'image/jpeg', 'jpg', '129709', NULL, 'storage/2019/09/16/', NULL, NULL, NULL, 'local', NULL, '2019-09-16 03:49:54', '2019-09-16 03:49:54', NULL),
(34, 8, '808a8dab59fe418dbac17945859cf968', 'me.png', 'image/png', 'png', '476399', NULL, 'storage/2019/09/16/', NULL, NULL, NULL, 'local', NULL, '2019-09-16 03:51:07', '2019-09-16 03:51:07', NULL),
(35, 8, '869e2b8ac7d94517a2c61dd0b589bf3e', 'me.jpg', 'image/jpeg', 'jpg', '129709', NULL, 'storage/2019/09/16/', NULL, NULL, NULL, 'local', NULL, '2019-09-16 12:28:22', '2019-09-16 12:28:22', NULL),
(36, 8, '46c5e2e5290344c28bb8e25e1d4e3af3', 'me.jpg', 'image/jpeg', 'jpg', '129709', NULL, 'storage/2019/09/16/', NULL, NULL, NULL, 'local', NULL, '2019-09-16 12:38:53', '2019-09-16 12:38:53', NULL),
(37, 8, '0eeaf101eeb64f298d27a29d74666d98', 'variable.png', 'image/png', 'png', '440753', NULL, 'storage/2019/09/16/', NULL, NULL, NULL, 'local', NULL, '2019-09-16 12:39:18', '2019-09-16 12:39:18', NULL),
(38, 8, 'a6227e7297da41b5b2827ecd1c388968', 'me.jpg', 'image/jpeg', 'jpg', '129709', NULL, 'storage/2019/09/16/', NULL, NULL, NULL, 'local', NULL, '2019-09-16 12:45:24', '2019-09-16 12:45:24', NULL),
(39, 8, '99c59ea178ca46dabc8c72b26bebd2fb', 'me.jpg', 'image/jpeg', 'jpg', '129709', NULL, 'storage/2019/09/16/', NULL, NULL, NULL, 'local', NULL, '2019-09-16 12:55:46', '2019-09-16 12:55:46', NULL),
(40, 8, '337d6e6f58fa473f8d4d7066ea5f8e17', 'group_2.png', 'image/png', 'png', '131434', NULL, 'storage/2019/09/21/', NULL, NULL, NULL, 'local', NULL, '2019-09-21 09:30:14', '2019-09-21 09:30:14', NULL),
(41, 8, '56b7adb1c89c42f2bb9ad2f6f1fcd1bb', 'Thinking-of-getting-a-cat.png', 'image/png', 'png', '1246129', NULL, 'storage/2019/12/22/', NULL, NULL, NULL, 'local', NULL, '2019-12-22 03:30:41', '2019-12-22 03:30:41', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `auth_history`
--

CREATE TABLE `auth_history` (
  `id` int(10) UNSIGNED NOT NULL,
  `user_id` int(11) NOT NULL,
  `os` varchar(100) DEFAULT NULL,
  `platform` varchar(100) DEFAULT NULL,
  `platform_version` varchar(100) DEFAULT NULL,
  `browser` varchar(100) DEFAULT NULL,
  `browser_version` varchar(10) DEFAULT NULL,
  `ip_address` varchar(100) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `id` int(10) UNSIGNED NOT NULL,
  `type` varchar(500) NOT NULL,
  `title` varchar(500) NOT NULL,
  `slug` varchar(500) DEFAULT NULL,
  `sort` int(11) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `options` json DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`id`, `type`, `title`, `slug`, `sort`, `description`, `options`, `created_at`, `updated_at`) VALUES
(1, 'blog', 'daily contents', 'test', NULL, '', NULL, '2019-03-12 07:10:37', '2019-03-12 09:18:02'),
(2, 'blog', 'test', 'test', NULL, '', NULL, '2019-03-12 07:15:39', '2019-03-12 09:17:48');

-- --------------------------------------------------------

--
-- Table structure for table `category_posts`
--

CREATE TABLE `category_posts` (
  `category_id` int(11) NOT NULL,
  `post_id` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `category_posts`
--

INSERT INTO `category_posts` (`category_id`, `post_id`) VALUES
(1, '10'),
(1, '4'),
(1, '7'),
(1, '8'),
(2, '10'),
(2, '4'),
(2, '6'),
(2, '8');

-- --------------------------------------------------------

--
-- Table structure for table `content_field`
--

CREATE TABLE `content_field` (
  `id` int(10) UNSIGNED NOT NULL,
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
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `content_field`
--

INSERT INTO `content_field` (`id`, `content_type_id`, `field_type`, `title`, `place`, `name`, `show_in_table`, `sort`, `dataattr`, `default_value`, `is_required`, `regex`, `created_at`, `updated_at`) VALUES
(2, 1, 'input', 'Description', 'main', 'content.description', 1, 1, '', NULL, 0, '', '2019-03-03 02:29:44', '2019-03-20 01:44:59'),
(3, 1, 'input', 'Password', 'side', 'content.password', 0, 4, '', NULL, 0, '', '2019-03-03 02:30:51', '2019-03-20 01:45:48'),
(4, 1, 'datetime', 'Publish at', 'side', 'content.publish_at', 0, 3, '{\"enable-time\": \"true\",\r\n\"time_24hr\": \"true\",\r\n\"allow-input\": \"true\",\r\n\"date-format\":\"Y-m-d h:i:s\"}', NULL, 0, '', '2019-03-05 02:37:59', '2019-03-20 01:45:06'),
(5, 1, 'tinymce', 'Content', 'main', 'content.content', 0, 2, '{\"theme\": \"modern\"}', NULL, 0, 'required|min:10|max:5000', '2019-03-05 02:38:25', '2019-03-20 01:48:56'),
(7, 1, 'input', 'cover', 'side', 'content.cover', 0, 6, '', NULL, 0, '', '2019-03-06 05:19:34', '2019-03-20 01:45:40'),
(8, 2, 'input', 'Title', 'main', 'content.title', 0, 0, '', NULL, 0, '', '2019-03-06 12:32:18', '2019-03-20 03:10:20'),
(9, 3, 'input', 'Title', 'main', 'content.title', 0, 0, NULL, NULL, 0, '0', '2019-03-06 12:33:01', '2019-03-19 10:41:54'),
(10, 1, 'input', 'Title', 'main', 'content.title', 1, 0, '', NULL, 1, 'required', '2019-03-11 11:34:59', '2019-03-20 03:16:07'),
(11, 1, 'category', 'Category', 'side', 'category', 0, 7, '', NULL, 0, '', '2019-03-12 05:27:03', '2019-03-20 01:45:21'),
(12, 1, 'tag', 'Tag', 'side', 'tag', 0, 8, '', NULL, 0, '', '2019-03-12 05:27:33', '2019-03-20 01:45:14'),
(13, 2, 'category', 'Category', 'side', 'content.category', 0, 0, '', NULL, 0, '', '2019-03-12 07:33:58', '2019-03-20 03:10:31'),
(14, 1, 'upload', 'Files', 'side', 'files', 0, 5, '{\"name\": \"files\"}', NULL, 0, '', '2019-03-14 03:24:53', '2019-09-16 11:02:32'),
(15, 2, 'input', 'Keywords', 'main', 'Keyword', 0, 0, '', NULL, 0, '', '2019-03-20 03:10:11', '2019-03-20 03:10:11'),
(16, 3, 'tinymce', 'Content', 'main', 'content.content', 0, 0, '', NULL, 0, '', '2019-09-15 08:55:14', '2019-09-15 08:56:45');

-- --------------------------------------------------------

--
-- Table structure for table `content_type`
--

CREATE TABLE `content_type` (
  `id` int(10) UNSIGNED NOT NULL,
  `title` varchar(500) DEFAULT NULL,
  `slug` varchar(100) DEFAULT NULL,
  `description` varchar(1000) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `content_type`
--

INSERT INTO `content_type` (`id`, `title`, `slug`, `description`, `created_at`, `updated_at`) VALUES
(1, 'Blog', 'blog', 'Blog posts', '2019-03-02 03:43:50', '2019-03-10 02:38:16'),
(2, 'News', 'news', 'Latest News', '2019-03-02 03:46:25', '2019-03-18 13:07:51'),
(3, 'Pages', 'pages', 'test', '2019-03-02 03:46:39', '2019-03-18 13:20:09');

-- --------------------------------------------------------

--
-- Table structure for table `password_resets`
--

CREATE TABLE `password_resets` (
  `email` int(11) NOT NULL,
  `token` varchar(60) NOT NULL,
  `created_at` varchar(60) NOT NULL,
  `expire_at` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `permissions`
--

CREATE TABLE `permissions` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(500) NOT NULL,
  `slug` varchar(100) NOT NULL,
  `description` varchar(500) DEFAULT NULL,
  `sort` int(11) DEFAULT '0',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `permissions`
--

INSERT INTO `permissions` (`id`, `name`, `slug`, `description`, `sort`, `created_at`, `updated_at`) VALUES
(5, 'Permission', 'permission', '', 6, '2019-02-25 05:10:55', '2019-02-28 04:19:15'),
(11, 'Users', 'user', '', 2, '2019-02-28 03:06:08', '2019-02-28 04:17:31'),
(12, 'Posts', 'post', '', 3, '2019-02-28 03:06:16', '2019-02-28 04:17:40'),
(13, 'Category', 'category', '', 4, '2019-02-28 03:06:26', '2019-02-28 04:17:52'),
(14, 'Role', 'role', '', 5, '2019-02-28 03:06:36', '2019-02-28 04:19:08'),
(15, 'Actions', 'action', '', 7, '2019-02-28 03:07:02', '2019-02-28 04:19:21'),
(17, 'Dashboard', 'dashboard', 'test', 1, '2019-02-28 04:14:24', '2019-03-18 13:37:17'),
(18, 'Notification', 'notification', '', 1, '2019-03-01 06:58:02', '2019-03-01 06:58:14');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `id` int(11) UNSIGNED NOT NULL,
  `user_id` int(11) NOT NULL,
  `type` varchar(45) NOT NULL,
  `slug` varchar(500) DEFAULT NULL,
  `content` json DEFAULT NULL,
  `click` int(11) DEFAULT '0',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`id`, `user_id`, `type`, `slug`, `content`, `click`, `created_at`, `updated_at`, `deleted_at`) VALUES
(5, 8, 'blog', NULL, '{\"cover\": \"cover\", \"title\": \"test title\", \"content\": \"content\", \"password\": \"test passport\", \"publish_at\": \"2019-03-21 12:00:0\", \"description\": \"description\"}', 0, '2019-03-12 06:12:40', '2019-06-05 01:50:07', NULL),
(6, 8, 'blog', NULL, '{\"cover\": \"latest content\", \"title\": \"xxxxxxxx\", \"content\": \"<p>fds</p>\", \"password\": \"latest content\", \"publish_at\": \"2019-03-21 3:00:0\", \"description\": \"test desc\"}', 0, '2019-03-12 06:26:37', '2019-06-05 01:49:40', NULL),
(9, 8, 'blog', NULL, '{\"cover\": \"\", \"title\": \"dsgsdf\", \"content\": \"<p>gfds</p>\", \"password\": \"\", \"publish_at\": \"\", \"description\": \"gf\"}', 0, '2019-06-05 02:15:41', '2019-06-06 12:09:04', NULL),
(10, 8, 'blog', NULL, '{\"cover\": \"\", \"title\": \"سىناق يازما\", \"content\": \"<p>سىناق يازما</p>\", \"password\": \"\", \"publish_at\": \"\", \"description\": \"سىناق يازما\"}', 0, '2019-06-05 02:16:06', '2019-09-15 08:49:30', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `roles`
--

CREATE TABLE `roles` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(500) NOT NULL,
  `slug` varchar(100) NOT NULL,
  `description` varchar(500) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `roles`
--

INSERT INTO `roles` (`id`, `name`, `slug`, `description`, `created_at`, `updated_at`) VALUES
(2, 'Manager', 'manager', '', '2019-02-25 05:30:15', '2019-02-28 05:36:04'),
(3, 'Writer', 'writer', 'Writer', '2019-02-25 05:30:32', '2019-02-25 05:30:32'),
(4, 'supervisiour', 'supervisiour', '', '2019-02-27 03:42:44', '2019-02-28 05:21:50');

-- --------------------------------------------------------

--
-- Table structure for table `role_action`
--

CREATE TABLE `role_action` (
  `role_id` int(11) NOT NULL,
  `action_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `role_action`
--

INSERT INTO `role_action` (`role_id`, `action_id`) VALUES
(2, 1),
(2, 3),
(2, 23),
(2, 12),
(2, 13),
(2, 24),
(2, 25),
(2, 14),
(2, 15),
(2, 17),
(2, 27),
(2, 16),
(2, 21),
(2, 22),
(2, 26),
(2, 18),
(2, 19),
(2, 20),
(4, 1),
(4, 3),
(4, 23);

-- --------------------------------------------------------

--
-- Table structure for table `taggable`
--

CREATE TABLE `taggable` (
  `post_id` int(11) NOT NULL,
  `tag_id` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `taggable`
--

INSERT INTO `taggable` (`post_id`, `tag_id`) VALUES
(6, '10'),
(6, '8'),
(8, '5'),
(9, '16'),
(9, '5'),
(9, '8'),
(10, '5');

-- --------------------------------------------------------

--
-- Table structure for table `tags`
--

CREATE TABLE `tags` (
  `id` int(10) UNSIGNED NOT NULL,
  `slug` varchar(500) DEFAULT NULL,
  `name` varchar(500) DEFAULT NULL,
  `count` int(11) DEFAULT '0',
  `type` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `tags`
--

INSERT INTO `tags` (`id`, `slug`, `name`, `count`, `type`) VALUES
(5, 'test', 'test', 24, NULL),
(6, 'aaa', 'aaa', 4, NULL),
(8, 'nur', 'Nur', 13, NULL),
(10, 'algha', 'algha', 7, NULL),
(16, 'asa', 'asa', 3, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `account` varchar(30) DEFAULT NULL,
  `password` varchar(60) NOT NULL,
  `picture` varchar(500) DEFAULT NULL,
  `access_token` varchar(100) DEFAULT NULL,
  `locale` varchar(2) DEFAULT 'en',
  `status` tinyint(1) DEFAULT NULL,
  `is_online` tinyint(1) DEFAULT '0',
  `email_verified_at` timestamp NULL DEFAULT NULL,
  `last_login` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NOT NULL,
  `updated_at` timestamp NOT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `is_admin` smallint(6) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `account`, `password`, `picture`, `access_token`, `locale`, `status`, `is_online`, `email_verified_at`, `last_login`, `created_at`, `updated_at`, `deleted_at`, `is_admin`) VALUES
(8, 'Tarim Uyghur', 'tarim@test.com', 'tarim', '$2b$12$fSo58b6aEqGTzDD3FR8G1O2Awpj2wds8MIz2wBlmS3GMGb.rm5RP2', '', 'xx', 'en', 1, 0, NULL, NULL, '2019-01-23 10:47:24', '2019-12-22 03:58:13', NULL, 1),
(23, 'test@gmail.com', 'test@gmail.com', 'test@gmail.com', '$2b$12$uKYAnUMvPX0rFW4clVfpRenUMHoCKauvaIP3JzSgzSm6W1eIA7LN2', NULL, NULL, 'en', NULL, 0, NULL, NULL, '2019-03-01 13:59:31', '2019-03-01 13:59:31', NULL, 0);

-- --------------------------------------------------------

--
-- Table structure for table `user_device`
--

CREATE TABLE `user_device` (
  `id` int(11) UNSIGNED NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `os` varchar(60) DEFAULT NULL,
  `model` varchar(60) DEFAULT NULL,
  `version` varchar(60) DEFAULT NULL,
  `token` varchar(200) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user_profile`
--

CREATE TABLE `user_profile` (
  `id` int(10) UNSIGNED NOT NULL,
  `user_id` int(11) NOT NULL,
  `avatar` varchar(200) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `status` varchar(500) DEFAULT NULL,
  `is_online` tinyint(1) DEFAULT '0',
  `be_notified` tinyint(1) DEFAULT '0',
  `last_seen_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user_role`
--

CREATE TABLE `user_role` (
  `user_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `user_role`
--

INSERT INTO `user_role` (`user_id`, `role_id`) VALUES
(17, 1),
(18, 2),
(19, 2),
(22, 1),
(22, 2),
(22, 3),
(9, 4),
(23, 4);

-- --------------------------------------------------------

--
-- Table structure for table `user_verification`
--

CREATE TABLE `user_verification` (
  `id` int(10) UNSIGNED NOT NULL,
  `user_id` int(11) NOT NULL,
  `verify_token` varchar(60) DEFAULT NULL,
  `expire_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `actions`
--
ALTER TABLE `actions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug_UNIQUE` (`slug`);

--
-- Indexes for table `attachmentable`
--
ALTER TABLE `attachmentable`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `attachments`
--
ALTER TABLE `attachments`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `auth_history`
--
ALTER TABLE `auth_history`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `category_posts`
--
ALTER TABLE `category_posts`
  ADD PRIMARY KEY (`category_id`,`post_id`);

--
-- Indexes for table `content_field`
--
ALTER TABLE `content_field`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `content_type`
--
ALTER TABLE `content_type`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `password_resets`
--
ALTER TABLE `password_resets`
  ADD UNIQUE KEY `email_UNIQUE` (`email`);

--
-- Indexes for table `permissions`
--
ALTER TABLE `permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug_UNIQUE` (`slug`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug_UNIQUE` (`slug`);

--
-- Indexes for table `taggable`
--
ALTER TABLE `taggable`
  ADD PRIMARY KEY (`post_id`,`tag_id`);

--
-- Indexes for table `tags`
--
ALTER TABLE `tags`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_device`
--
ALTER TABLE `user_device`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_profile`
--
ALTER TABLE `user_profile`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_verification`
--
ALTER TABLE `user_verification`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `actions`
--
ALTER TABLE `actions`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `attachments`
--
ALTER TABLE `attachments`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT for table `auth_history`
--
ALTER TABLE `auth_history`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `content_field`
--
ALTER TABLE `content_field`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `content_type`
--
ALTER TABLE `content_type`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `permissions`
--
ALTER TABLE `permissions`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `tags`
--
ALTER TABLE `tags`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `user_device`
--
ALTER TABLE `user_device`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_profile`
--
ALTER TABLE `user_profile`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_verification`
--
ALTER TABLE `user_verification`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
