# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from proto import generator_pb2 as proto_dot_generator__pb2


class GeneratorServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ScribblePredict = channel.unary_unary(
                '/generator.GeneratorService/ScribblePredict',
                request_serializer=proto_dot_generator__pb2.ScribblePredictRequest.SerializeToString,
                response_deserializer=proto_dot_generator__pb2.ScribblePredictReply.FromString,
                )
        self.ScribblePredictInBackground = channel.unary_unary(
                '/generator.GeneratorService/ScribblePredictInBackground',
                request_serializer=proto_dot_generator__pb2.ScribblePredictRequest.SerializeToString,
                response_deserializer=proto_dot_generator__pb2.ScribblePredictInBackgroundReply.FromString,
                )
        self.ScribblePredictStatus = channel.unary_unary(
                '/generator.GeneratorService/ScribblePredictStatus',
                request_serializer=proto_dot_generator__pb2.ScribblePredictInBackgroundReply.SerializeToString,
                response_deserializer=proto_dot_generator__pb2.ScribblePredictStatusReply.FromString,
                )
        self.CaptionPredict = channel.unary_unary(
                '/generator.GeneratorService/CaptionPredict',
                request_serializer=proto_dot_generator__pb2.CaptionPredictRequest.SerializeToString,
                response_deserializer=proto_dot_generator__pb2.CaptionPredictReply.FromString,
                )


class GeneratorServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ScribblePredict(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ScribblePredictInBackground(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ScribblePredictStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CaptionPredict(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GeneratorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ScribblePredict': grpc.unary_unary_rpc_method_handler(
                    servicer.ScribblePredict,
                    request_deserializer=proto_dot_generator__pb2.ScribblePredictRequest.FromString,
                    response_serializer=proto_dot_generator__pb2.ScribblePredictReply.SerializeToString,
            ),
            'ScribblePredictInBackground': grpc.unary_unary_rpc_method_handler(
                    servicer.ScribblePredictInBackground,
                    request_deserializer=proto_dot_generator__pb2.ScribblePredictRequest.FromString,
                    response_serializer=proto_dot_generator__pb2.ScribblePredictInBackgroundReply.SerializeToString,
            ),
            'ScribblePredictStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.ScribblePredictStatus,
                    request_deserializer=proto_dot_generator__pb2.ScribblePredictInBackgroundReply.FromString,
                    response_serializer=proto_dot_generator__pb2.ScribblePredictStatusReply.SerializeToString,
            ),
            'CaptionPredict': grpc.unary_unary_rpc_method_handler(
                    servicer.CaptionPredict,
                    request_deserializer=proto_dot_generator__pb2.CaptionPredictRequest.FromString,
                    response_serializer=proto_dot_generator__pb2.CaptionPredictReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'generator.GeneratorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GeneratorService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ScribblePredict(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/generator.GeneratorService/ScribblePredict',
            proto_dot_generator__pb2.ScribblePredictRequest.SerializeToString,
            proto_dot_generator__pb2.ScribblePredictReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ScribblePredictInBackground(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/generator.GeneratorService/ScribblePredictInBackground',
            proto_dot_generator__pb2.ScribblePredictRequest.SerializeToString,
            proto_dot_generator__pb2.ScribblePredictInBackgroundReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ScribblePredictStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/generator.GeneratorService/ScribblePredictStatus',
            proto_dot_generator__pb2.ScribblePredictInBackgroundReply.SerializeToString,
            proto_dot_generator__pb2.ScribblePredictStatusReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CaptionPredict(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/generator.GeneratorService/CaptionPredict',
            proto_dot_generator__pb2.CaptionPredictRequest.SerializeToString,
            proto_dot_generator__pb2.CaptionPredictReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
