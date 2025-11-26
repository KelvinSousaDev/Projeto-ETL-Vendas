import schedule
import time
import os


def job():
  print("--- Iniciando ETL... ---")
  os.system('python etl_pipeline.py')
  print("--- Fim do ETL ---")

schedule.every(30).seconds.do(job)

print("Agendador ligado... (Ctrl+C para parar)")

while True:
    schedule.run_pending()
    time.sleep(1)