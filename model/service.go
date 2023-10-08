package model

import "time"

type Service struct {
	ID       uint   `json:"id" gorm:"primary_key"`
	Name     string `json:"name"`
	Url      string `json:"url"`
	Describe string `json:"describe"`
	Eid      uint   `json:"eid"`
	Pid      uint   `json:"pid"`

	CreatedAt time.Time
	UpdatedAt time.Time
	DeletedAt *time.Time `sql:"index"`
}

// TableName 自定义表名
func (*Service) TableName() string {
	return "service"
}
