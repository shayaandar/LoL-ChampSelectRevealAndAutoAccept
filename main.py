import warnings
import urllib3
import lcu_class
import lcu_args

def main():
    lcu = lcu_class.LCU()
    lcu.set_region(lcu_args.get_lol_region())  # Set the region
    try:
        credentials = lcu_args.get_port_and_token()
    except:
        print("Credentials not retrieved, must start client or restart client")

    # Ignore certificate error 
    warnings.filterwarnings('ignore', category=urllib3.exceptions.InsecureRequestWarning)

    lcu.set_credentials(credentials[0], credentials[1], credentials[2], credentials[3])
    lcu.initialize_LCU()
    lcu.initialize_riot()
    # Checks game state, auto accepts queue, and auto pulls up u.gg for teammates
    lcu.recursive_gameflow_check()

if __name__ == "__main__":
    main()
