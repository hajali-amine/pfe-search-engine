package types

type Job struct {
	Title       string              `json:"title"`
	Description string              `json:"description"`
	Company     string              `json:"company"`
	Location    string              `json:"location"`
	Skills      []map[string]string `json:"skills"`
}