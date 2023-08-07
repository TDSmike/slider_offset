import cv2


class AutoSlider:
    def __init__(self,bg_path,tp1_path,tp2_path):
        self.begin = cv2.imread(tp1_path, 0)
        self.slider_img = cv2.imread(tp2_path, 0)
        self.background_img = cv2.imread(bg_path, 0)
        print(self.background_img.shape)

    def match_end(self):
        result = cv2.matchTemplate(self.background_img, self.slider_img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        slider_position = max_loc
        gap_position = (slider_position[0], slider_position[1])
        cv2.rectangle(self.background_img,gap_position,(slider_position[0]+50, slider_position[1]+50),(0,0,255),2)
        # uncommenting below to display image
        ###############################################
        # cv2.imshow('begin',self.background_img)
        # cv2.waitKey()
        ###############################################
        return slider_position[0]

    def match_begin(self):
        result1 = cv2.matchTemplate(self.background_img, self.begin, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result1)
        slider_position = max_loc
        gap_position = (slider_position[0], slider_position[1])
        cv2.rectangle(self.background_img,gap_position,(slider_position[0]+50, slider_position[1]+50),(0,0,255),2)
        # uncommenting below to display image
        ###############################################
        # cv2.imshow('end',self.background_img)
        # cv2.waitKey()
        ###############################################
        return slider_position[0]
    
    def offset(self):
        offset = self.match_end() - self.match_begin()
        print(f'picture size = {self.background_img.shape}, offset = {offset}')
        return offset
    
# sample = AutoSlider('pic.png','begin.png','end.png')
# print(sample.offset())