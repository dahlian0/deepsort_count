# deepsort_count
This program will output the number of detections by class from the txt file obtained from DeepSORT.

What this program is doing
1. rewrite the txt file obtained from DeepSORT into a csv file.
2. compile a list of detected class names for each track ID.
3. calculate the most frequent class name in the list and total it up to output the number of each class detected by DeepSORT.

<img width="956" alt="スクリーンショット 2022-01-28 0 03 58" src="https://user-images.githubusercontent.com/48791086/151385295-716ae096-7ab2-4aef-b7c5-9ae655e00b82.png">

# Installation
You can easily install the libraries using the requirements.txt file.
```bash
pip install -r requirements.txt
```

# Usage
Place the txt file you want to use in data file.

```bash
git clone https://github.com/dahlian0/deepsort_count.git
```
To install the library using the requirements.txt file
```bash
pip install -r requirements.txt
```
The execution command for v4 is
```bash
python v4.py
```
The main execution command for v5 is
```bash
python v5.py
```

## License
This software is released under the MIT License, see LICENSE.

## Authors
Risa SHINODA (Master Course Student at Kyoto University)


