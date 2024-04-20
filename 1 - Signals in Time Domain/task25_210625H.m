% Getting user input for both arrays 

firstArray = input('Enter first array : ');
secondArray = input('Enter second array : ');


% Check whether dimensions are same in both arrays
if size(firstArray) == size(secondArray)

    % Check whether the elements are same in both arrays
    outputArray = (firstArray == secondArray);
    disp('Binary output array is :')
    disp(outputArray)

else
    error('Input arrays must have the same dimensions')

end