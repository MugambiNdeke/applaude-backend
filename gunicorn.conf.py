import multiprocessing

bind = "0.0.0.0:8080"
workers = 2  # Adjust based on droplet size, usually (2 x CPUs) + 1
threads = 4
timeout = 120
accesslog = "-"
errorlog = "-"
