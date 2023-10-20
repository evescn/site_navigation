package controller

import (
	"github.com/gin-gonic/gin"
	"github.com/wonderivan/logger"
	"net/http"
	"site_navigation/service"
)

var RoleMenuRelation roleMenuRelation

type roleMenuRelation struct{}

// GetAll 返回环境列表
func (*roleMenuRelation) GetAll(c *gin.Context) {

	data, err := service.RoleMenuRelation.GetAll()
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{
			"code": 90500,
			"msg":  err.Error(),
			"data": nil,
		})
		return
	}

	c.JSON(http.StatusOK, gin.H{
		"code": 90200,
		"msg":  "获取环境列表成功",
		"data": data,
	})
}

// Get 返回环境列表
func (*roleMenuRelation) GetPermissions(c *gin.Context) {
	params := new(struct {
		RoleID uint `form:"role_id"`
	})

	// 绑定请求参数
	//绑定参数
	if err := c.Bind(params); err != nil {
		logger.Error("Bind 请求参数失败：" + err.Error())
		c.JSON(http.StatusBadRequest, gin.H{
			"code": 90400,
			"msg":  err.Error(),
			"data": nil,
		})
		return
	}

	data, err := service.RoleMenuRelation.GetPermissions(params.RoleID)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{
			"code": 90500,
			"msg":  err.Error(),
			"data": nil,
		})
		return
	}

	c.JSON(http.StatusOK, gin.H{
		"code": 90200,
		"msg":  "获取环境列表成功",
		"data": data,
	})
}

//// Add 创建环境
//func (*roleMenuRelation) Add(c *gin.Context) {
//	params := new(model.RoleMenuRelation)
//
//	// 绑定请求参数
//	if err := c.ShouldBind(params); err != nil {
//		logger.Error("Bind 请求参数失败：" + err.Error())
//		c.JSON(http.StatusBadRequest, gin.H{
//			"code": 90400,
//			"msg":  err.Error(),
//			"data": nil,
//		})
//		return
//	}
//
//	err := service.RoleMenuRelation.Add(params)
//	if err != nil {
//		c.JSON(http.StatusInternalServerError, gin.H{
//			"code": 90500,
//			"msg":  err.Error(),
//			"data": nil,
//		})
//		return
//	}
//
//	c.JSON(http.StatusOK, gin.H{
//		"code": 90200,
//		"msg":  "新增环境成功！",
//		"data": nil,
//	})
//}

// Update 更新环境
func (*roleMenuRelation) Update(c *gin.Context) {
	params := new(struct {
		RoleID              uint     `json:"role_id"`
		NewRoleMenuRelation []string `json:"new_role_menu_relation"`
		OldRoleMenuRelation []string `json:"old_role_menu_relation"`
	})

	// 绑定请求参数
	if err := c.ShouldBind(params); err != nil {
		logger.Error("Bind 请求参数失败：" + err.Error())
		c.JSON(http.StatusBadRequest, gin.H{
			"code": 90400,
			"msg":  err.Error(),
			"data": nil,
		})
		return
	}
	logger.Info(params)
	err := service.RoleMenuRelation.Update(params.RoleID, params.NewRoleMenuRelation, params.OldRoleMenuRelation)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{
			"code": 90500,
			"msg":  err.Error(),
			"data": nil,
		})
		return
	}

	c.JSON(http.StatusOK, gin.H{
		"code": 90200,
		"msg":  "更新环境信息成功！",
		"data": nil,
	})
}

//// Delete 删除环境
//func (*roleMenuRelation) Delete(c *gin.Context) {
//	params := new(struct {
//		ID uint `json:"id"`
//	})
//
//	// 绑定请求参数
//	if err := c.ShouldBind(params); err != nil {
//		logger.Error("Bind 请求参数失败：" + err.Error())
//		c.JSON(http.StatusBadRequest, gin.H{
//			"code": 90400,
//			"msg":  err.Error(),
//			"data": nil,
//		})
//		return
//	}
//
//	err := service.RoleMenuRelation.Delete(params.ID)
//	if err != nil {
//		c.JSON(http.StatusInternalServerError, gin.H{
//			"code": 90500,
//			"msg":  err.Error(),
//			"data": nil,
//		})
//		return
//	}
//
//	c.JSON(http.StatusOK, gin.H{
//		"code": 90200,
//		"msg":  "删除环境成功！",
//		"data": nil,
//	})
//}
