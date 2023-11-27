import grpc
from concurrent import futures
from grpc_reflection.v1alpha import reflection
from dotenv import load_dotenv
from src.health import HealthService
from src.generator import GeneratorService
import proto.generator_pb2 as generator_pb2
import proto.generator_pb2_grpc as generator_pb2_grpc
import proto.health_pb2 as health_pb2
import proto.health_pb2_grpc as health_pb2_grpc
import os

load_dotenv()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    generator_pb2_grpc.add_GeneratorServiceServicer_to_server(
        GeneratorService(), server=server
    )
    health_pb2_grpc.add_HealthServicer_to_server(
        HealthService(), server=server
    )
    server.add_insecure_port('[::]:{}'.format(os.environ.get("PORT") or 5002))
    SERVICE_NAMES = (
        generator_pb2.DESCRIPTOR.services_by_name['GeneratorService'].full_name,
        health_pb2.DESCRIPTOR.services_by_name['Health'].full_name,
        reflection.SERVICE_NAME
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    print("Server started")
    serve()
