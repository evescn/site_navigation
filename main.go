package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"site_navigation/db"
)

func main() {
	fmt.Println(gin.Version)

	// 初始化数据库
	db.Init()
}
