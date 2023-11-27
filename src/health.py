import proto.health_pb2 as health_pb2
import proto.health_pb2_grpc as health_pb2_grpc


class HealthService(health_pb2_grpc.HealthServicer):
    def Check(self, request, context):
        response = health_pb2.HealthCheckResponse()
        response.status = health_pb2.HealthCheckResponse.ServingStatus.SERVING
        return response
