package api

import (
	"context"
	"quadrocopter-management-system/src/backend-go/internal/service"

	pb "quadrocopter-management-system/src/backend-go/pkg/cache"
)

type CacheHandler struct {
	pb.UnimplementedCacheServiceServer
	service *service.CacheService
}

func NewCacheHandler(service *service.CacheService) *CacheHandler {
	return &CacheHandler{service: service}
}

func (h *CacheHandler) Get(ctx context.Context, req *pb.GetRequest) (*pb.GetResponse, error) {
	value, err := h.service.Get(ctx, req.Key)
	if err != nil {
		return nil, err
	}
	return &pb.GetResponse{Value: value}, nil
}

func (h *CacheHandler) Set(ctx context.Context, req *pb.SetRequest) (*pb.SetResponse, error) {
	err := h.service.Set(ctx, req.Key, req.Value, req.Ttl)
	if err != nil {
		return nil, err
	}
	return &pb.SetResponse{Success: true}, nil
}
