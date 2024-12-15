package main

import (
	"context"
	"log"
	"time"

	pb "quadrocopter-management-system/src/backend-go/pkg/cache"

	"google.golang.org/grpc"
)

// Этот клиент для тестирования

func main() {
	conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("Failed to connect to gRPC server: %v", err)
	}
	defer conn.Close()

	client := pb.NewCacheServiceClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	_, err = client.Set(ctx, &pb.SetRequest{
		Key:   "example_key",
		Value: "Hello, World!",
		Ttl:   60, // 1 минута
	})
	if err != nil {
		log.Fatalf("Failed to set key: %v", err)
	}
	log.Println("Key set successfully")

	response, err := client.Get(ctx, &pb.GetRequest{Key: "example_key"})
	if err != nil {
		log.Fatalf("Failed to get key: %v", err)
	}
	log.Printf("Value for key 'example_key': %s", response.Value)
}
