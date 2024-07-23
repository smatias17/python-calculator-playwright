requirements:
	@pip3 install -r requirements.txt
	@pip3 install pytest-playwright playwright -U

test_add:
	@PYTHONPATH=. pytest --numprocesses auto -k add --junit-xml=reports/xml/report_add_calculator.xml

test_divide:
	@PYTHONPATH=. pytest --numprocesses auto -k divide --junit-xml=reports/xml/report_divide_calculator.xml

test_subtract:
	@PYTHONPATH=. pytest --numprocesses auto -k subtract --junit-xml=reports/xml/report_subtract_calculator.xml

test_multiply:
	@PYTHONPATH=. pytest --numprocesses auto -k multiply --junit-xml=reports/xml/report_multiply_calculator.xml

test_edge:
	@PYTHONPATH=. pytest --numprocesses auto -k ec --junit-xml=reports/xml/report_ec_calculator.xml

test_full:
	@PYTHONPATH=. pytest --numprocesses auto --junit-xml=reports/xml/report_full_calculator.xml