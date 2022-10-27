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
                response_deserializer=actuators__services__pb2.PowerStatus.FromString,
                )
        self.turnOff = channel.unary_unary(
                '/AC/turnOff',
                request_serializer=actuators__services__pb2.Empty.SerializeToString,
                response_deserializer=actuators__services__pb2.PowerStatus.FromString,
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
                    response_serializer=actuators__services__pb2.PowerStatus.SerializeToString,
            ),
            'turnOff': grpc.unary_unary_rpc_method_handler(
                    servicer.turnOff,
                    request_deserializer=actuators__services__pb2.Empty.FromString,
                    response_serializer=actuators__services__pb2.PowerStatus.SerializeToString,
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
            actuators__services__pb2.PowerStatus.FromString,
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
            actuators__services__pb2.PowerStatus.FromString,
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


class LampStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.turnOn = channel.unary_unary(
                '/Lamp/turnOn',
                request_serializer=actuators__services__pb2.Empty.SerializeToString,
                response_deserializer=actuators__services__pb2.PowerStatus.FromString,
                )
        self.turnOff = channel.unary_unary(
                '/Lamp/turnOff',
                request_serializer=actuators__services__pb2.Empty.SerializeToString,
                response_deserializer=actuators__services__pb2.PowerStatus.FromString,
                )
        self.changeColor = channel.unary_unary(
                '/Lamp/changeColor',
                request_serializer=actuators__services__pb2.ColorRequest.SerializeToString,
                response_deserializer=actuators__services__pb2.ColorResponse.FromString,
                )


class LampServicer(object):
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

    def changeColor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LampServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'turnOn': grpc.unary_unary_rpc_method_handler(
                    servicer.turnOn,
                    request_deserializer=actuators__services__pb2.Empty.FromString,
                    response_serializer=actuators__services__pb2.PowerStatus.SerializeToString,
            ),
            'turnOff': grpc.unary_unary_rpc_method_handler(
                    servicer.turnOff,
                    request_deserializer=actuators__services__pb2.Empty.FromString,
                    response_serializer=actuators__services__pb2.PowerStatus.SerializeToString,
            ),
            'changeColor': grpc.unary_unary_rpc_method_handler(
                    servicer.changeColor,
                    request_deserializer=actuators__services__pb2.ColorRequest.FromString,
                    response_serializer=actuators__services__pb2.ColorResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Lamp', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Lamp(object):
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
        return grpc.experimental.unary_unary(request, target, '/Lamp/turnOn',
            actuators__services__pb2.Empty.SerializeToString,
            actuators__services__pb2.PowerStatus.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/Lamp/turnOff',
            actuators__services__pb2.Empty.SerializeToString,
            actuators__services__pb2.PowerStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def changeColor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Lamp/changeColor',
            actuators__services__pb2.ColorRequest.SerializeToString,
            actuators__services__pb2.ColorResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class SprinkleStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.turnOn = channel.unary_unary(
                '/Sprinkle/turnOn',
                request_serializer=actuators__services__pb2.Empty.SerializeToString,
                response_deserializer=actuators__services__pb2.PowerStatus.FromString,
                )
        self.turnOff = channel.unary_unary(
                '/Sprinkle/turnOff',
                request_serializer=actuators__services__pb2.Empty.SerializeToString,
                response_deserializer=actuators__services__pb2.PowerStatus.FromString,
                )


class SprinkleServicer(object):
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


def add_SprinkleServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'turnOn': grpc.unary_unary_rpc_method_handler(
                    servicer.turnOn,
                    request_deserializer=actuators__services__pb2.Empty.FromString,
                    response_serializer=actuators__services__pb2.PowerStatus.SerializeToString,
            ),
            'turnOff': grpc.unary_unary_rpc_method_handler(
                    servicer.turnOff,
                    request_deserializer=actuators__services__pb2.Empty.FromString,
                    response_serializer=actuators__services__pb2.PowerStatus.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Sprinkle', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Sprinkle(object):
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
        return grpc.experimental.unary_unary(request, target, '/Sprinkle/turnOn',
            actuators__services__pb2.Empty.SerializeToString,
            actuators__services__pb2.PowerStatus.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/Sprinkle/turnOff',
            actuators__services__pb2.Empty.SerializeToString,
            actuators__services__pb2.PowerStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
