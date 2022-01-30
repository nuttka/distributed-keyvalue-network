flag=1

config: clean
	python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. proto/key_value.proto
	python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. proto/central_management.proto


run_serv_pares_1: config
	python svc_par.py $(arg)
run_serv_pares_2: config
	python svc_par.py $(arg) $(flag) 
run_cli_pares: config
	python cln_par.py $(arg)
run_serv_central: config
	python svc_cen.py $(arg)
run_cli_central: config
	python cln_cen.py $(arg)



clean:
	rm -rf *pb2*