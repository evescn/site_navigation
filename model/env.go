package model

import "time"

type Env struct {
	ID       uint   `json:"id" gorm:"primary_key"`
	Name     string `json:"name"`
	Describe string `json:"describe"`

	CreatedAt time.Time
	UpdatedAt time.Time
	DeletedAt *time.Time `sql:"index"`
}

// TableName 自定义表名
func (*Env) TableName() string {
	return "env"
}
