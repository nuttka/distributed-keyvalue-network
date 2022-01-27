python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. proto/key_value.proto

python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. proto/central_management.proto