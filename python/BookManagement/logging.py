class Logger:
    def __init__(self):
        self.logs=[]

    def log(self,message,level="INFO"):
        log_entry=f"[{level}] {message}"
        self.logs.append(log_entry)
        print(log_entry)