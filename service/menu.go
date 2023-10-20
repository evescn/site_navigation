package service

import (
	"errors"
	"github.com/wonderivan/logger"
	"site_navigation/dao"
	"site_navigation/model"
)

var Menu menus

type menus struct{}

// List 返回列表
func (*menus) List(menuName string, page, limit int) (*dao.Menus, error) {
	return dao.Menu.List(menuName, page, limit)
}

// GetAll 查询所有页面信息
func (*menus) GetAll() ([]*model.Menu, error) {
	return dao.Menu.GetAll()
}

// Get 根据 ID 查询，查询页面信息
func (*menus) Get(ID uint) (*model.Menu, bool, error) {
	return dao.Menu.Get(ID)
}

// Add 创建环境
func (*menus) Add(m *model.Menu) error {
	// 判断环境是否存在
	_, has, err := dao.Menu.Has(m.Path)
	if err != nil {
		return err
	}

	if has {
		logger.Error("当前数据已存在，请重新创建")
		return errors.New("当前数据已存在，请重新创建")
	}

	// 不存在则创建数据
	if err = dao.Menu.Add(m); err != nil {
		return err
	}

	return nil
}

// Update 更新环境
func (*menus) Update(m *model.Menu) error {
	return dao.Menu.Update(m)
}

// Delete 删除环境
func (*menus) Delete(ID uint) error {
	_, has, err := dao.SubMenu.GetP(ID)
	if err != nil {
		return err
	}

	if has {
		logger.Error("当前页面关联子页面信息，请先删除关联信息")
		return errors.New("当前页面关联子页面信息，请先删除关联信息")
	}

	return dao.Menu.Delete(ID)
}
