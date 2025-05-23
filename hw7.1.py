import logging
import random

logging.basicConfig(
    filename='log.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')

def orel_reshka():
    result = random.choice(['Орел', 'Решка'])
    print('Випало:', result)
    return result

def test(result):
    if result == 'Орел':
        print('true')
    elif result == 'Решка':
        print('false')
    logging.info('Test completed successfully')

orelreshka_simulator = orel_reshka()
test(orelreshka_simulator)
