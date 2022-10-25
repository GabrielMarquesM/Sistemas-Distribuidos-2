# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import actuators_services_pb2 as actuators__services__pb2


class ACStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.turnOn = channel.unary_unary(
                '/AC/turnOn',
                request_serializer=actuators__services__pb2.Empty.SerializeToString,
                response_deserializer=actuators__services__pb2.TempPowerStatus.FromString,
                )
        self.turnOff = channel.unary_unary(
                '/AC/turnOff',
                request_serializer=actuators__services__pb2.Empty.SerializeToString,
                response_deserializer=actuators__services__pb2.TempPowerStatus.FromString,
                )
        self.switchPower = channel.unary_unary(
                '/AC/switchPower',
                request_serializer=actuators__services__pb2.Empty.SerializeToString,
                response_deserializer=actuators__services__pb2.TempPowerStatus.FromString,
                )
        self.changeTemperature = channel.unary_unary(
                '/AC/changeTemperature',
                request_serializer=actuators__services__pb2.TempRequest.SerializeToString,
                response_deserializer=actuators__services__pb2.TempResponse.FromString,
                )


class ACServicer(object):
    """Missing associated documentation comment in .proto file."""

    def turnOn(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def turnOff(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def switchPower(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def changeTemperature(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ACServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'turnOn': grpc.unary_unary_rpc_method_handler(
                    servicer.turnOn,
                    request_deserializer=actuators__services__pb2.Empty.FromString,
                    response_serializer=actuators__services__pb2.TempPowerStatus.SerializeToString,
            ),
            'turnOff': grpc.unary_unary_rpc_method_handler(
                    servicer.turnOff,
                    request_deserializer=actuators__services__pb2.Empty.FromString,
                    response_serializer=actuators__services__pb2.TempPowerStatus.SerializeToString,
            ),
            'switchPower': grpc.unary_unary_rpc_method_handler(
                    servicer.switchPower,
                    request_deserializer=actuators__services__pb2.Empty.FromString,
                    response_serializer=actuators__services__pb2.TempPowerStatus.SerializeToString,
            ),
            'changeTemperature': grpc.unary_unary_rpc_method_handler(
                    servicer.changeTemperature,
                    request_deserializer=actuators__services__pb2.TempRequest.FromString,
                    response_serializer=actuators__services__pb2.TempResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'AC', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AC(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def turnOn(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AC/turnOn',
            actuators__services__pb2.Empty.SerializeToString,
            actuators__services__pb2.TempPowerStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def turnOff(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AC/turnOff',
            actuators__services__pb2.Empty.SerializeToString,
            actuators__services__pb2.TempPowerStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def switchPower(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AC/switchPower',
            actuators__services__pb2.Empty.SerializeToString,
            actuators__services__pb2.TempPowerStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def changeTemperature(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AC/changeTemperature',
            actuators__services__pb2.TempRequest.SerializeToString,
            actuators__services__pb2.TempResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
