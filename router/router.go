package router

import (
	"github.com/gin-gonic/gin"
	"net/http"
	"site_navigation/controller"
)

var Router router

type router struct{}

func (*router) InitApiRouter(router *gin.Engine) {
	router.GET("/evescnapi", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"code": 90200,
			"msg":  "evescn api success!",
			"data": nil,
		})
	}).
		//登录验证
		POST("/api/login", controller.Login.Auth).
		// 路由，获取权限信息
		GET("/api/permissions", controller.User.List).
		// 用户管理
		GET("/api/user/list", controller.User.List).
		POST("/api/user/add", controller.User.Add).
		PUT("/api/user/update", controller.User.Update).
		PUT("/api/user/updateRole", controller.User.UpdateRole).
		DELETE("/api/user/del", controller.User.Delete).
		// 环境管理
		GET("/api/url/env/list", controller.Env.List).
		POST("/api/url/env/add", controller.Env.Add).
		PUT("/api/url/env/update", controller.Env.Update).
		DELETE("/api/url/env/del", controller.Env.Delete).
		// URL信息管理
		GET("/api/url/svc/list", controller.Service.List).
		POST("/api/url/svc/add", controller.Service.Add).
		PUT("/api/url/svc/update", controller.Service.Update).
		DELETE("/api/url/svc/del", controller.Service.Delete).
		// 权限管理
		GET("/api/role/list", controller.Roles.List).
		GET("/api/role/getAll", controller.Roles.GetAll).
		POST("/api/role/add", controller.Roles.Add).
		PUT("/api/role/update", controller.Roles.Update).
		DELETE("/api/role/del", controller.Roles.Delete).
		// 1级菜单管理
		GET("/api/menu/list", controller.Menu.List).
		POST("/api/menu/add", controller.Menu.Add).
		PUT("/api/menu/update", controller.Menu.Update).
		DELETE("/api/menu/del", controller.Menu.Delete).
		// 2级菜单管理
		GET("/api/submenu/list", controller.SubMenu.List).
		POST("/api/submenu/add", controller.SubMenu.Add).
		PUT("/api/submenu/update", controller.SubMenu.Update).
		DELETE("/api/submenu/del", controller.SubMenu.Delete).
		// 3级菜单管理
		GET("/api/subsubmenu/list", controller.SubSubMenus.List).
		POST("/api/subsubmenu/add", controller.SubSubMenus.Add).
		PUT("/api/subsubmenu/update", controller.SubSubMenus.Update).
		DELETE("/api/subsubmenu/del", controller.SubSubMenus.Delete).
		// 权限菜单关系管理
		GET("/api/roleMenuRelation/getAll", controller.RoleMenuRelation.GetAll).
		GET("/api/roleMenuRelation/getPermissions", controller.RoleMenuRelation.GetPermissions).
		PUT("/api/roleMenuRelation/update", controller.RoleMenuRelation.Update)
}
