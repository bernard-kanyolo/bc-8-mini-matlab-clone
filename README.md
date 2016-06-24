[![Build Status](https://travis-ci.org/bernard-kanyolo/bc-8-mini-matlab-clone.svg?branch=master)](https://travis-ci.org/bernard-kanyolo/bc-8-mini-matlab-clone)
# Mini Matlab Clone

## Features

* Create and save new matrices into variables:
```MATLAB
a = [1, 2, 3, 4]
b = [1 2 3; 4 5 6]
```

* Create new matrices using zeros(n), zeros(n,n), ones(n), ones(n,n):
```MATLAB
c = zeros(2,1)
d = zeros(2)
e = ones(2,1)
f = ones(2)
```

* Mini Matlab supports the following Matrix and Array operations:
  * Addition:
  ```MATLAB
  a + 1
  a + b
  ```
  * Transpose (using '):
  ```MATLAB
  a'
  ```
  * Inverse:
  ```MATLAB
  inv(a)
  ```

* Concatenation:
  * Horizontal concatenation:
  ```MATLAB
  A = [a,b]
  ```
  * Vertical concatenation:
  ```MATLAB
  B = [a;b]
  ```

* Saving and Loading workspace:
```MATLAB
save > workspace.mat
load < workspace.mat
```

* View current workspace variables:
```MATLAB
workspace
```

* Installation
```
  Clone this repository
  Navigate into the directory
  [optional] create a virtual environment
  run "pip install -r requirements.txt"
  run "python app.py"
```

* Tested on
```
  Python 2.7
  Python 3.5
```
