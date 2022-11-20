package types

type Job struct {
	Title string `json:"title"`
	Description string `json:"description"`
	Logo string `json:"logo"`
	Company string `json:"company"`
	Location string `json:"location"`
	Skills []string `json:"skills"`
}