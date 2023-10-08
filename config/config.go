package config

import "time"

const (
	WsAddr     = "0.0.0.0:8080"
	ListenAddr = "0.0.0.0:9000"

	//数据库配置
	DbType = "mysql"
	DbHost = "localhost"
	DbPort = 3306
	DbName = "site_navigation"
	DbUser = "root"
	DbPwd  = "123456"
	//打印mysql debug sql日志
	LogMode = false
	//连接池配置
	MaxIdleConns = 10               //最大空闲连接
	MaxOpenConns = 100              //最大连接数
	MaxLifeTime  = 30 * time.Second //最大生存时间

	//账号密码
	AdminUser = "admin"
	AdminPwd  = "123456"
)
