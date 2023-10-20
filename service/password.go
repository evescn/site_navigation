package service

import (
	"site_navigation/dao"
	"site_navigation/model"
)

var Password password

type password struct{}

// Add 创建密码
func (*password) Add(e *model.Password) (uint, error) {
	return dao.Password.Add(e)
}

// Update 更新环境
func (*password) Update(e *model.Password) error {
	return dao.Password.Update(e)
}

// Delete 删除环境
func (*password) Delete(id uint) error {
	return dao.Password.Delete(id)
}
