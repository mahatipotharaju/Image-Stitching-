
clc;
clear all;
close all;

A = imread('1.jpg'); 
B = imread('2.jpg'); 
w1 = zeros(1944, 2592, 3, 'uint8');
for cnt=1:3
    imgA = A(:,:,cnt);
    imgB = B(:,:,cnt);
    pointsA = detectSURFFeatures(imgA);
    pointsB = detectSURFFeatures(imgB);
    [featuresA, pointsA] = extractFeatures(imgA, pointsA);
    [featuresB, pointsB] = extractFeatures(imgB, pointsB);
    
%%
    indexPairs = matchFeatures(featuresA, featuresB);
    pointsA = pointsA(indexPairs(:, 1), :);
    pointsB = pointsB(indexPairs(:, 2), :);  
%%    
    [tform, pointsBm, pointsAm] = estimateGeometricTransform(...
        pointsB, pointsA, 'affine');
    imgBp = imwarp(imgB, tform, 'OutputView', imref2d(size(imgB)));
    pointsBmp = transformPointsForward(tform, pointsBm.Location);
%%
    for i=1:1944
        for j=1:2592
            b = imgA(i, j);
            c = imgBp(i, j);
            w1(i, j,cnt) = min(b,c);
        end
    end
end

figure, clf;
imshow(w1);
title('Stitched Image');

