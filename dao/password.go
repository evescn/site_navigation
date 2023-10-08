package dao

import (
	"errors"
	"github.com/wonderivan/logger"
	"site_navigation/db"
	"site_navigation/model"
)

var Password password

type password struct{}

type Passwords struct {
	Items []*model.Password `json:"items"`
	Total int               `json:"total"`
}

// Update 更新
func (*password) Update(u *model.Password) error {
	tx := db.GORM.Model(&model.Password{}).Where("id = ?", u.ID).Updates(&u)
	if tx.Error != nil {
		logger.Error("更新Password信息失败," + tx.Error.Error())
		return errors.New("更新Password信息失败," + tx.Error.Error())
	}

	return nil
}

// Add 新增
func (*password) Add(u *model.Password) error {
	tx := db.GORM.Create(&u)
	if tx.Error != nil {
		logger.Error("新增Password信息失败," + tx.Error.Error())
		return errors.New("新增Password信息失败," + tx.Error.Error())
	}

	return nil
}

// Delete 删除
func (*password) Delete(id uint) error {
	data := new(model.Password)
	data.ID = id
	tx := db.GORM.Delete(&data)
	if tx.Error != nil {
		logger.Error("删除Password信息失败," + tx.Error.Error())
		return errors.New("删除Password信息失败," + tx.Error.Error())
	}

	return nil
}
