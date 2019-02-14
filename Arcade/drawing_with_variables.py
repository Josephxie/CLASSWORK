import arcade

print ("What would you like for the x coordinate")
center_x = int(input())

print ("What would you like for the y coordinate")
center_y = int(input())

print ("What would like for the size")
size = int(input())

print
WIDTH = 640
HEIGHT = 480

#x, y, radius getting user input for x, y and radius
#x = int(input("Enter x location: "))
#y = int(input("Enter y location: "))
radius = int(input)


arcade.open_window(WIDTH, HEIGHT, "My Drawing")
arcade.set_background_color(arcade.color.BLACK)

arcade.start_render()
# Begin drawing

arcade.draw_circle_filled(center_x, center_y, size, arcade.color.BONDI_BLUE)

# End drawing
arcade.finish_render()
arcade.run()