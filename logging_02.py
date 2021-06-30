import logging

'''
logger = logging.getLogger(__name__)
logger.propagate = False
logger.info('Hello from helper')

'''

logger = logging.getLogger(__name__)

#cread handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# level and the format

stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formater = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formater)
file_h.setFormatter(formater)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is a warning')
logger.error('this is an error')