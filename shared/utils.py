import time


def measure_response_time(func, *args, **kwargs):
    """
    Measure the execution time of a function and return its result.
    
    Args:
        func (function): The function to measure.
        *args: Positional arguments for the function.
        **kwargs: Keyword arguments for the function.
        
    Returns:
        tuple: (result of the function, execution time in milliseconds)
    """
    start_time = time.time()  
    result = func(*args, **kwargs)  
    end_time = time.time()  
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    return result, execution_time