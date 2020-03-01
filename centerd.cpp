#include"opencv2/core/core.hpp"
#include"opencv2/imgproc/imgproc.hpp"
#include"opencv2/highgui/highgui.hpp"
#include <iostream>
#include <cmath>
using namespace cv;
using namespace std;

float distance(int x1, int y1, int x2, int y2){
	float result = sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1));
	return result ;
}

int main(){

	Mat img = imread("1.png", 2);
	Mat img1;
	Canny(img, img1, 15, 200, 3);
	imshow("canny", img1);
	//GaussianBlur( img, img, Size(9,9), 2, 2 );
	int x = img1.rows;
	int y = img1.cols;
	Mat img2(x, y, CV_8UC3, Scalar(255, 255, 255));
	namedWindow("centerdet", WINDOW_NORMAL);
	float slope = -9.0/5 ;
	float theta = atan(slope);
	float a = sin(theta), b = cos(theta);
	float rad;
	int arr[4][2]; 
	cout << theta << endl; 
	vector<Vec3f> circles;
	HoughCircles(img1, circles, CV_HOUGH_GRADIENT, 1, 40, 200, 15, 1, 100);
	cout << circles.size() << " ran " << endl;
	for(int i = 0; i < circles.size() ; i++){
		Vec3i c = circles[i];
		cout << c[0] << " " << c[1] << endl;
		int x1 = c[0], y1 = c[1] ;
		for(int j = -1; j< 2;j++){
			for(int k = -1; k < 2; k++){
				img2.at<Vec3b>(y1+j, x1+k)[0] = 0;
				img2.at<Vec3b>(y1+j, x1+k)[1] = 0;
				img2.at<Vec3b>(y1+j, x1+k)[2] = 255;
			}
		}
		rad = c[2];
		arr[i][0] = c[0];
		arr[i][1] = c[1];

	}
	//cout << rad << endl;
	int i = 0;
	while(1){	

		for(int j = -1; j< 2;j++){
			for(int k = -1; k < 2; k++){
				img2.at<Vec3b>(arr[i][1]+j, arr[i][0]+k)[0] = 255;
				img2.at<Vec3b>(arr[i][1]+j, arr[i][0]+k)[1] = 255;
				img2.at<Vec3b>(arr[i][1]+j, arr[i][0]+k)[2] = 255;
			}
		}
		waitKey(250);
		//cout << " running" << endl;
		arr[i][0] = cvRound(arr[i][0] + 25*b);
		arr[i][1] = cvRound(arr[i][1] + 25*a);
		for(int j = -1; j< 2;j++){
			for(int k = -1; k < 2; k++){
				img2.at<Vec3b>(arr[i][1]+j, arr[i][0]+k)[0] = 0;
				img2.at<Vec3b>(arr[i][1]+j, arr[i][0]+k)[1] = 0;
				img2.at<Vec3b>(arr[i][1]+j, arr[i][0]+k)[2] = 255;
			}
		}
		imshow("centerdet", img2);
		//cout << " ran" << endl;
		for(int l = 0; l< circles.size(); l++){
			int x2 = arr[l][0];
			int y2 = arr[l][1];
			//cout << l << " " << endl;
			float d = distance(x2, y2, arr[i][0], arr[i][1]);
			//cout << d << " " ;
			if((d < 2*rad) && (d > 0)){
				i = l ;
				cout << l << " " ;
				//cout << i << " ran1" << endl; 
			}
		}
		if(arr[i][0] > y || arr[i][0] < 0){
			b = -b ;
		}
		if(arr[i][1] > x || arr[i][1] < 0){
			a = -a ;
		}
	}
	
	waitKey(0);
	return 0;
}