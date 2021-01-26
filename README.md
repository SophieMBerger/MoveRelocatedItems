# Move "Relocated Items" directory

Ever since a couple of Mac OS versions ago, whenever I update my OS I get a mysterious "Relocated Items" folder that appears on my Desktop.
I decided to create a Python script that automatically moves this folder into a folder I created just for these type of files within my Documents directory.

## Installation
```bash
pip install watchdog
```
## Usage
Change:
```python
desktop_dir = "/Users/SophieMBerger/Desktop"
destination_folder = "/Users/SophieMBerger/Documents/RelocatedItems"
```
to point to your own Desktop path and the path of the directory you want to relocate the "Relocated Items" folder to.

## License
[MIT](https://choosealicense.com/licenses/mit/)
