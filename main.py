"""
Dungeondelf main file
"""

import arcade

#Constants
WINDOW_W = 800
WINDOW_H = 600

#Globals
g_window_title = "Dunegondelf v 0.0.1"

class GameView(arcade.Window):
    """
    Main application class
    """

    def __init__(self):
        #call parent to set up window
        super().__init__(WINDOW_W, WINDOW_H, g_window_title)

        self.background_color = arcade.csscolor.BLACK

    def setup(self):
        """Set up or reset the game"""
        pass

    def on_draw(self):
        """Render the screen"""
        self.clear() #Leave at beginning of on_draw

def main():
    """Main func"""
    window = GameView()
    window.setup()
    arcade.run()
    
if __name__ == '__main__':
    main()