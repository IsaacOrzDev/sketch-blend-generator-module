gen:
	python -m grpc_tools.protoc --proto_path=. ./proto/*.proto --python_out=. --grpc_python_out=.