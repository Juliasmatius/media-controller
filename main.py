def main():
    import guli
    from pyfiglet import Figlet
    print("Creating config...")
    temp_str = ""
    guli.GuliVariable("process_name").setValue(temp_str)
    print("Config created")
    print("Importing packages...")
    import media_controller
    from nicegui import ui
    print("Imported packages")
    print("Setting up nicegui...")
    ui.label("Welcome to Juli's media controller")
    ui.button('Play', on_click=lambda: media_controller.playpause())
    ui.button('Next song', on_click=lambda: media_controller.skip())
    ui.button('Previous song', on_click=lambda: media_controller.prev())
    ui.button('Mute', on_click=lambda: media_controller.mute())
    ui.button('Increase volume', on_click=lambda: media_controller.increase_volume())
    ui.button('Decrease volume', on_click=lambda: media_controller.decrease_volume())
    print("Nicegui setup")
    print("Starting webserver...")
    custom_fig = Figlet(font='starwars')
    print(custom_fig.renderText('Select your media app!!'))
    print("If using youtube, click the video.")
    try:
        ui.run()
    except KeyboardInterrupt:
        custom_fig = Figlet(font='starwars')
        print(custom_fig.renderText('Goodbye'))
        exit()