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
        response = generator_pb2.PredictReply()
        urls = []
        iterator = replicate.run(
            os.environ.get("SCRIBBLE_MODEL"),
            input={
                "prompt": request.prompt, 
                "structure": "scribble"
            }
        )
        for image in iterator:
            urls.append(image)
        response.urls.extend(urls)
        return response
    
    def ScribblePredict(self, request, context):
        response = generator_pb2.ScribblePredictReply()

        iterator = replicate.run(
            os.environ.get("SCRIBBLE_MODEL"),
            input={
                "prompt": request.prompt, 
                "image": request.imageUrl, 
                "structure": "scribble"
            }
        )
        url = None
        for image in iterator:
            url = image
        response.url = url
        return response
    
    def CaptionPredict(self, request, context):
        response = generator_pb2.CaptionPredictReply()
        iterator = replicate.run(
            os.environ.get("BLIP_MODEL"),
            input={
                "image": request.imageUrl, 
                "task": "image_captioning"
            }
        )
        caption = ""
        for item in iterator:
            caption += item
        response.caption = caption.replace("Caption: ", "")
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    generator_pb2_grpc.add_GeneratorServiceServicer_to_server(
        GeneratorService(), server=server
    )
    server.add_insecure_port('[::]:{}'.format(os.environ.get("PORT") or 5002))
    SERVICE_NAMES = (
        generator_pb2.DESCRIPTOR.services_by_name['GeneratorService'].full_name,
        reflection.SERVICE_NAME
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
