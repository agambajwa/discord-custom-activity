from discoIPC import ipc
import configparser
import time

config = configparser.ConfigParser()
config.read('config.ini')

base_activity = {
    'details': "Poopin' on da toilet",
    'state' : 'Blaze',
    'timestamps': {},
    'assets': {
        'large_image': 'main_image',
        'large_text': "Drop D'Turd",
        'small_image': 'small_image',
        'small_text': 'Its a me'
    },
    'party': {
        'size': [69, 420]
    }
}

def main():
    client = ipc.DiscordIPC(config['CLIENT']['client_id'])
    # Connect to Discord Client
    client.connect()

    print('\nStarting Custom Activity...\n')
    time.sleep(5)

    try:
        client.update_activity(set_activity()) # Update Activity
        while True:
            input('\nConnected! ')
            # Do nothing   

    except KeyboardInterrupt:
        print('Disconnecting...\n')
        client.disconnect()

def set_activity():
    """Set acitivty for the player."""
    activity = base_activity
    activity['timestamps']['start'] = time.time()
    return activity

if __name__ == '__main__':
    main()
