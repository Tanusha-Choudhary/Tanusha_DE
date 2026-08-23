import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.debug("debug")
try:
    amount ="100"
    f_amount= amount+10
    logging.info(f"f_amount:{f_amount}")
except TypeError as e:
    amount = "100"
    amount_n = int(amount)
    f_amount= amount_n+10
    logging.error(f"{e}:{f_amount}")
    # print(file_contents)
finally:
    logging.warning(f"f_amount:{f_amount}")