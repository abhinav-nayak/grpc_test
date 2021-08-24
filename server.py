from concurrent import futures
import grpc

from generated_automatically import test_pb2_grpc
from server_code import testing


class Server:

    @staticmethod
    def run():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        test_pb2_grpc.add_test_grpcServicer_to_server(testing(), server)
        server.add_insecure_port('[::]:50051')
        server.start()
        server.wait_for_termination()
        
if __name__ == '__main__':
    Server.run()
