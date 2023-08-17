import os

def force_quit_service():
    try:
        # Get the process IDs of QuickLookUIService
        pids = os.popen('pgrep QuickLookUIService').read().strip().split('\n')
        if pids:
            for pid in pids:
                os.system('kill -9 {}'.format(pid))
            print('All instances of QuickLookUIService have been force quit.')
        else:
            print('QuickLookUIService is not running.')
    except Exception as e:
        print('Error: {}'.format(e))

if __name__ == "__main__":
    force_quit_service()
