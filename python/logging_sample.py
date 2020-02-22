import logging 

if __name__ == "__main__":
  log = logging.getLogger('Console')
  log.setLevel(logging.INFO)

  consoleHandler = logging.StreamHandler()
  consoleHandler.name = 'SystemOut'
  consoleHandler.setLevel(logging.INFO)
  consoleHandler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
  log.addHandler(consoleHandler)

  log.info("Hello world")

  log.info("Print handlers")
  for i in log.handlers:
    log.info(i.name)
    log.info(isinstance(i, logging.StreamHandler))
  
  log.info("Find the handlers using a lambda")
  ch = filter(lambda h: isinstance(i,logging.StreamHandler), log.handlers)
  for i in ch:
    log.info(i)

  log.info("Remove a handler")
  log.removeHandler(consoleHandler)
  
  print("Try to find the handler using a lambdas")
  ch = filter(lambda h: isinstance(i,logging.StreamHandler), log.handlers)
  print(ch)
  for i in ch:
    print(i)

  if not ch:
    log.addHandler(consoleHandler)
  log.info("Hanlder added succsfully")
