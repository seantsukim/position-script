#this is a script to get the positions of images into the inkscape svg
#these are the position and scale variables for the images
#start_x & start_y handle the position of the image
#start_w & start_h handle the scale of the image
start_x = 12.3
start_y = 11.6
start_w = 88.0
start_h = 63.0

eight_proxy_pos = []
rotate_cw = False

#for loops into the 8 different positions for the image
#we need the 8 positions for the grid to then put into inkscape
#(x ,    y,     w,    h)
#(12.3,  11.6,  88.0, 63.0)
#(12.3,  74.6,  88.0, 63.0)
#(12.3,  137.6, 88.0, 63.0)
#(12.3,  200.6, 88.0, 63.0)
#(100.3, 11.6,  88.0, 63.0)
#(100.3, 74.6,  88.0, 63.0)
#(100.3, 137.6, 88.0, 63.0)
#(100.3, 200.6, 88.0, 63.0)

#tracking the x and y values as the loop goes on, with these mutable variables
new_x = start_x
new_y = start_y
#we for loop twice for the x values 12.3 then transition to 100.3
for x_pos in range(0,2):
    new_y = start_y
    #we for loop four times for the y values 11.6, 74.6, 137.6, & 200.6
    for y_pos in range(0,4):
        eight_proxy_pos.append((new_x, new_y, start_w, start_h, rotate_cw))
        new_y = new_y + 63.0
    new_x = start_x + 90.0
    rotate_cw = not rotate_cw

#now we print the results to visually see the result
index = 1
for pos in eight_proxy_pos:
    print("proxy position", index ,pos[0:-1], ", Rotate Clockwise:", pos[-1])
    index = index + 1 
