/*
 Navicat Premium Data Transfer

 Source Server         : project_test
 Source Server Type    : MySQL
 Source Server Version : 50022
 Source Host           : localhost:3306
 Source Schema         : light_blog

 Target Server Type    : MySQL
 Target Server Version : 50022
 File Encoding         : 65001

 Date: 10/08/2018 09:28:15
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version`  (
  `version_num` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '',
  PRIMARY KEY USING BTREE (`version_num`)
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
INSERT INTO `alembic_version` VALUES ('075a1b4493d4');

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `text` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `date` datetime NULL DEFAULT NULL,
  `post_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY USING BTREE (`id`),
  INDEX `post_id` USING BTREE(`post_id`),
  CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`post_id`) REFERENCES `post` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = 'InnoDB free: 3072 kB; (`post_id`) REFER `light_blog/post`(`id`)' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of comment
-- ----------------------------
INSERT INTO `comment` VALUES (1, '不知道', '不知道', '2018-08-08 15:43:36', 9);
INSERT INTO `comment` VALUES (2, '不知道', '不知道', '2018-08-08 15:44:03', 9);
INSERT INTO `comment` VALUES (3, '不知道', '不知道', '2018-08-08 15:48:33', 101);
INSERT INTO `comment` VALUES (4, '不知道', '不知道', '2018-08-08 15:49:45', 101);
INSERT INTO `comment` VALUES (5, '不知道', '不知道', '2018-08-08 15:49:50', 101);
INSERT INTO `comment` VALUES (6, 'dss', 'dss', '2018-08-08 15:50:11', 101);
INSERT INTO `comment` VALUES (7, 'dss', 'dss', '2018-08-08 15:50:21', 101);
INSERT INTO `comment` VALUES (8, 'zz', 'zz', '2018-08-08 15:51:05', 10);
INSERT INTO `comment` VALUES (9, 'zz', 'zz', '2018-08-08 15:51:36', 10);
INSERT INTO `comment` VALUES (10, 'zz', 'zz', '2018-08-08 15:51:41', 10);
INSERT INTO `comment` VALUES (11, 'zz', 'zz', '2018-08-08 15:51:45', 10);

-- ----------------------------
-- Table structure for post
-- ----------------------------
DROP TABLE IF EXISTS `post`;
CREATE TABLE `post`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `text` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `publish_date` datetime NULL DEFAULT NULL,
  `user_id` int(11) NULL DEFAULT NULL,
  `is_delete` tinyint(1) NULL DEFAULT NULL,
  PRIMARY KEY USING BTREE (`id`),
  INDEX `user_id` USING BTREE(`user_id`),
  CONSTRAINT `post_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 105 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = 'InnoDB free: 3072 kB; (`user_id`) REFER `light_blog/user`(`id`)' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of post
-- ----------------------------
INSERT INTO `post` VALUES (1, 'Post0', 'EXAMPLE TEXT的发送到发送到发送到发送到发送到发斯蒂芬dsfasdfasdf阿斯蒂芬多多多多多多多多多多多多多多多多多多多多多的点点滴滴多多多多多多多多多多多多多的点点滴滴多多多多多多多多多多多', '2018-08-06 14:03:34', 2, 1);
INSERT INTO `post` VALUES (2, 'Post1', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 2, 1);
INSERT INTO `post` VALUES (3, 'Post2', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 2, 1);
INSERT INTO `post` VALUES (4, 'Post3', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 2, 1);
INSERT INTO `post` VALUES (5, 'Post4', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 2, 0);
INSERT INTO `post` VALUES (6, 'Post5', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 2, 0);
INSERT INTO `post` VALUES (7, 'Post6', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (8, 'Post7', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (9, 'Post8', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 2, 0);
INSERT INTO `post` VALUES (10, 'Post9', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 1);
INSERT INTO `post` VALUES (11, 'Post10', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (12, 'Post11', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (13, 'Post12', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (14, 'Post13', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (15, 'Post14', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (16, 'Post15', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (17, 'Post16', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (18, 'Post17', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (19, 'Post18', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (20, 'Post19', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (21, 'Post20', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (22, 'Post21', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (23, 'Post22', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (24, 'Post23', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (25, 'Post24', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (26, 'Post25', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (27, 'Post26', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (28, 'Post27', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (29, 'Post28', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (30, 'Post29', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (31, 'Post30', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (32, 'Post31', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (33, 'Post32', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (34, 'Post33', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (35, 'Post34', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (36, 'Post35', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (37, 'Post36', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (38, 'Post37', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (39, 'Post38', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (40, 'Post39', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (41, 'Post40', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (42, 'Post41', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (43, 'Post42', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (44, 'Post43', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (45, 'Post44', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (46, 'Post45', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (47, 'Post46', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (48, 'Post47', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (49, 'Post48', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (50, 'Post49', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (51, 'Post50', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (52, 'Post51', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (53, 'Post52', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (54, 'Post53', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (55, 'Post54', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (56, 'Post55', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (57, 'Post56', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (58, 'Post57', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (59, 'Post58', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (60, 'Post59', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (61, 'Post60', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (62, 'Post61', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (63, 'Post62', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (64, 'Post63', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (65, 'Post64', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (66, 'Post65', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (67, 'Post66', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (68, 'Post67', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (69, 'Post68', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (70, 'Post69', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (71, 'Post70', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (72, 'Post71', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (73, 'Post72', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (74, 'Post73', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (75, 'Post74', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (76, 'Post75', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 2, 1);
INSERT INTO `post` VALUES (77, 'Post76', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 2, 0);
INSERT INTO `post` VALUES (78, 'Post77', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (79, 'Post78', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 2, 0);
INSERT INTO `post` VALUES (80, 'Post79', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (81, 'Post80', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (82, 'Post81', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (83, 'Post82', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (84, 'Post83', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 2, 0);
INSERT INTO `post` VALUES (85, 'Post84', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 2, 0);
INSERT INTO `post` VALUES (86, 'Post85', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 2, 0);
INSERT INTO `post` VALUES (87, 'Post86', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (88, 'Post87', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 2, 0);
INSERT INTO `post` VALUES (89, 'Post88', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (90, 'Post89', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (91, 'Post90', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (92, 'Post91', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (93, 'Post92', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 1);
INSERT INTO `post` VALUES (94, 'Post93', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 1);
INSERT INTO `post` VALUES (95, 'Post94', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (96, 'Post95', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (97, 'Post96', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (98, 'Post97', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (99, 'Post98', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (100, 'Post99', 'EXAMPLE TEXT', '2018-08-06 14:03:34', 1, 0);
INSERT INTO `post` VALUES (101, '手动阀', '<p>打发手动阀手动阀手动阀手动阀</p>\r\n', '2018-08-06 17:30:56', 2, 1);
INSERT INTO `post` VALUES (102, '看看有没有user_id', '<p>测试一下user_id能不能被动态添加</p>\r\n', '2018-08-07 11:27:37', 2, 0);
INSERT INTO `post` VALUES (103, '观察文章样式', '<p><strong>看看编辑器</strong>的效果对<em>文字</em>有没有用</p>\r\n', '2018-08-08 09:43:27', 2, 1);
INSERT INTO `post` VALUES (104, 'zzzzz', '<p>zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz</p>\r\n', '2018-08-08 10:29:15', 2, 1);

-- ----------------------------
-- Table structure for post_tag
-- ----------------------------
DROP TABLE IF EXISTS `post_tag`;
CREATE TABLE `post_tag`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `post_id` int(11) NULL DEFAULT NULL,
  `tag_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY USING BTREE (`id`),
  INDEX `post_id` USING BTREE(`post_id`),
  INDEX `tag_id` USING BTREE(`tag_id`),
  CONSTRAINT `post_tag_ibfk_1` FOREIGN KEY (`post_id`) REFERENCES `post` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `post_tag_ibfk_2` FOREIGN KEY (`tag_id`) REFERENCES `tag` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 199 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = 'InnoDB free: 3072 kB; (`post_id`) REFER `light_blog/post`(`id`); (`tag_id`) REFE' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of post_tag
-- ----------------------------
INSERT INTO `post_tag` VALUES (1, 77, 1);
INSERT INTO `post_tag` VALUES (2, 77, 2);
INSERT INTO `post_tag` VALUES (3, 77, 3);
INSERT INTO `post_tag` VALUES (4, 76, 3);
INSERT INTO `post_tag` VALUES (5, 76, 4);
INSERT INTO `post_tag` VALUES (6, 78, 1);
INSERT INTO `post_tag` VALUES (7, 78, 4);
INSERT INTO `post_tag` VALUES (8, 80, 2);
INSERT INTO `post_tag` VALUES (9, 80, 1);
INSERT INTO `post_tag` VALUES (10, 80, 4);
INSERT INTO `post_tag` VALUES (11, 79, 3);
INSERT INTO `post_tag` VALUES (12, 81, 4);
INSERT INTO `post_tag` VALUES (13, 81, 1);
INSERT INTO `post_tag` VALUES (14, 81, 2);
INSERT INTO `post_tag` VALUES (15, 82, 1);
INSERT INTO `post_tag` VALUES (16, 83, 4);
INSERT INTO `post_tag` VALUES (17, 83, 1);
INSERT INTO `post_tag` VALUES (18, 85, 1);
INSERT INTO `post_tag` VALUES (19, 85, 3);
INSERT INTO `post_tag` VALUES (20, 85, 2);
INSERT INTO `post_tag` VALUES (21, 1, 4);
INSERT INTO `post_tag` VALUES (22, 1, 3);
INSERT INTO `post_tag` VALUES (23, 1, 2);
INSERT INTO `post_tag` VALUES (24, 84, 3);
INSERT INTO `post_tag` VALUES (25, 6, 2);
INSERT INTO `post_tag` VALUES (26, 86, 3);
INSERT INTO `post_tag` VALUES (27, 86, 2);
INSERT INTO `post_tag` VALUES (28, 86, 1);
INSERT INTO `post_tag` VALUES (29, 87, 4);
INSERT INTO `post_tag` VALUES (30, 88, 2);
INSERT INTO `post_tag` VALUES (31, 89, 3);
INSERT INTO `post_tag` VALUES (32, 89, 4);
INSERT INTO `post_tag` VALUES (33, 91, 3);
INSERT INTO `post_tag` VALUES (34, 91, 4);
INSERT INTO `post_tag` VALUES (35, 90, 1);
INSERT INTO `post_tag` VALUES (36, 93, 3);
INSERT INTO `post_tag` VALUES (37, 27, 2);
INSERT INTO `post_tag` VALUES (38, 27, 1);
INSERT INTO `post_tag` VALUES (39, 27, 3);
INSERT INTO `post_tag` VALUES (40, 92, 3);
INSERT INTO `post_tag` VALUES (41, 92, 1);
INSERT INTO `post_tag` VALUES (42, 92, 2);
INSERT INTO `post_tag` VALUES (43, 2, 2);
INSERT INTO `post_tag` VALUES (44, 94, 1);
INSERT INTO `post_tag` VALUES (45, 94, 3);
INSERT INTO `post_tag` VALUES (46, 94, 2);
INSERT INTO `post_tag` VALUES (47, 95, 2);
INSERT INTO `post_tag` VALUES (48, 95, 3);
INSERT INTO `post_tag` VALUES (49, 97, 4);
INSERT INTO `post_tag` VALUES (50, 97, 3);
INSERT INTO `post_tag` VALUES (51, 97, 1);
INSERT INTO `post_tag` VALUES (52, 8, 2);
INSERT INTO `post_tag` VALUES (53, 8, 1);
INSERT INTO `post_tag` VALUES (54, 96, 3);
INSERT INTO `post_tag` VALUES (55, 96, 4);
INSERT INTO `post_tag` VALUES (56, 96, 2);
INSERT INTO `post_tag` VALUES (57, 7, 4);
INSERT INTO `post_tag` VALUES (58, 7, 2);
INSERT INTO `post_tag` VALUES (59, 3, 1);
INSERT INTO `post_tag` VALUES (60, 98, 4);
INSERT INTO `post_tag` VALUES (61, 98, 2);
INSERT INTO `post_tag` VALUES (62, 99, 4);
INSERT INTO `post_tag` VALUES (63, 99, 3);
INSERT INTO `post_tag` VALUES (64, 28, 2);
INSERT INTO `post_tag` VALUES (65, 53, 1);
INSERT INTO `post_tag` VALUES (66, 53, 4);
INSERT INTO `post_tag` VALUES (67, 52, 4);
INSERT INTO `post_tag` VALUES (68, 52, 3);
INSERT INTO `post_tag` VALUES (69, 100, 4);
INSERT INTO `post_tag` VALUES (70, 100, 1);
INSERT INTO `post_tag` VALUES (71, 29, 4);
INSERT INTO `post_tag` VALUES (72, 29, 2);
INSERT INTO `post_tag` VALUES (73, 31, 1);
INSERT INTO `post_tag` VALUES (74, 54, 2);
INSERT INTO `post_tag` VALUES (75, 54, 3);
INSERT INTO `post_tag` VALUES (76, 54, 4);
INSERT INTO `post_tag` VALUES (77, 30, 3);
INSERT INTO `post_tag` VALUES (78, 4, 2);
INSERT INTO `post_tag` VALUES (79, 4, 1);
INSERT INTO `post_tag` VALUES (80, 4, 4);
INSERT INTO `post_tag` VALUES (81, 10, 4);
INSERT INTO `post_tag` VALUES (82, 55, 4);
INSERT INTO `post_tag` VALUES (83, 55, 1);
INSERT INTO `post_tag` VALUES (84, 55, 2);
INSERT INTO `post_tag` VALUES (85, 56, 3);
INSERT INTO `post_tag` VALUES (86, 5, 3);
INSERT INTO `post_tag` VALUES (87, 5, 1);
INSERT INTO `post_tag` VALUES (88, 32, 3);
INSERT INTO `post_tag` VALUES (89, 32, 2);
INSERT INTO `post_tag` VALUES (90, 32, 1);
INSERT INTO `post_tag` VALUES (91, 57, 4);
INSERT INTO `post_tag` VALUES (92, 33, 1);
INSERT INTO `post_tag` VALUES (93, 33, 4);
INSERT INTO `post_tag` VALUES (94, 33, 3);
INSERT INTO `post_tag` VALUES (95, 34, 4);
INSERT INTO `post_tag` VALUES (96, 58, 3);
INSERT INTO `post_tag` VALUES (97, 58, 2);
INSERT INTO `post_tag` VALUES (98, 60, 3);
INSERT INTO `post_tag` VALUES (99, 60, 1);
INSERT INTO `post_tag` VALUES (100, 60, 2);
INSERT INTO `post_tag` VALUES (101, 35, 2);
INSERT INTO `post_tag` VALUES (102, 59, 4);
INSERT INTO `post_tag` VALUES (103, 59, 2);
INSERT INTO `post_tag` VALUES (104, 11, 1);
INSERT INTO `post_tag` VALUES (105, 11, 2);
INSERT INTO `post_tag` VALUES (106, 11, 3);
INSERT INTO `post_tag` VALUES (107, 12, 4);
INSERT INTO `post_tag` VALUES (108, 12, 2);
INSERT INTO `post_tag` VALUES (109, 12, 1);
INSERT INTO `post_tag` VALUES (110, 36, 2);
INSERT INTO `post_tag` VALUES (111, 36, 4);
INSERT INTO `post_tag` VALUES (112, 38, 3);
INSERT INTO `post_tag` VALUES (113, 61, 1);
INSERT INTO `post_tag` VALUES (114, 61, 2);
INSERT INTO `post_tag` VALUES (115, 13, 3);
INSERT INTO `post_tag` VALUES (116, 13, 4);
INSERT INTO `post_tag` VALUES (117, 13, 1);
INSERT INTO `post_tag` VALUES (118, 37, 3);
INSERT INTO `post_tag` VALUES (119, 37, 4);
INSERT INTO `post_tag` VALUES (120, 37, 2);
INSERT INTO `post_tag` VALUES (121, 63, 1);
INSERT INTO `post_tag` VALUES (122, 14, 1);
INSERT INTO `post_tag` VALUES (123, 14, 2);
INSERT INTO `post_tag` VALUES (124, 62, 2);
INSERT INTO `post_tag` VALUES (125, 62, 3);
INSERT INTO `post_tag` VALUES (126, 62, 1);
INSERT INTO `post_tag` VALUES (127, 9, 2);
INSERT INTO `post_tag` VALUES (128, 16, 2);
INSERT INTO `post_tag` VALUES (129, 16, 3);
INSERT INTO `post_tag` VALUES (130, 16, 4);
INSERT INTO `post_tag` VALUES (131, 39, 2);
INSERT INTO `post_tag` VALUES (132, 15, 3);
INSERT INTO `post_tag` VALUES (133, 15, 1);
INSERT INTO `post_tag` VALUES (134, 15, 4);
INSERT INTO `post_tag` VALUES (135, 40, 1);
INSERT INTO `post_tag` VALUES (136, 40, 3);
INSERT INTO `post_tag` VALUES (137, 64, 3);
INSERT INTO `post_tag` VALUES (138, 42, 2);
INSERT INTO `post_tag` VALUES (139, 41, 1);
INSERT INTO `post_tag` VALUES (140, 17, 4);
INSERT INTO `post_tag` VALUES (141, 65, 4);
INSERT INTO `post_tag` VALUES (142, 66, 1);
INSERT INTO `post_tag` VALUES (143, 18, 4);
INSERT INTO `post_tag` VALUES (144, 43, 1);
INSERT INTO `post_tag` VALUES (145, 43, 3);
INSERT INTO `post_tag` VALUES (146, 19, 1);
INSERT INTO `post_tag` VALUES (147, 67, 2);
INSERT INTO `post_tag` VALUES (148, 67, 4);
INSERT INTO `post_tag` VALUES (149, 45, 3);
INSERT INTO `post_tag` VALUES (150, 45, 1);
INSERT INTO `post_tag` VALUES (151, 45, 4);
INSERT INTO `post_tag` VALUES (152, 69, 3);
INSERT INTO `post_tag` VALUES (153, 69, 4);
INSERT INTO `post_tag` VALUES (154, 69, 2);
INSERT INTO `post_tag` VALUES (155, 20, 1);
INSERT INTO `post_tag` VALUES (156, 44, 2);
INSERT INTO `post_tag` VALUES (157, 68, 4);
INSERT INTO `post_tag` VALUES (158, 21, 1);
INSERT INTO `post_tag` VALUES (159, 21, 4);
INSERT INTO `post_tag` VALUES (160, 21, 3);
INSERT INTO `post_tag` VALUES (161, 22, 4);
INSERT INTO `post_tag` VALUES (162, 22, 1);
INSERT INTO `post_tag` VALUES (163, 22, 2);
INSERT INTO `post_tag` VALUES (164, 46, 2);
INSERT INTO `post_tag` VALUES (165, 46, 4);
INSERT INTO `post_tag` VALUES (166, 46, 3);
INSERT INTO `post_tag` VALUES (167, 70, 2);
INSERT INTO `post_tag` VALUES (168, 70, 3);
INSERT INTO `post_tag` VALUES (169, 72, 4);
INSERT INTO `post_tag` VALUES (170, 72, 3);
INSERT INTO `post_tag` VALUES (171, 72, 2);
INSERT INTO `post_tag` VALUES (172, 71, 2);
INSERT INTO `post_tag` VALUES (173, 71, 1);
INSERT INTO `post_tag` VALUES (174, 47, 4);
INSERT INTO `post_tag` VALUES (175, 47, 1);
INSERT INTO `post_tag` VALUES (176, 23, 1);
INSERT INTO `post_tag` VALUES (177, 23, 3);
INSERT INTO `post_tag` VALUES (178, 23, 4);
INSERT INTO `post_tag` VALUES (179, 49, 1);
INSERT INTO `post_tag` VALUES (180, 49, 4);
INSERT INTO `post_tag` VALUES (181, 24, 2);
INSERT INTO `post_tag` VALUES (182, 24, 3);
INSERT INTO `post_tag` VALUES (183, 48, 3);
INSERT INTO `post_tag` VALUES (184, 48, 2);
INSERT INTO `post_tag` VALUES (185, 26, 1);
INSERT INTO `post_tag` VALUES (186, 73, 4);
INSERT INTO `post_tag` VALUES (187, 73, 1);
INSERT INTO `post_tag` VALUES (188, 73, 3);
INSERT INTO `post_tag` VALUES (189, 25, 3);
INSERT INTO `post_tag` VALUES (190, 25, 1);
INSERT INTO `post_tag` VALUES (191, 50, 4);
INSERT INTO `post_tag` VALUES (192, 74, 3);
INSERT INTO `post_tag` VALUES (193, 74, 4);
INSERT INTO `post_tag` VALUES (194, 74, 2);
INSERT INTO `post_tag` VALUES (195, 75, 4);
INSERT INTO `post_tag` VALUES (196, 75, 3);
INSERT INTO `post_tag` VALUES (197, 51, 3);
INSERT INTO `post_tag` VALUES (198, 51, 1);

-- ----------------------------
-- Table structure for reminder
-- ----------------------------
DROP TABLE IF EXISTS `reminder`;
CREATE TABLE `reminder`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime NULL DEFAULT NULL,
  `email` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `text` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  PRIMARY KEY USING BTREE (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of reminder
-- ----------------------------
INSERT INTO `reminder` VALUES (3, '2018-08-09 17:56:52', '2428986312@qq.com', '终于等到您！欢迎来到博客的全新世界!');
INSERT INTO `reminder` VALUES (4, '2018-08-09 18:01:57', '2428986312@qq.com', '终于等到您！欢迎来到博客的全新世界!');
INSERT INTO `reminder` VALUES (5, '2018-08-09 18:01:57', '1126531273@qq.com', '终于等到您！欢迎来到博客的全新世界!');
INSERT INTO `reminder` VALUES (6, '2018-08-09 18:19:24', '1126531273@qq.com', '终于等到您！欢迎来到博客的全新世界!');
INSERT INTO `reminder` VALUES (7, '2018-08-09 18:19:24', '1126531273@qq.com', '终于等到您！欢迎来到博客的全新世界!');
INSERT INTO `reminder` VALUES (8, '2018-08-09 18:27:29', '1126531273@qq.com', '终于等到您！欢迎来到博客的全新世界!');

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY USING BTREE (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of role
-- ----------------------------
INSERT INTO `role` VALUES (1, 'admin', '');
INSERT INTO `role` VALUES (2, 'default', '');
INSERT INTO `role` VALUES (3, 'poster', '');

-- ----------------------------
-- Table structure for tag
-- ----------------------------
DROP TABLE IF EXISTS `tag`;
CREATE TABLE `tag`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY USING BTREE (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of tag
-- ----------------------------
INSERT INTO `tag` VALUES (1, 'Python');
INSERT INTO `tag` VALUES (2, 'Flask');
INSERT INTO `tag` VALUES (3, 'SQLALchemy');
INSERT INTO `tag` VALUES (4, 'JMilkFan');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY USING BTREE (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, 'chenbo', '$2b$12$4ia4LokT4EVXg6jg3mLbBu9ePsmgCURRBNIYt.vGlLzSPCcKftWhu');
INSERT INTO `user` VALUES (2, 'bobo', '$2b$12$4ia4LokT4EVXg6jg3mLbBu9ePsmgCURRBNIYt.vGlLzSPCcKftWhu');
INSERT INTO `user` VALUES (3, 'z', '$2b$12$4ia4LokT4EVXg6jg3mLbBu9ePsmgCURRBNIYt.vGlLzSPCcKftWhu');
INSERT INTO `user` VALUES (4, 'chenlong', '$2b$12$ka2FxuNy9WtfN0RwLTJiNeBgehPElICSOSzl/vEmlvS1UHvBBgaEC');
INSERT INTO `user` VALUES (5, 'long', '$2b$12$Oqk3paAeMUx3If6TLRxhruaWTPjbKl6kiW8JWkou5A1AVJwhZv9Su');
INSERT INTO `user` VALUES (6, 'bobobo', '$2b$12$rOx7DLTr3VEkOOYJ9Nv8nOuefMF5CIJFtPQPEcYhX6Nxt5UL7CaR6');
INSERT INTO `user` VALUES (7, 'zhubajie', '$2b$12$imA3z5aCsynQ/d5Eq7ws9e23R594RqytRVIr4v4VVn0aoUF77a1cy');
INSERT INTO `user` VALUES (8, 'zzzzzzzz', '$2b$12$RlgrJX2oWbXRQ5iMP.8.5.rsSf2SprlOucIkhXULAOMvseAu.N95u');
INSERT INTO `user` VALUES (9, 'success', '$2b$12$chtO1XPB4j9M.uVXawcZIOL1etZLIv6jbfYq9W2d79/cE9//5enyW');

-- ----------------------------
-- Table structure for user_role
-- ----------------------------
DROP TABLE IF EXISTS `user_role`;
CREATE TABLE `user_role`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NULL DEFAULT NULL,
  `role_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY USING BTREE (`id`),
  INDEX `role_id` USING BTREE(`role_id`),
  INDEX `user_id` USING BTREE(`user_id`),
  CONSTRAINT `user_role_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `user_role_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = 'InnoDB free: 3072 kB; (`role_id`) REFER `light_blog/role`(`id`); (`user_id`) REF' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of user_role
-- ----------------------------
INSERT INTO `user_role` VALUES (1, 2, 1);
INSERT INTO `user_role` VALUES (2, 2, 2);
INSERT INTO `user_role` VALUES (3, 2, 3);
INSERT INTO `user_role` VALUES (5, 1, 1);
INSERT INTO `user_role` VALUES (6, 3, 2);
INSERT INTO `user_role` VALUES (7, 4, 2);
INSERT INTO `user_role` VALUES (8, 5, 2);
INSERT INTO `user_role` VALUES (9, 6, 2);
INSERT INTO `user_role` VALUES (10, 7, 2);
INSERT INTO `user_role` VALUES (11, 8, 2);
INSERT INTO `user_role` VALUES (12, 9, 2);

SET FOREIGN_KEY_CHECKS = 1;
