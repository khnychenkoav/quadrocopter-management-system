package main

import (
	"log"
	"net"
	"quadrocopter-management-system/src/backend-go/internal/api"
	"quadrocopter-management-system/src/backend-go/internal/repository"
	"quadrocopter-management-system/src/backend-go/internal/service"

	pb "quadrocopter-management-system/src/backend-go/pkg/cache"

	"google.golang.org/grpc"
)

func main() {
	// Инициализация Redis
	redisRepo := repository.NewRedisRepository("localhost:6379")
	cacheService := service.NewCacheService(redisRepo)
	cacheHandler := api.NewCacheHandler(cacheService)

	// Настройка gRPC сервера
	grpcServer := grpc.NewServer()
	pb.RegisterCacheServiceServer(grpcServer, cacheHandler)

	// Запуск сервера
	listener, err := net.Listen("tcp", ":50051")
	if err != nil {
		log.Fatalf("Failed to listen: %v", err)
	}
	log.Println("gRPC server is running on port :50051")
	if err := grpcServer.Serve(listener); err != nil {
		log.Fatalf("Failed to serve: %v", err)
	}
}
