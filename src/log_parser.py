import logging
logger = logging.getLogger(__name__)
def main():
    logging.basicConfig(level = logging.INFO)
    logger.info("Starting log file processing")
           
        
if __name__ == '__main__':
    main()
    

def parse_log_line(line: str) -> dict | None:
    try:
        log_parser =line.strip().split(" ", 4)
        d={"date": log_parser[0], "time": log_parser[1], "level": log_parser[2], "service": log_parser[3], "message": log_parser[4]}
    except IndexError:
        return None
    return d

with open("sample.log", 'r') as file:
    for line in file:
        result= parse_log_line(line)
        if result is None:
            print(None)
        else:
            print(result)
        

  
        
       
            
    