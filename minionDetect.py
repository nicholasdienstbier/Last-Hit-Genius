import cv2


# Load Screenshots
def load_screenshots():
    # load all of the screenshots
    screenshots = []
    for i in range(1, 15):
        img = cv2.imread(f"../inGameScreenshots/Screen{i}.png")        
        screenshots.append(img)
    return screenshots

screenshots = load_screenshots()