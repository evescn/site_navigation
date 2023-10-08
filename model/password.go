package model

import "time"

type Password struct {
	ID       uint   `json:"id" gorm:"primary_key"`
	Name     string `json:"name"`
	Password string `json:"password"`

	CreatedAt time.Time
	UpdatedAt time.Time
	DeletedAt *time.Time `sql:"index"`
}

// TableName 自定义表名
func (*Password) TableName() string {
	return "password"
}
