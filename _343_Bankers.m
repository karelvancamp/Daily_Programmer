function [] = _343_Bankers(available,Requires)

%?>> available = [3 3 2];
%>> Requires = [0 1 0 7 5 3;2 0 0 3 2 2;3 0 2 9 0 2;2 1 1 2 2 2;0 0 2 4 3 3;0 0 0 20 20 20];
%>> _343_Bankers(available,Requires)
  
rows = size(Requires)(1);
solution = [];
unachieved = 0:rows-1;
Requires1 = [unachieved' Requires];

c = 1;
while c > 0
  c = 0;
  Possible = Requires1(:,2:4) - Requires1(:,5:7) .+ available;
  Possible = [Requires1(:,1) Possible];
  targets = all(Possible' >= 0);
  
  for i = 1:rows
    if targets(i) > 0
      available = available + Requires(i,1:3);
      Requires1(i,1) = -1;
      solution = [solution [i-1]];
      unachieved(i) = 0;
      c = 1;
    end
  end
  
end

if sum(unachieved) > 0
  disp('Unachieved goals:') 
  disp(unachieved(unachieved>0))
end
 
disp('A possible sequence is:')
disp(solution)

end 