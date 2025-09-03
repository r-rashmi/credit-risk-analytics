import logging

def setup_logger():
    """
    Set up and return a logger for the project.
    """
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler()
        ]
    )
    
    # Get a logger 
    logger = logging.getLogger('credit_risk_analytics')
    logger.info("Logger initialized")
    return logger