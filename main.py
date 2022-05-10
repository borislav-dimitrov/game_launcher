from controller.main_controller import MainController
import tkinter as tk

# TODO
from view.main_view import MainView


def main():
    main_controller = MainController()
    main_controller.startup()

    root = tk.Tk()
    main_view = MainView(root, "Game Launcher", main_controller, resolution=(540, 720))
    main_controller.view = main_view
    root.mainloop()

    main_controller.custom_exit()


if __name__ == '__main__':
    main()
