import adafruit_dht
import board 
import Time 
dhtSensor = adafruit_dht.DHT11(board.D4)
try: 
     while true : 
              try: 
                    humidity = dhtSensor.humidity
                    temp_c = dhtSensor.temperature
                    temp_f = temp_c*(9/5)+32
                    print("temp: {:.1f} F / {:.1f} C  Humidity: {}% ".format(temp_f, temp_c , humidity ))
                    time.sleep(2.0) 
              except RuntimeError as error : 
                       print(error.args[0]) 
                       time.sleep(2.0)
                       continue 
              except Exception as error : 
                       dhtSensor.exit() 
                       raise error 
except KeyboardInterrupt : 
        # If there is a KeyboardInterrupt , exit the program and cleanup 
        print("Cleaning up!") 
        dhtSensor.exit() 
