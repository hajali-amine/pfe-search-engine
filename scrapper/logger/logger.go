package logger

import "go.uber.org/zap"

func BuildLogger() *zap.SugaredLogger {
	config := zap.NewProductionConfig()
	config.Level = zap.NewAtomicLevelAt(zap.InfoLevel)

	l, _ := config.Build()
	return l.Sugar()
}
