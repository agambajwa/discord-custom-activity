from discoIPC import ipc
import configparser
import time

config = configparser.ConfigParser()
config.read('config.ini')

base_activity = {
    'details': 'Custom details',
    'state' : 'Custom state',
    'assets': {
        'large_image': 'image_name',
        'large_text': 'Image text',
        'small_image': 'small_image_name',
        'small_text': 'Small image text'
    },
    'party': {
        'size': [1, 5]
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
    return activity

if __name__ == '__main__':
    main()
