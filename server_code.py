from generated_automatically import test_pb2, test_pb2_grpc

class testing(test_pb2_grpc.test_grpcServicer):
	def test_function(self, request, context):
		if request.number == 0:
			answer = "false"
		else:
			answer = "true"
		return test_pb2.output(status=answer)

