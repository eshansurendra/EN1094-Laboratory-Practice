randomArrayFirst = rand(5,10)*50+50;

% Process of vectorization

tic

sinArray = sin(randomArrayFirst);
finishtime = toc;

disp([' Time elapsed for vectorization process : ' num2str(finishtime)]);

% For looping Process
tic
[rows,columns] = size(randomArrayFirst);
sineArray_2 = zeros(rows,columns);

for index = 1:rows
    for x = 1:columns
        sineArray_2(index,x) = sin(randomArrayFirst(index,x));
    end
end

finishtime = toc;
disp([' Time elapsed for using a for loop process : ' num2str(finishtime)]);
