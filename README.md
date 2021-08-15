# OpenCV-Moving_Object_Removal


### Sample video:

 ![sample](https://github.com/tejas-trivedi/OpenCV-Object_Removal/blob/master/Sample_videos/sample1.gif)
<br/><br/><br/>


## - Running Average Method: 
In this method, the moving objects and detected and removed. This is done by differentiating between the pixels that seem to change over time. The average is computed over previous and current frames in a loop until frames are exhausted.
### Result:
![result1](https://github.com/tejas-trivedi/OpenCV-Object_Removal/blob/master/Running_Average/average_result.jpeg)

<br/>

## - Median Filtering Method: 
This is a background subtraction method that approximates the median of each pixel to be the background. Here we assume that the median pixel is the background because the background is part that will be visible for most of the time in the video (considering static background with moving objects).
### Result:
![result1](https://github.com/tejas-trivedi/OpenCV-Object_Removal/blob/master/Median_Filtering/median_result_2.jpeg)


## Conclusion:
This is a very basic level implementation of background subtraction method. As we can see, the results here are not very accurate. A deep learning approach can achieve far more accuracy than this method 
