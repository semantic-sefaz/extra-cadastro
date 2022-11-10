#!/bin/bash
while true
do
	now=$(date +'%Y-%m-%d')
	#script -c "python carga_final.py" log/${now}.log
	python carga_final >> log/${now}.log
	echo "Processo concluído."
	sleep 1d
done