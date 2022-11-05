import numpy as np
import cv2 as cv
import math    

"""
Image morphing using affine transformatins"
"""
            
def imgmorphing(img1, img2):
            numpy1 = np.array([[218, 240],[295, 240],[250, 383]],np.float32)
            numpy2 = np.array([[248, 245],[345, 270],[281, 366]],np.float32)
            numpy3 =np.zeros((3,2),np.float32)
            numpy4 =np.zeros((3,2),np.float32)
            iterations = 66.0 #Number of iterations 
            piece = 1.0 / iterations
            for i in range(0,int(iterations)):
                        for j in range(0,3):
                                    disx = (numpy1[j,0] - numpy2[j,0])*-1
                                    disy = (numpy1[j,1] - numpy2[j,1])*-1
        
                                    movex1 = (disx/iterations) * (i+1)
                                    movey1 = (disy/iterations) * (i+1)
        
       
                                    movex2 =disx-movex1
                                    movey2 =disy-movey1
            
                                    numpy3[j,0] = numpy1[j,0] + movex1
                                    numpy3[j,1] = numpy1[j,1] + movey1
        
                                    numpy4[j,0] = numpy2[j,0] - movex2
                                    numpy4[j,1] = numpy2[j,1] - movey2
                        mat1=cv.getAffineTransform(numpy1, numpy3)
                        mat2=cv.getAffineTransform(numpy2, numpy4)
                        dst1=cv.warpAffine(img1, mat1, (img1.shape[1],img1.shape[0]),None,None,cv.BORDER_REPLICATE)
                        dst2=cv.warpAffine(img2, mat2, (img1.shape[1],img1.shape[0]),None,None,cv.BORDER_REPLICATE)
                        dst=cv.addWeighted(dst1, 1-(piece*(i)), dst2, piece*(i+1), 0)
                        cv.imshow("dst",dst)
                        cv.waitKey(25)
            cv.waitKey(0)
def main():
            img1 = cv.imread("Downloads/abbeel.jpeg")
            img2 = cv.imread("Downloads/malik.jpeg")
            imgmorphing(img1, img2)
main()
             

  
 