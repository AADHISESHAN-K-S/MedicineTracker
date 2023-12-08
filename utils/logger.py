def setup_logging(file_name):
	path = "logs/"+file_name
	log_format = '%(asctime)s - %(levelname)s - %(message)s'

	logger = logging.getLogger(file_name)
	logger.setLevel(logging.INFO)

	# file handler
	file_handler = logging.FileHandler(path)
	logger.addHandler(file_handler)

	# formatter
	formatter = logging.Formatter(log_format)
	file_handler.setFormatter(formatter)

	return logger