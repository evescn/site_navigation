package db

import (
	"fmt"
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/mysql"
	"github.com/wonderivan/logger"
	"site_navigation/config"
)

var (
	isInit bool
	GORM   *gorm.DB
	err    error
)

func Init() {
	// 判断是否初始化
	if isInit {
		return
	}

	//组装数据库连接的数据
	//parseTime是查询结果是否自动解析为时间
	//loc是Mysql的时区设置
	dsn := fmt.Sprintf("%s:%s@tcp(%s:%d)/%s?charset=utf8&parseTime=True&loc=Local",
		config.DbUser,
		config.DbPwd,
		config.DbHost,
		config.DbPort,
		config.DbName)

	GORM, err = gorm.Open(config.DbType, dsn)
	if err != nil {
		logger.Error(err.Error())
	}

	//打印sql语句
	GORM.LogMode(config.LogMode)
	//开启连接池
	GORM.DB().SetMaxIdleConns(config.MaxIdleConns)
	GORM.DB().SetMaxOpenConns(config.MaxOpenConns)
	GORM.DB().SetConnMaxLifetime(config.MaxLifeTime)

	//isInit = true
	//GORM.AutoMigrate(model.Env{}, model.Password{}, model.Service{})
	logger.Info("数据库连接成功")
}

func Close() error {
	logger.Info("关闭数据库连接")
	return GORM.Close()
}
