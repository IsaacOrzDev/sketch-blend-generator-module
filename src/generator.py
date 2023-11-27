import proto.generator_pb2 as generator_pb2
import proto.generator_pb2_grpc as generator_pb2_grpc
import replicate
import os


class GeneratorService(generator_pb2_grpc.GeneratorServiceServicer):
    def ScribblePredict(self, request, context):
        response = generator_pb2.ScribblePredictReply()

        iterator = replicate.run(
            os.environ.get("SCRIBBLE_MODEL"),
            input={
                "prompt": request.prompt,
                "image": request.imageUrl,
                "structure": "scribble",
                "n_prompt": os.environ.get("N_PROMPT")
            }
        )
        url = None
        for image in iterator:
            url = image
        response.url = url
        return response

    def ScribblePredictInBackground(self, request, context):
        response = generator_pb2.ScribblePredictInBackgroundReply()
        parts = os.environ.get("SCRIBBLE_MODEL").split(":")
        model = replicate.models.get(parts[0])
        version = model.versions.get(parts[1])
        prediction = replicate.predictions.create(
            version=version,
            input={
                "prompt": request.prompt,
                "image": request.imageUrl,
                "structure": "scribble",
                "n_prompt": os.environ.get("N_PROMPT")
            })
        response.id = prediction.id
        return response

    def ScribblePredictStatus(self, request, context):
        response = generator_pb2.ScribblePredictStatusReply()
        prediction = replicate.predictions.get(request.id)
        response.status = prediction.status
        if prediction.output is not None:
            for image in prediction.output:
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
