import grpc
from concurrent import futures
from grpc_reflection.v1alpha import reflection
import proto.generator_pb2 as generator_pb2
import proto.generator_pb2_grpc as generator_pb2_grpc
import replicate
from dotenv import load_dotenv
import os

load_dotenv()


class GeneratorService(generator_pb2_grpc.GeneratorServiceServicer):
    def Predict(self, request, context):
        response = generator_pb2.PredictResponse()
        urls = []
        iterator = replicate.run(
            os.environ.get("REPLICATE_MODEL"),
            input={"prompt": request.prompt}
        )
        for image in iterator:
            urls.append(image)
        response.urls.extend(urls)
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    generator_pb2_grpc.add_GeneratorServiceServicer_to_server(
        GeneratorService(), server=server
    )
    server.add_insecure_port('[::]:{}'.format(os.environ.get("PORT")))
    SERVICE_NAMES = (
        generator_pb2.DESCRIPTOR.services_by_name['GeneratorService'].full_name,
        reflection.SERVICE_NAME
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
