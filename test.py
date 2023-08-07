import slider_class


## arg[0] = background, arg[1] = where slider begin(by screenshot), arg[2] = where slider end

sample = slider_class.AutoSlider('pic.png','begin.png','end.png')
print(sample.offset())