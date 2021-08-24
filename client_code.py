from generated_automatically import test_pb2, test_pb2_grpc
import grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = test_pb2_grpc.test_grpcStub(channel)
        response = stub.test_function(test_pb2.input(number=0))
        print("For input number 0 client received: " + response.status)
        response = stub.test_function(test_pb2.input(number=1))
        print("For input number 1 client received: " + response.status)


if __name__ == '__main__':
    run()


