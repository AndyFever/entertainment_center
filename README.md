# entertainment_center
Displays some classic films with their trailers and movie info. 

Installation
------------

1. To run in Terminal, navigate to the directory containing the files 

**enterainment_centre.py**
**media.py**

2. Run the line of code ```bash python3 entertainment_center.py ```
3. The application Fresh Tomatoes will then open in your default browser

Configuration
-------------

New movies can be added or edited in the enterainment_center.py. 
The format for an instance of a movie is as follows:

```python
# Create an instance of the movie Rear Window
rear_window = media.Movie(
    "Rear Window",
    "In deadly danger...because they saw too much!",
    "http://img.moviepostershop.com/"
    "rear-window-movie-poster-1954-1020143868.jpg",
    "https://www.youtube.com/watch?v=Ob_Sq__g01E",
    "James Stewart",
    "1954")
```
