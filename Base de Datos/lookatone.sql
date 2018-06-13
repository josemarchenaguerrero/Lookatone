-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 08-06-2018 a las 21:42:19
-- Versión del servidor: 10.1.26-MariaDB
-- Versión de PHP: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `lookatone`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add perfiles', 7, 'add_perfiles'),
(20, 'Can change perfiles', 7, 'change_perfiles'),
(21, 'Can delete perfiles', 7, 'delete_perfiles'),
(22, 'Can add alarmcontrol', 8, 'add_alarmcontrol'),
(23, 'Can change alarmcontrol', 8, 'change_alarmcontrol'),
(24, 'Can delete alarmcontrol', 8, 'delete_alarmcontrol'),
(25, 'Can add association', 9, 'add_association'),
(26, 'Can change association', 9, 'change_association'),
(27, 'Can delete association', 9, 'delete_association'),
(28, 'Can add code', 10, 'add_code'),
(29, 'Can change code', 10, 'change_code'),
(30, 'Can delete code', 10, 'delete_code'),
(31, 'Can add nonce', 11, 'add_nonce'),
(32, 'Can change nonce', 11, 'change_nonce'),
(33, 'Can delete nonce', 11, 'delete_nonce'),
(34, 'Can add user social auth', 12, 'add_usersocialauth'),
(35, 'Can change user social auth', 12, 'change_usersocialauth'),
(36, 'Can delete user social auth', 12, 'delete_usersocialauth'),
(37, 'Can add partial', 13, 'add_partial'),
(38, 'Can change partial', 13, 'change_partial'),
(39, 'Can delete partial', 13, 'delete_partial');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(9, 'social_django', 'association'),
(10, 'social_django', 'code'),
(11, 'social_django', 'nonce'),
(13, 'social_django', 'partial'),
(12, 'social_django', 'usersocialauth'),
(8, 'Twitter', 'alarmcontrol'),
(7, 'Twitter', 'perfiles');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2018-06-08 19:38:46.878067'),
(2, 'auth', '0001_initial', '2018-06-08 19:38:55.425528'),
(3, 'Twitter', '0001_initial', '2018-06-08 19:38:57.801612'),
(4, 'Twitter', '0002_auto_20180402_1102', '2018-06-08 19:38:58.612436'),
(5, 'Twitter', '0003_perfiles', '2018-06-08 19:38:59.408767'),
(6, 'Twitter', '0004_alarmcontrol', '2018-06-08 19:38:59.589629'),
(7, 'Twitter', '0005_auto_20180607_1935', '2018-06-08 19:39:00.427740'),
(8, 'admin', '0001_initial', '2018-06-08 19:39:02.453553'),
(9, 'admin', '0002_logentry_remove_auto_add', '2018-06-08 19:39:02.494511'),
(10, 'contenttypes', '0002_remove_content_type_name', '2018-06-08 19:39:03.598532'),
(11, 'auth', '0002_alter_permission_name_max_length', '2018-06-08 19:39:04.524602'),
(12, 'auth', '0003_alter_user_email_max_length', '2018-06-08 19:39:05.355474'),
(13, 'auth', '0004_alter_user_username_opts', '2018-06-08 19:39:05.394242'),
(14, 'auth', '0005_alter_user_last_login_null', '2018-06-08 19:39:05.964434'),
(15, 'auth', '0006_require_contenttypes_0002', '2018-06-08 19:39:06.095011'),
(16, 'auth', '0007_alter_validators_add_error_messages', '2018-06-08 19:39:06.138082'),
(17, 'auth', '0008_alter_user_username_max_length', '2018-06-08 19:39:07.027175'),
(18, 'auth', '0009_alter_user_last_name_max_length', '2018-06-08 19:39:08.300671'),
(19, 'sessions', '0001_initial', '2018-06-08 19:39:09.154698'),
(20, 'default', '0001_initial', '2018-06-08 19:39:12.493674'),
(21, 'social_auth', '0001_initial', '2018-06-08 19:39:12.552899'),
(22, 'default', '0002_add_related_name', '2018-06-08 19:39:13.367567'),
(23, 'social_auth', '0002_add_related_name', '2018-06-08 19:39:13.404817'),
(24, 'default', '0003_alter_email_max_length', '2018-06-08 19:39:14.098688'),
(25, 'social_auth', '0003_alter_email_max_length', '2018-06-08 19:39:14.136042'),
(26, 'default', '0004_auto_20160423_0400', '2018-06-08 19:39:14.172911'),
(27, 'social_auth', '0004_auto_20160423_0400', '2018-06-08 19:39:14.213431'),
(28, 'social_auth', '0005_auto_20160727_2333', '2018-06-08 19:39:14.458501'),
(29, 'social_django', '0006_partial', '2018-06-08 19:39:15.001588'),
(30, 'social_django', '0007_code_timestamp', '2018-06-08 19:39:15.606306'),
(31, 'social_django', '0008_partial_timestamp', '2018-06-08 19:39:16.341537'),
(32, 'spider_google', '0001_initial', '2018-06-08 19:39:17.019930'),
(33, 'spider_google', '0002_auto_20180502_1436', '2018-06-08 19:39:17.800601'),
(34, 'spider_google', '0003_auto_20180502_1437', '2018-06-08 19:39:19.140674'),
(35, 'spider_google', '0004_auto_20180502_1538', '2018-06-08 19:39:19.181842'),
(36, 'spider_google', '0005_spider_html', '2018-06-08 19:39:19.472993'),
(37, 'spider_google', '0006_auto_20180515_1334', '2018-06-08 19:39:22.391549'),
(38, 'spider_google', '0007_auto_20180515_1500', '2018-06-08 19:39:24.002104'),
(39, 'spider_google', '0008_spider_html_incidencia', '2018-06-08 19:39:25.009520'),
(40, 'spider_google', '0009_auto_20180608_2138', '2018-06-08 19:39:26.253764'),
(41, 'social_django', '0004_auto_20160423_0400', '2018-06-08 19:39:26.310771'),
(42, 'social_django', '0005_auto_20160727_2333', '2018-06-08 19:39:26.337964'),
(43, 'social_django', '0002_add_related_name', '2018-06-08 19:39:26.374019'),
(44, 'social_django', '0001_initial', '2018-06-08 19:39:26.404252'),
(45, 'social_django', '0003_alter_email_max_length', '2018-06-08 19:39:26.440638');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `social_auth_association`
--

CREATE TABLE `social_auth_association` (
  `id` int(11) NOT NULL,
  `server_url` varchar(255) NOT NULL,
  `handle` varchar(255) NOT NULL,
  `secret` varchar(255) NOT NULL,
  `issued` int(11) NOT NULL,
  `lifetime` int(11) NOT NULL,
  `assoc_type` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `social_auth_code`
--

CREATE TABLE `social_auth_code` (
  `id` int(11) NOT NULL,
  `email` varchar(254) NOT NULL,
  `code` varchar(32) NOT NULL,
  `verified` tinyint(1) NOT NULL,
  `timestamp` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `social_auth_nonce`
--

CREATE TABLE `social_auth_nonce` (
  `id` int(11) NOT NULL,
  `server_url` varchar(255) NOT NULL,
  `timestamp` int(11) NOT NULL,
  `salt` varchar(65) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `social_auth_partial`
--

CREATE TABLE `social_auth_partial` (
  `id` int(11) NOT NULL,
  `token` varchar(32) NOT NULL,
  `next_step` smallint(5) UNSIGNED NOT NULL,
  `backend` varchar(32) NOT NULL,
  `data` longtext NOT NULL,
  `timestamp` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `social_auth_usersocialauth`
--

CREATE TABLE `social_auth_usersocialauth` (
  `id` int(11) NOT NULL,
  `provider` varchar(32) NOT NULL,
  `uid` varchar(255) NOT NULL,
  `extra_data` longtext NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `spider_google_idiomas`
--

CREATE TABLE `spider_google_idiomas` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `reduccion` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `spider_google_idiomas`
--

INSERT INTO `spider_google_idiomas` (`id`, `nombre`, `reduccion`) VALUES
(1, 'Arabe', 'ar'),
(2, 'Bulgaro', 'bg'),
(3, 'Catalan', 'ca'),
(4, 'Danes', 'da'),
(5, 'Armenio', 'hy'),
(6, 'Bieloruso', 'be'),
(7, 'Croata', 'hr'),
(8, 'Holandes', 'nl'),
(9, 'Checo', 'cs'),
(10, 'Ingles', 'en'),
(11, 'Esperanto', 'eo'),
(12, 'Estonio', 'et'),
(13, 'Filipino', 'tl'),
(14, 'Finlandes', 'fi'),
(15, 'Frances', 'fr'),
(16, 'Aleman', 'de'),
(17, 'Griego', 'el'),
(18, 'Hebreo', 'iw'),
(19, 'Hungaro', 'hu'),
(20, 'Islandes', 'is'),
(21, 'Indonesio', 'id'),
(22, 'Italiano', 'it'),
(23, 'Japones', 'ja'),
(24, 'Coreano', 'ko'),
(25, 'Leton', 'lv'),
(26, 'Lituano', 'lt'),
(27, 'Persa', 'fa'),
(28, 'Polaco', 'pl'),
(29, 'Portuges', 'pt'),
(30, 'Rumano', 'ro'),
(31, 'Ruso', 'ru'),
(32, 'Serbio', 'sr'),
(33, 'Eslovaco', 'sk'),
(34, 'Esloveno', 'sl'),
(35, 'Español', 'es'),
(36, 'Sueco', 'sv'),
(37, 'Tailandes', 'th'),
(38, 'Turco', 'tr'),
(39, 'Ucraniano', 'uk'),
(40, 'Viednamita', 'vi'),
(41, 'Chino Simplificado', 'zh-CN'),
(42, 'Chino Tradicional', 'zh-TW');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `spider_google_paises`
--

CREATE TABLE `spider_google_paises` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `reduccion` varchar(2) NOT NULL,
  `continente` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `spider_google_paises`
--

INSERT INTO `spider_google_paises` (`id`, `nombre`, `reduccion`, `continente`) VALUES
(1, 'Afganistan', 'AF', 'Asia'),
(2, 'Albania', 'AL', 'Europa'),
(3, 'Argelia', 'DZ', 'Africa'),
(4, 'Saoma Americana', 'AS', 'Oceania'),
(5, 'Andorra', 'AD', 'Europa'),
(6, 'Angola', 'AI', 'Africa'),
(7, 'Antartida', 'AQ', 'Antartida'),
(8, 'Antigua y Barbuda', 'AG', 'America Central'),
(9, 'Argentina', 'AR', 'America Sur'),
(10, 'Armenia', 'M', 'Europa'),
(11, 'Aruba', 'AW', 'America Central'),
(12, 'Australia', 'AU', 'Oceania'),
(13, 'Austria', 'AT', 'Europa'),
(14, 'Azerbaijan', 'AZ', 'Europa'),
(15, 'Bahamas', 'BD', 'America Central'),
(16, 'Bangladesh', 'BH', 'Asia'),
(17, 'Bahamas', 'BS', 'America Central'),
(18, 'Bahrain', 'BH', 'Asia'),
(19, 'Barbados', 'BB', 'America Central'),
(20, 'Belize', 'BZ', 'America Central'),
(21, 'Belgica', 'BE', 'Europa'),
(22, 'Bielorusia', 'BY', 'Europa'),
(23, 'Benin', 'BJ', 'Africa'),
(24, 'Bermudas', 'BM', 'America Central'),
(25, 'Bhutan', 'BT', 'Asia'),
(26, 'Bolivia', 'BO', 'America Sur'),
(27, 'Bosnia y Herzegovia', 'BA', 'Europa'),
(28, 'Botswana', 'BW', 'Africa'),
(29, 'Brasil', 'BR', 'America Sur'),
(30, 'Territorio Britanio en el Oceano Indico', 'IO', 'Asia'),
(31, 'Brunei Darussalam', 'BN', 'Asia'),
(32, 'Bulgaria', 'BG', 'Europa'),
(33, 'Burkina Faso', 'BF', 'Africa'),
(34, 'Burundi', 'BI', 'Africa'),
(35, 'Cambodia', 'KH', 'Asia'),
(36, 'Cameroon', 'CM', 'Africa'),
(37, 'Canada', 'CA', 'America Norte'),
(38, 'Cabo Verde', 'CV', 'Africa'),
(39, 'Islas Caiman', 'KY', 'America Central'),
(40, 'Republica Centro Africana', 'CF', 'Africa'),
(41, 'Chad', 'TD', 'Africa'),
(42, 'Chile', 'CL', 'America Sur'),
(43, 'China', 'CN', 'Asia'),
(44, 'Isla de Navidad', 'CX', 'Asia'),
(45, 'Islas de Cocos', 'CC', 'Asia'),
(46, 'Colombia', 'CO', 'America Sur'),
(47, 'COmoros', 'KM', 'Africa'),
(48, 'Congo', 'CG', 'Africa'),
(49, 'Republica Democratica del Congo', 'CD', 'Africa'),
(50, 'Islas Cook', 'CK', 'Oceania'),
(51, 'Costa Rica', 'CR', 'America Central'),
(52, 'Costa de Marfil', 'CI', 'Africa'),
(53, 'Croacia', 'HR', 'Europa'),
(54, 'Chipre', 'CY', 'Europa'),
(55, 'Republica Checa', 'CZ', 'Europa'),
(56, 'Dinamarca', 'DK', 'Europa'),
(57, 'Djibouti', 'DJ', 'Africa'),
(58, 'Republica Dominicana', 'DO', 'America Central'),
(59, 'Dominica', 'DM', 'America Central'),
(60, 'Timor Oriental', 'TL', 'Asia'),
(61, 'Ecuador', 'EC', 'America Sur'),
(62, 'Egipto', 'EG', 'Africa'),
(63, 'El Salvador', 'SV', 'America Sur'),
(64, 'Guinea Ecuatorial', 'GQ', 'Africa'),
(65, 'Estonia', 'EE', 'Europa'),
(66, 'Erinea', 'ER', 'Africa'),
(67, 'Etiopia', 'ET', 'Africa'),
(68, 'Islas Malvinas', 'FK', 'America Sur'),
(69, 'Islas Faroe', 'FO', 'Europa'),
(70, 'Fiji', 'FJ', 'Oceania'),
(71, 'Finlandia', 'FI', 'Europa'),
(72, 'Francia', 'FR', 'Europa'),
(73, 'Guinea Francesa', 'GF', 'America Sur'),
(74, 'Polinesia Francesa', 'PF', 'Oceania'),
(75, 'Territorios Australes Franceses', 'TF', 'Africa'),
(76, 'Gabon', 'GA', 'Africa'),
(77, 'Gambia', 'GM', 'Africa'),
(78, 'Georgia', 'GE', 'Europa'),
(79, 'Alemania', 'DE', 'Europa'),
(80, 'Ghana', 'GH', 'Africa'),
(81, 'Gibraltar', 'GI', 'Europa'),
(82, 'Gracia', 'GR', 'Europa'),
(83, 'Groenlandia', 'GL', 'America Norte'),
(84, 'Guadalupe', 'GP', 'America Central'),
(85, 'Guam', 'GU', 'Oceania'),
(86, 'Guatemala', 'GT', 'America Central'),
(87, 'Guinea', 'GN', 'Africa'),
(88, 'Guinea Bissau', 'GW', 'Africa'),
(89, 'Guyana', 'GY', 'Africa'),
(90, 'Haiti', 'HT', 'America Central'),
(91, 'Heard e Islas McDonald', 'HM', 'America Sur'),
(92, 'Sabana Occidental', 'EH', 'Africa'),
(93, 'Granada', 'CD', 'America Central'),
(94, 'Hong Kong', 'HK', 'Asia'),
(95, 'Honduras', 'HN', 'America Central'),
(96, 'Hungria', 'HU', 'Europa'),
(97, 'Islandia', 'IS', 'Europa'),
(98, 'India', 'IN', 'Asia'),
(99, 'Indonesia', 'ID', 'Europa'),
(100, 'Iraq', 'IQ', 'Asia'),
(101, 'Irlanda', 'IE', 'Europa'),
(102, 'Israel', 'IL', 'Asia'),
(103, 'Italia', 'IT', 'Europa'),
(104, 'Jamaica', 'JM', 'America Central'),
(105, 'Japon', 'JP', 'Asia'),
(106, 'Jodan', 'JO', 'Asia'),
(107, 'Kazakhstan', 'KZ', 'Asia'),
(108, 'Kenia', 'KE', 'Africa'),
(109, 'Kiribati', 'KI', 'Africa'),
(110, 'Kuwait', 'KW', 'Asia'),
(111, 'Kyrgyzstan', 'KG', 'Asia'),
(112, 'Republica Democratica Popular de Lao', 'LA', 'Asia'),
(113, 'Letonia', 'LV', 'Europa'),
(114, 'Libao', 'LS', 'Asia'),
(115, 'Lesato', 'LS', 'Africa'),
(116, 'Liberia', 'LR', 'Africa'),
(117, 'Libia', 'LY', 'Africa'),
(118, 'Liechteinstein', 'LI', 'Europa'),
(119, 'Lituania', 'LT', 'Europa'),
(120, 'Luxemburgo', 'LU', 'Europa'),
(121, 'Macau', 'MO', 'Asia'),
(122, 'Macedonia', 'MK', 'Europa'),
(123, 'Madagascar', 'MG', 'Africa'),
(124, 'Malawi', 'MW', 'Asia'),
(125, 'Malasia', 'MY', 'Asia'),
(126, 'Mali', 'ML', 'Africa'),
(127, 'Malta', 'MT', 'Europa'),
(128, 'Islas Marshall', 'MH', 'Oceania'),
(129, 'Martinica', 'MQ', 'America Central'),
(130, 'Mauritania', 'MR', 'Africa'),
(131, 'Mauricio', 'MU', 'Oceania'),
(132, 'Mayote', 'YT', 'Africa'),
(133, 'Mejico', 'MX', 'America Central'),
(134, 'Micronesia', 'FM', 'Oceania'),
(135, 'Maldova', 'MD', 'Europa'),
(136, 'Mongolia', 'MN', 'Asia'),
(137, 'Montserrat', 'MS', 'Europa'),
(138, 'Maruecos', 'MA', 'Africa'),
(139, 'Mozambique', 'MZ', 'Africa'),
(140, 'Nimibia', 'NA', 'Africa'),
(141, 'Nauru', 'NR', 'Oceania'),
(142, 'Nepal', 'NP', 'Asia'),
(143, 'Paises Bajos', 'NL', 'Europa'),
(144, 'Antilas Holandesas', 'AN', 'Oceania'),
(145, 'Nueva Caledonia', 'NC', 'Oceania'),
(146, 'Nueva Zelanda', 'NZ', 'Oceania'),
(147, 'Nicaragua', 'NI', 'America Central'),
(148, 'Niger', 'NE', 'Africa'),
(149, 'Niue', 'NU', 'Oceania'),
(150, 'Islas Nortfolk', 'NF', 'Oceania'),
(151, 'Northern Maria', 'MP', 'Oceania'),
(152, 'Noruega', 'NO', 'Europa'),
(153, 'Oan', 'OM', 'Asia'),
(154, 'Pakistan', 'PK', 'Asia'),
(155, 'Territorio Palestino', 'PS', 'Asia'),
(156, 'Palau', 'PW', 'Asia'),
(157, 'Panama', 'PA', 'America Central'),
(158, 'Filipinas', 'PH', 'Oceania'),
(159, 'Papua Nueva Guinea', 'PG', 'Oceania'),
(160, 'Paraguay', 'PY', 'America Sur'),
(161, 'Peru', 'PE', 'America Sur'),
(162, 'Pitcairn', 'PN', 'Europa'),
(163, 'Polonia', 'PL', 'Europa'),
(164, 'Portugal', 'PT', 'Europa'),
(165, 'Puerto Rico', 'PR', 'America Central'),
(166, 'Qatar', 'QA', 'Asia'),
(167, 'Reunion', 'RE', 'Africa'),
(168, 'Rumania', 'RO', 'Europa'),
(169, 'Rusia', 'RU', 'Europa'),
(170, 'Rwanda', 'RW', 'Africa'),
(171, 'Santa Kitts y Nevis', 'KN', 'America Central'),
(172, 'Santa Lucia', 'LC', 'America Central'),
(173, 'San Vicente y las Granadinas', 'VC', 'America Central'),
(174, 'Samoa', 'WS', 'Oceania'),
(175, 'San Marino', 'SM', 'Europa'),
(176, 'Santo Tome y Principe', 'ST', 'Africa'),
(177, 'Arabia Saudi', 'SA', 'Africa'),
(178, 'Senegal', 'SN', 'Africa'),
(179, 'Serbia y Montenegro', 'CS', 'Europa'),
(180, 'Seychelles', 'SC', 'Africa'),
(181, 'Sierra Leona', 'SL', 'Africa'),
(182, 'Singapour', 'SG', 'Asia'),
(183, 'Eslovaquia', 'SK', 'Europa'),
(184, 'Eslovenia', 'SI', 'Europa'),
(185, 'Islas Salomon', 'SB', 'Europa'),
(186, 'Somalia', 'SO', 'Africa'),
(187, 'Sur Africa', 'ZA', 'Africa'),
(188, 'Sur Georgia y El las Islas Sandwich del Sur', 'GS', 'America Sur'),
(189, 'Corea el Sur', 'KR', 'Asia'),
(190, 'España', 'ES', 'Europa'),
(191, 'Sri Lanka', 'LK', 'Asia'),
(192, 'Santa Helena', 'SH', 'Africa'),
(193, 'San Pierre y Mequelon', 'PM', 'America Norte'),
(194, 'Suriname', 'SJ', 'America Sur'),
(195, 'Svalbard y Islas Jan Meyen', 'SJ', 'Europa'),
(196, 'Suecia', 'SE', 'Europa'),
(197, 'Swaziland', 'SZ', 'Africa'),
(198, 'Suiza', 'CH', 'Europa'),
(199, 'Taiwan', 'TW', 'Asia'),
(200, 'Tajikistan', 'TJ', 'Asia'),
(201, 'Tanzania', 'TZ', 'Africa'),
(202, 'Tailandia', 'TH', 'Asia'),
(203, 'Togo', 'TG', 'Africa'),
(204, 'Takelon', 'TK', 'Oceania'),
(205, 'Trinidad y Tobago', 'TT', 'America Central'),
(206, 'Tunez', 'TN', 'Africa'),
(207, 'Turquia', 'TR', 'Asia'),
(208, 'Turkmenistan', 'TM', 'Asia'),
(209, 'Islas Turcas y Caicos', 'TC', 'America Norte'),
(210, 'Tuvalu', 'TV', 'Oceania'),
(211, 'Uganda', 'UG', 'Africa'),
(212, 'Ucrania', 'UA', 'Europa'),
(213, 'Estados Unidos Arabes', 'AE', 'Asia'),
(214, 'Reino Unido', 'GB', 'Europa'),
(215, 'Islas menores alejadas de Estados Unidos', 'UM', 'America Norte'),
(216, 'Uruguay', 'UY', 'America Sur'),
(217, 'Uzbekistan', 'UZ', 'Asia'),
(218, 'Vanautu', 'VU', 'Oceania'),
(219, 'Vaticano', 'VA', 'Europa'),
(220, 'Venezuela', 'VE', 'America Sur'),
(221, 'Viet Nam', 'VN', 'Asia'),
(222, 'Islas Virgenes (Inglesas)', 'VG', 'America Central'),
(223, 'Islas Virgenes (US)', 'VI', 'America Central'),
(224, 'Islas Wallis y Futuna', 'WF', 'Oceania'),
(225, 'Yenen', 'YE', 'Asia'),
(226, 'Zambia', 'ZM', 'Africa'),
(227, 'Zimbabwe', 'ZW', 'Africa'),
(228, 'Estados Unidos', 'US', 'America Norte');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `spider_google_spider_html`
--

CREATE TABLE `spider_google_spider_html` (
  `id` int(11) NOT NULL,
  `filtro` varchar(200) CHARACTER SET latin1 NOT NULL,
  `subfiltro` varchar(200) CHARACTER SET latin1 NOT NULL,
  `titulo` varchar(200) CHARACTER SET latin1 NOT NULL,
  `url` varchar(200) CHARACTER SET latin1 NOT NULL,
  `fecha` varchar(10) CHARACTER SET latin1 NOT NULL,
  `hora` varchar(5) CHARACTER SET latin1 NOT NULL,
  `html` varchar(100) CHARACTER SET latin1 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `spider_google_spider_html_incidencia`
--

CREATE TABLE `spider_google_spider_html_incidencia` (
  `id` int(11) NOT NULL,
  `incidencia` longtext CHARACTER SET latin1 NOT NULL,
  `spider_html_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `twitter_alarmcontrol`
--

CREATE TABLE `twitter_alarmcontrol` (
  `id` int(11) NOT NULL,
  `fecha` varchar(50) NOT NULL,
  `texto` varchar(256) NOT NULL,
  `usuario` varchar(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `twitter_perfiles`
--

CREATE TABLE `twitter_perfiles` (
  `id` int(11) NOT NULL,
  `id_twitter` varchar(256) NOT NULL,
  `consumer_key` varchar(256) NOT NULL,
  `consumer_secret` varchar(256) NOT NULL,
  `access_token` varchar(256) NOT NULL,
  `access_token_secret` varchar(256) NOT NULL,
  `usuario_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `social_auth_association`
--
ALTER TABLE `social_auth_association`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `social_auth_association_server_url_handle_078befa2_uniq` (`server_url`,`handle`);

--
-- Indices de la tabla `social_auth_code`
--
ALTER TABLE `social_auth_code`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `social_auth_code_email_code_801b2d02_uniq` (`email`,`code`),
  ADD KEY `social_auth_code_code_a2393167` (`code`),
  ADD KEY `social_auth_code_timestamp_176b341f` (`timestamp`);

--
-- Indices de la tabla `social_auth_nonce`
--
ALTER TABLE `social_auth_nonce`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `social_auth_nonce_server_url_timestamp_salt_f6284463_uniq` (`server_url`,`timestamp`,`salt`);

--
-- Indices de la tabla `social_auth_partial`
--
ALTER TABLE `social_auth_partial`
  ADD PRIMARY KEY (`id`),
  ADD KEY `social_auth_partial_token_3017fea3` (`token`),
  ADD KEY `social_auth_partial_timestamp_50f2119f` (`timestamp`);

--
-- Indices de la tabla `social_auth_usersocialauth`
--
ALTER TABLE `social_auth_usersocialauth`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `social_auth_usersocialauth_provider_uid_e6b5e668_uniq` (`provider`,`uid`),
  ADD KEY `social_auth_usersocialauth_user_id_17d28448_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `spider_google_idiomas`
--
ALTER TABLE `spider_google_idiomas`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `spider_google_paises`
--
ALTER TABLE `spider_google_paises`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `spider_google_spider_html`
--
ALTER TABLE `spider_google_spider_html`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `spider_google_spider_html_incidencia`
--
ALTER TABLE `spider_google_spider_html_incidencia`
  ADD PRIMARY KEY (`id`),
  ADD KEY `spider_google_spider_spider_html_id_c6c1792c_fk_spider_go` (`spider_html_id`);

--
-- Indices de la tabla `twitter_alarmcontrol`
--
ALTER TABLE `twitter_alarmcontrol`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `twitter_perfiles`
--
ALTER TABLE `twitter_perfiles`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `usuario_id` (`usuario_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT de la tabla `social_auth_association`
--
ALTER TABLE `social_auth_association`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `social_auth_code`
--
ALTER TABLE `social_auth_code`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `social_auth_nonce`
--
ALTER TABLE `social_auth_nonce`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `social_auth_partial`
--
ALTER TABLE `social_auth_partial`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `social_auth_usersocialauth`
--
ALTER TABLE `social_auth_usersocialauth`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `spider_google_idiomas`
--
ALTER TABLE `spider_google_idiomas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT de la tabla `spider_google_paises`
--
ALTER TABLE `spider_google_paises`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=229;

--
-- AUTO_INCREMENT de la tabla `spider_google_spider_html`
--
ALTER TABLE `spider_google_spider_html`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT de la tabla `spider_google_spider_html_incidencia`
--
ALTER TABLE `spider_google_spider_html_incidencia`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `twitter_alarmcontrol`
--
ALTER TABLE `twitter_alarmcontrol`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `twitter_perfiles`
--
ALTER TABLE `twitter_perfiles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `social_auth_usersocialauth`
--
ALTER TABLE `social_auth_usersocialauth`
  ADD CONSTRAINT `social_auth_usersocialauth_user_id_17d28448_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `spider_google_spider_html_incidencia`
--
ALTER TABLE `spider_google_spider_html_incidencia`
  ADD CONSTRAINT `spider_google_spider_spider_html_id_c6c1792c_fk_spider_go` FOREIGN KEY (`spider_html_id`) REFERENCES `spider_google_spider_html` (`id`);

--
-- Filtros para la tabla `twitter_perfiles`
--
ALTER TABLE `twitter_perfiles`
  ADD CONSTRAINT `Twitter_perfiles_usuario_id_8be7b3c3_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
