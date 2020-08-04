/*
Navicat MySQL Data Transfer

Source Server         : MySQL
Source Server Version : 50540
Source Host           : localhost:3306
Source Database       : easybuy

Target Server Type    : MYSQL
Target Server Version : 50540
File Encoding         : 65001

Date: 2018-12-03 20:03:38
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for address
-- ----------------------------
DROP TABLE IF EXISTS `address`;
CREATE TABLE `address` (
  `id` int(20) NOT NULL AUTO_INCREMENT COMMENT '主键id',
  `userId` int(255) DEFAULT NULL COMMENT '用户主键',
  `address` varchar(255) DEFAULT NULL COMMENT '地址',
  `createTime` datetime DEFAULT NULL COMMENT '创建时间',
  `isDefault` int(2) DEFAULT '0' COMMENT '是否是默认地址（1:是 0否）',
  `remark` varchar(255) DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of address
-- ----------------------------
INSERT INTO `usercenter_address` VALUES ('11', '2', '北京市海淀区大有庄', null, '0', '朋友家');
INSERT INTO `usercenter_address` VALUES ('12', '2', '北京市海淀区大有庄', null, '0', '女朋友公司');
INSERT INTO `usercenter_address` VALUES ('13', '9', '北京市西直门大桥芬兰国际大厦', null, '0', '女朋友地址');
INSERT INTO `usercenter_address` VALUES ('14', '18', '北京市花园路小区', null, '0', '家里');
INSERT INTO `usercenter_address` VALUES ('15', '18', '北京市海淀区成府路', null, '0', '公司');

-- ----------------------------
-- Table structure for news
-- ----------------------------
DROP TABLE IF EXISTS `news`;
CREATE TABLE `news` (
  `id` int(10) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `title` varchar(40) NOT NULL COMMENT '标题',
  `content` varchar(1000) NOT NULL COMMENT '内容',
  `createTime` varchar(10) NOT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `PK__EASYBUY___C63B5EE724927208` (`id`),
  UNIQUE KEY `UQ__EASYBUY___C12AD09D276EDEB3` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=704 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of news
-- ----------------------------
INSERT INTO `news` VALUES ('531', '会员特惠月开始了', '会员特惠月开始了,亲们赶快下单啊,不到剁手誓不罢休啊,不到离婚誓不清空购物车啊。更多优惠，尽在易买网。', '2010-12-22');
INSERT INTO `news` VALUES ('597', '迎双旦促销大酬宾', '迎双旦促销大酬宾', '2010-12-24');
INSERT INTO `news` VALUES ('649', '加入会员，赢千万大礼包', '加入会员，赢千万大礼包', '2010-12-22');
INSERT INTO `news` VALUES ('650', '新年不夜天，通宵也是开张了', '新年不夜天，通宵也是开张了', '2011-05-22');
INSERT INTO `news` VALUES ('651', '积分兑换开始了', '积分兑换开始了', '2010-12-22');
INSERT INTO `news` VALUES ('653', '团购阿迪1折起', '团购阿迪1折起', '2010-12-22');
INSERT INTO `news` VALUES ('664', '最新酷睿笔记本', 'IBME系列全场促销中，最新酷睿双核处理器，保证CPU更高效的运转。', '2013-08-05');
INSERT INTO `news` VALUES ('675', 'aa', '012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789', '2013-08-14');
INSERT INTO `news` VALUES ('676', 'ResultR', 'ResultResultResultResultResu', '2016-03-28');
INSERT INTO `news` VALUES ('677', '会员特惠月开始了1', '会员特惠月开始了', '2010-12-22');
INSERT INTO `news` VALUES ('678', '迎双旦促销大酬宾2', '迎双旦促销大酬宾', '2010-12-24');
INSERT INTO `news` VALUES ('679', '加入会员，赢千万大礼包3', '加入会员，赢千万大礼包', '2010-12-22');
INSERT INTO `news` VALUES ('680', '新年不夜天，通宵也是开张了4', '新年不夜天，通宵也是开张了', '2011-05-22');
INSERT INTO `news` VALUES ('681', '积分兑换开始了5', '积分兑换开始了', '2010-12-22');
INSERT INTO `news` VALUES ('682', '团购阿迪1折起6', '团购阿迪1折起', '2010-12-22');
INSERT INTO `news` VALUES ('683', '最新酷睿笔记本7', 'IBME系列全场促销中，最新酷睿双核处理器，保证CPU更高效的运转。', '2013-08-05');
INSERT INTO `news` VALUES ('684', 'aa8', '012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789', '2013-08-14');
INSERT INTO `news` VALUES ('685', 'ResultR9', 'ResultResultResultResultResu', '2016-03-28');
INSERT INTO `news` VALUES ('686', '会员特惠月开始了11', '会员特惠月开始了', '2010-12-22');
INSERT INTO `news` VALUES ('687', '迎双旦促销大酬宾21', '迎双旦促销大酬宾', '2010-12-24');
INSERT INTO `news` VALUES ('688', '加入会员，赢千万大礼包31', '加入会员，赢千万大礼包', '2010-12-22');
INSERT INTO `news` VALUES ('689', '新年不夜天，通宵也是开张了41', '新年不夜天，通宵也是开张了', '2011-05-22');
INSERT INTO `news` VALUES ('690', '积分兑换开始了51', '积分兑换开始了', '2010-12-22');
INSERT INTO `news` VALUES ('691', '团购阿迪1折起61', '团购阿迪1折起', '2010-12-22');
INSERT INTO `news` VALUES ('692', '最新酷睿笔记本71', 'IBME系列全场促销中，最新酷睿双核处理器，保证CPU更高效的运转。', '2013-08-05');
INSERT INTO `news` VALUES ('693', 'aa81', '012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789', '2013-08-14');
INSERT INTO `news` VALUES ('694', 'ResultR91', 'ResultResultResultResultResu', '2016-03-28');
INSERT INTO `news` VALUES ('695', '会员特惠月开始了111', '会员特惠月开始了', '2010-12-22');
INSERT INTO `news` VALUES ('696', '迎双旦促销大酬宾211', '迎双旦促销大酬宾', '2010-12-24');
INSERT INTO `news` VALUES ('697', '加入会员，赢千万大礼包311', '加入会员，赢千万大礼包', '2010-12-22');
INSERT INTO `news` VALUES ('698', '新年不夜天，通宵也是开张了411', '新年不夜天，通宵也是开张了', '2011-05-22');
INSERT INTO `news` VALUES ('699', '积分兑换开始了511', '积分兑换开始了', '2010-12-22');
INSERT INTO `news` VALUES ('700', '团购阿迪1折起611', '团购阿迪1折起', '2010-12-22');
INSERT INTO `news` VALUES ('701', '最新酷睿笔记本711', 'IBME系列全场促销中，最新酷睿双核处理器，保证CPU更高效的运转。', '2013-08-05');
INSERT INTO `news` VALUES ('702', 'aa811', '012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789', '2013-08-14');
INSERT INTO `news` VALUES ('703', 'ResultR911', 'ResultResultResultResultResu', '2016-03-28');

-- ----------------------------
-- Table structure for order
-- ----------------------------
DROP TABLE IF EXISTS `order`;
CREATE TABLE `order` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `userId` int(255) DEFAULT NULL COMMENT '用户主键',
  `loginName` varchar(255) DEFAULT NULL,
  `userAddress` varchar(255) DEFAULT NULL COMMENT '用户地址',
  `createTime` datetime DEFAULT NULL COMMENT '创建时间',
  `cost` float DEFAULT NULL COMMENT '总消费',
  `serialNumber` varchar(255) DEFAULT NULL COMMENT '订单号',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of order
-- ----------------------------
INSERT INTO `order` VALUES ('1', '18', 'shangzezhong', '北京市花园路小区', '2016-06-02 14:51:46', '1721', '60B7487F47F9434EAA5FD1D9E22CB06C');
INSERT INTO `order` VALUES ('2', '18', 'shangzezhong', '北京市海淀区成府路', '2016-06-02 14:52:49', '8596', '8EF5E1557D55413781658A65FC301B8A');
INSERT INTO `order` VALUES ('3', '2', 'admin', '北京市海淀区大有庄', '2016-06-03 11:41:09', '456', '51718726C1274CC59504AB4E6FD64BA0');

-- ----------------------------
-- Table structure for order_detail
-- ----------------------------
DROP TABLE IF EXISTS `order_detail`;
CREATE TABLE `order_detail` (
  `id` int(10) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `orderId` int(10) NOT NULL COMMENT '订单主键',
  `productId` int(10) NOT NULL COMMENT '商品主键',
  `quantity` int(10) NOT NULL COMMENT '数量',
  `cost` float NOT NULL COMMENT '消费',
  PRIMARY KEY (`id`),
  UNIQUE KEY `PK__EASYBUY___66E1BD8E2F10007B` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of order_detail
-- ----------------------------
INSERT INTO `usercenter_order_detail` VALUES ('1', '1', '733', '5', '760');
INSERT INTO `order_detail` VALUES ('2', '1', '734', '4', '608');
INSERT INTO `order_detail` VALUES ('3', '1', '735', '1', '152');
INSERT INTO `order_detail` VALUES ('4', '1', '738', '1', '45');
INSERT INTO `order_detail` VALUES ('5', '1', '739', '1', '156');
INSERT INTO `order_detail` VALUES ('6', '2', '755', '1', '8596');
INSERT INTO `order_detail` VALUES ('7', '3', '733', '1', '152');
INSERT INTO `order_detail` VALUES ('8', '3', '734', '1', '152');
INSERT INTO `order_detail` VALUES ('9', '3', '735', '1', '152');

-- ----------------------------
-- Table structure for product
-- ----------------------------
DROP TABLE IF EXISTS `product`;
CREATE TABLE `product` (
  `id` int(10) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(20) NOT NULL COMMENT '名称',
  `description` varchar(1024) DEFAULT NULL COMMENT '描述',
  `price` float NOT NULL COMMENT '价格',
  `sold` int(10) DEFAULT 0 '销量',
  `categoryLevel1Id` int(10) DEFAULT NULL COMMENT '分类1',
  `categoryLevel2Id` int(10) DEFAULT NULL COMMENT '分类2',
  `categoryLevel3Id` int(10) DEFAULT NULL COMMENT '分类3',
  `fileName` varchar(200) DEFAULT NULL COMMENT '文件名称',
  `isDelete` int(1) DEFAULT '0' COMMENT '是否删除(1：删除 0：未删除)',
  PRIMARY KEY (`id`),
  UNIQUE KEY `PK__EASYBUY___94F6E55132E0915F` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=771 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of product
-- ----------------------------
INSERT INTO `goods_product` VALUES ('733', '香奈儿', '', '152' '0', '548', '654', '655', 'brand5.jpg', '0');
INSERT INTO `goods_product` VALUES ('734', '洗面奶', '', '152', '0', '548' '654', '655', 'make_4.jpg', '0');
INSERT INTO `goods_product` VALUES ('735', '啫喱水', '', '152', '0', '548', '654', '655', 'make_3.jpg', '0');
INSERT INTO `goods_product` VALUES ('736', '香水5852', '', '152',  '0', '548', '654', '655', 'per_2.jpg', '0');
INSERT INTO `goods_product` VALUES ('737', '香水', '', '152' '0', '548', '654', '655', 'per_3.jpg', '0');
INSERT INTO `goods_product` VALUES ('738', '润肤露', '', '45', '0', '548', '654', '655', 'pro8.jpg', '0');
INSERT INTO `goods_product` VALUES ('739', '洁面装', '', '156' '0', '548', '654', '655', 'make_6.jpg', '0');
INSERT INTO `goods_product` VALUES ('740', '电饭锅', '', '158', '0', '628', '656', '659', 'n_img1.jpg', '0');
INSERT INTO `goods_product` VALUES ('741', '婴儿喂奶装', '', '569', '0', '632', '637', '653', 'baby_b1.jpg', '0');
INSERT INTO `goods_product` VALUES ('742', '坚果套餐', '', '158',  '0', '660', '661', '662', 'n_img2.jpg', '0');
INSERT INTO `goods_product` VALUES ('743', '超甜蜜崭', '', '589',  '0', '660', '661', '663', 'fre_r.jpg', '0');
INSERT INTO `goods_product` VALUES ('744', '华为2566', '', '589',  '0', '670', '671', '672', 'tel_1.jpg', '1');
INSERT INTO `goods_product` VALUES ('745', '荣耀3C', '', '589', '0', '670', '671', '672', 'tel_5.jpg', '0');
INSERT INTO `goods_product` VALUES ('746', '小米手环', '', '963', '0', '670', '674', '675', 'tel_6.jpg', '0');
INSERT INTO `goods_product` VALUES ('747', '华为2265', '', '896',  '0', '670', '671', '673', 'tel_b2.jpg', '0');
INSERT INTO `goods_product` VALUES ('748', '越南坚果', '', '520',  '0', '660', '661', '662', 'food_b1.jpg', '0');
INSERT INTO `goods_product` VALUES ('749', '日本进口马桶', '', '5866', '0', '628', '657', '0', 'home_b1.jpg', '0');
INSERT INTO `goods_product` VALUES ('750', '联想Y系列', '', '569',  '0', '670', '690', '691', 'tel_2.jpg', '0');
INSERT INTO `goods_product` VALUES ('751', '脑白金1号', '', '589',  '0', '676', '677', '680', 'pa_5.jpg', '0');
INSERT INTO `goods_product` VALUES ('752', '莫里斯按', '', '589',  '0', '676', '678', '0', 'food_1.jpg', '0');
INSERT INTO `goods_product` VALUES ('753', '三鹿好奶粉', '', '859', '0', '676', '679', '0', 'milk_8.jpg', '0');
INSERT INTO `goods_product` VALUES ('754', '儿童牛奶', '', '5896', '0', '676', '679', '0', 'hot1.jpg', '0');
INSERT INTO `goods_product` VALUES ('755', '软沙发', '', '8596' '0', '628', '696', '0', 'home_1.jpg', '0');
INSERT INTO `goods_product` VALUES ('756', '收纳盒', '', '5966', '0', '628', '696', '0', 'home_3.jpg', '0');
INSERT INTO `goods_product` VALUES ('757', '洗衣液', '', '58',  '0', '628', '696', '0', 'make_2.jpg', '0');
INSERT INTO `goods_product` VALUES ('758', '红短沙发', '', '596', '0', '628', '696', '0', 'home_r.jpg', '0');
INSERT INTO `goods_product` VALUES ('759', '新西兰奶粉', '', '5896', '0', '676', '679', '0', 'milk_2.jpg', '0');
INSERT INTO `goods_product` VALUES ('760', '婴儿车', '', '11000', '0', '681', '682', '687', 'baby_5.jpg', '0');
INSERT INTO `goods_product` VALUES ('761', '夏款婴儿车', '', '963', '0', '681', '682', '688', 'baby_1.jpg', '0');
INSERT INTO `goods_product` VALUES ('762', '抗压旅行箱', '', '569',  '0', '681', '683', '685', 't2.jpg', '0');
INSERT INTO `goods_product` VALUES ('763', '透明手提箱', '', '8596',  '0', '681', '683', '684', 'baby_3.jpg', '0');
INSERT INTO `goods_product` VALUES ('764', '婴儿果粉', '', '5896',  '0', '660', '661', '662', 'milk_1.jpg', '0');
INSERT INTO `goods_product` VALUES ('765', '椰子粉', '', '5963',  '0', '660', '661', '662', 'milk_3.jpg', '0');
INSERT INTO `goods_product` VALUES ('766', '坚果蛋糕', '', '200', '0', '660', '661', '663', 'milk_5.jpg', '0');
INSERT INTO `goods_product` VALUES ('767', '编制手提箱', '', '5896',  '0', '681', '682', '688', 'baby_3.jpg', '0');
INSERT INTO `goods_product` VALUES ('768', '纸箱', '', '5896', '0', '681', '682', '687', 'pa_6.jpg', '0');
INSERT INTO `goods_product` VALUES ('769', '健胃液', '', '152',  '0', '676', '679', '0', 'tm_big.jpg', '0');
INSERT INTO `goods_product` VALUES ('770', '联想NTC', '', '8596', '0', '670', '671', '672', 'tel_3.jpg', '1');

-- ----------------------------
-- Table structure for goods_category
-- ----------------------------
DROP TABLE IF EXISTS `goods_category`;
CREATE TABLE `goods_category` (
  `id` int(10) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(20) NOT NULL COMMENT '名称',
  `parentId` int(10) NOT NULL COMMENT '父级目录id',
  `type` int(11) DEFAULT NULL COMMENT '级别(1:一级 2：二级 3：三级)',
  `iconClass` varchar(255) DEFAULT NULL COMMENT '图标',
  PRIMARY KEY (`id`),
  UNIQUE KEY `PK__EASYBUY___9EC2A4E236B12243` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=697 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of goods_category
-- ----------------------------
INSERT INTO `goods_category` VALUES ('548', '化妆品', '1', null);
INSERT INTO `goods_category` VALUES ('628', '家用商品', '1', null);
INSERT INTO `goods_category` VALUES ('654', '面部护理', '2', '548');
INSERT INTO `goods_category` VALUES ('655', '少女派', '3', '654');
INSERT INTO `goods_category` VALUES ('656', '餐具', '2', '628');
INSERT INTO `goods_category` VALUES ('657', '卫具', '2', '628');
INSERT INTO `goods_category` VALUES ('658', '叉子', '3', '656');
INSERT INTO `goods_category` VALUES ('659', '锅', '3', '656');
INSERT INTO `goods_category` VALUES ('660', '进口食品,生鲜', '1', null);
INSERT INTO `goods_category` VALUES ('661', '零食/糖果/巧克力', '2', '660');
INSERT INTO `goods_category` VALUES ('662', '坚果', '3', '661');
INSERT INTO `goods_category` VALUES ('663', '蜜饯', '3', '661');
INSERT INTO `goods_category` VALUES ('670', '电子商品', '1', null);
INSERT INTO `goods_category` VALUES ('671', '手机', '2', '670');
INSERT INTO `goods_category` VALUES ('672', '华为手机', '3', '671');
INSERT INTO `goods_category` VALUES ('673', '联想手机', '3', '671');
INSERT INTO `goods_category` VALUES ('674', '手环', '2', '670');
INSERT INTO `goods_category` VALUES ('675', '小米手环', '3', '674');
INSERT INTO `goods_category` VALUES ('676', '保健食品', '1', null);
INSERT INTO `goods_category` VALUES ('677', '老年保健品', '2', '676');
INSERT INTO `goods_category` VALUES ('678', '中年营养品', '2', '676');
INSERT INTO `goods_category` VALUES ('679', '儿童保健品', '2', '676');
INSERT INTO `goods_category` VALUES ('680', '脑白金', '3', '677');
INSERT INTO `goods_category` VALUES ('681', '箱包', '1', null);
INSERT INTO `goods_category` VALUES ('682', '旅行箱', '2', '681');
INSERT INTO `goods_category` VALUES ('683', '手提箱', '2', '681');
INSERT INTO `goods_category` VALUES ('684', '大型', '3', '683');
INSERT INTO `goods_category` VALUES ('685', '小型', '3', '683');
INSERT INTO `goods_category` VALUES ('686', '中型', '3', '683');
INSERT INTO `goods_category` VALUES ('687', '大型', '3', '682');
INSERT INTO `goods_category` VALUES ('688', '中型', '3', '682');
INSERT INTO `goods_category` VALUES ('689', '小型', '3', '682');
INSERT INTO `goods_category` VALUES ('690', '电脑', '2', '670');
INSERT INTO `goods_category` VALUES ('691', '联想电脑', '3', '690');
INSERT INTO `goods_category` VALUES ('692', '刀叉', '3', '656');
INSERT INTO `goods_category` VALUES ('693', '碗筷', '3', '656');
INSERT INTO `goods_category` VALUES ('696', '客厅专用',  '2', '628');

-- ----------------------------
-- Table structure for result
-- ----------------------------
DROP TABLE IF EXISTS `result`;
CREATE TABLE `result` (
  `stuno` char(10) DEFAULT NULL,
  `subjectName` char(10) DEFAULT NULL,
  `score` int(10) DEFAULT NULL,
  `age` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of result
-- ----------------------------
INSERT INTO `result` VALUES ('1', 'java', '80', '11');
INSERT INTO `result` VALUES ('1', 'c', '78', '12');
INSERT INTO `result` VALUES ('2', 'c', '60', '13');
INSERT INTO `result` VALUES ('3', 'java', '75', '14');
INSERT INTO `result` VALUES ('2', 'java', '75', '15');
INSERT INTO `result` VALUES ('4', 'java', '90', '16');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `loginName` varchar(255) NOT NULL COMMENT '登录名',
  `userName` varchar(255) DEFAULT NULL COMMENT '用户名',
  `password` varchar(255) NOT NULL COMMENT '密码',
  `sex` int(2) DEFAULT '1' COMMENT '性别(1:男 0：女)',
  `identityCode` varchar(60) DEFAULT NULL COMMENT '身份证号',
  `email` varchar(80) DEFAULT NULL COMMENT '邮箱',
  `mobile` varchar(11) DEFAULT NULL COMMENT '手机',
  `type` int(2) DEFAULT '0' COMMENT '类型（1：后台 0:前台）',
  PRIMARY KEY (`id`),
  UNIQUE KEY `PK__EASYBUY___C96109CC3A81B327` (`loginName`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('2', 'admin', '系统管理员', 'e10adc3949ba59abbe56e057f20f883e', '1', '130406198302141869', 'hello11@bdqn.com', '13878916381', '1');
INSERT INTO `user` VALUES ('10', 'cgn', '程广宁', 'e10adc3949ba59abbe56e057f20f883e', '1', '140225189987854589', '1044732267@qq.com', '13366055011', '0');
INSERT INTO `user` VALUES ('11', 'hyl', '韩语良', 'e10adc3949ba59abbe56e057f20f883e', '1', '140225198874584539', '1044732267@qq.com', '13366055010', '0');
INSERT INTO `user` VALUES ('12', 'ck', '陈康', 'e10adc3949ba59abbe56e057f20f883e', '1', '140225189987854589', '1044732267@qq.com', '13366055010', '0');
INSERT INTO `user` VALUES ('13', 'kys', '康有沈', 'e10adc3949ba59abbe56e057f20f883e', '1', '1402251985512541525', '1044732267@qq.com', '13366055010', '0');
INSERT INTO `user` VALUES ('14', 'sb', '沈白', 'e10adc3949ba59abbe56e057f20f883e', '1', '140225158987854589', '1044732267@qq.com', '13366055010', '0');
INSERT INTO `user` VALUES ('15', 'lb', '李白', 'e10adc3949ba59abbe56e057f20f883e', '1', '140225189987854589', '10447322658@qq.com', '1336998554', '0');
INSERT INTO `user` VALUES ('16', 'lgw', '李高伟', 'e10adc3949ba59abbe56e057f20f883e', '1', '140225189987854589', '1011322658@qq.com', '1336998554', '0');
INSERT INTO `user` VALUES ('18', 'shangzezhong', '尚泽忠', '4297f44b13955235245b2497399d7a93', '1', '140225198810013745', '1044888844@qq.com', '13366528458', '0');
INSERT INTO `user` VALUES ('19', 'liguangliang', '李光亮', '25f9e794323b453885f5181f1b624d0b', '1', '140225198841547785', '1047777@qq.com', '13366055048', '0');
INSERT INTO `user` VALUES ('20', 'szz', '李光亮', 'e10adc3949ba59abbe56e057f20f883e', '1', '140225198810013748', '1044732267@qq.com', '13366555010', '1');
INSERT INTO `user` VALUES ('21', 'ssr', null, 'e10adc3949ba59abbe56e057f20f883e', '1', null, '1101632@qq.com', '12321321321', '0');
INSERT INTO `user` VALUES ('22', '小悲伤', null, 'e10adc3949ba59abbe56e057f20f883e', '1', null, '11016132@qq.com', '12321321222', '0');
INSERT INTO `user` VALUES ('23', '小可爱', null, 'e10adc3949ba59abbe56e057f20f883e', '1', null, '110216532@qq.com', '123323221', '0');
INSERT INTO `user` VALUES ('24', 'lailai', null, 'e10adc3949ba59abbe56e057f20f883e', '1', null, '110161322@qq.com', '1232121321', '0');
INSERT INTO `user` VALUES ('26', 'xzz', '小渣渣', 'e28f46e271f1ed4ef72056c06f26c91a', '1', null, '110216532@qq.com', '1233232213', '0');
INSERT INTO `user` VALUES ('28', 'laibinshen', 'laibinshen', 'e28f46e271f1ed4ef72056c06f26c91a', '1', null, '112165632@aa.com', '13633333333', '0');
INSERT INTO `user` VALUES ('29', 'xxx', 'xxx', 'f5f89e0355943bb0f3aae6826a3dae6f', '1', null, '1102165632@aa.co', '13633333333', '0');
INSERT INTO `user` VALUES ('34', 'goudan', '天王', 'e10adc3949ba59abbe56e057f20f883e', '1', '4565123231321321', '110216632@aa.com', '1363333333', '1');
