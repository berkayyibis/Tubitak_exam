clc;
clear;

for i=0:6
    test0=imread(strcat('test_',num2str(i),'.tif'));
    %imshow(test0)
    test0gray=rgb2gray(test0);
    %imshow(test0gray)
    [height, width, dim] = size(test0gray);
    centerWidth=round(width/2);
    centerHeight=round(height/2);
    BoxBottomX=centerWidth-128;
    BoxBottomY=centerHeight-128;
    cropimg=imcrop(test0gray, [BoxBottomX BoxBottomY 255 255]);
    %imshow(cropimg)
    lap = [1 1 1; 1 -8 1; 1 1 1]; %laplacian filtresi
    laplacian = imfilter(cropimg, lap, 'conv'); 
    %imshow(laplacian) 
    nMean=mean2(laplacian);%ortalama 
    nStd=std2(laplacian);%standard sapma
    nResult=nStd^2;%varyans deðeri
    disp(strcat('Variance Value of Test_',num2str(i),' Image'))
    disp(nResult)
    imwrite(cropimg,sprintf('testoutput_%d',i),'tif');
end
