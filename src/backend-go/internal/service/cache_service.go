package service

import (
	"context"
	"quadrocopter-management-system/src/backend-go/internal/repository"
	"time"
)

type CacheService struct {
	repo *repository.RedisRepository
}

func NewCacheService(repo *repository.RedisRepository) *CacheService {
	return &CacheService{repo: repo}
}

func (s *CacheService) Get(ctx context.Context, key string) (string, error) {
	return s.repo.Get(ctx, key)
}

func (s *CacheService) Set(ctx context.Context, key string, value string, ttl int64) error {
	return s.repo.Set(ctx, key, value, time.Duration(ttl)*time.Second)
}
