flag=1

config:
	python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. proto/key_value.proto
	python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. proto/central_management.proto


run_serv_pares_1:
	python svc_par.py $(arg)
run_serv_pares_2:
	python svc_par.py $(arg) $(flag) 
run_cli_pares:
	python cln_par.py $(arg)
run_serv_central:
	python svc_cen.py $(arg)
run_cli_central:
	python cln_cen.py $(arg)



clean:
	rm -rf *pb2*