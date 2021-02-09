# Text Adventure

## What Is This?
This is a python script (two actually) that lets YOU create a text adventure game, no coding required! And the best part is? It has no dependencies! Just plain ol' python.

## How Do I Use It?
I'm glad you asked. It's easy!

### Step 1: Make sure Python3 is installed. If not, go to [https://www.python.org/downloads/](https://www.python.org/downloads/)
### Step 2: Write your story!
Create a text file called "story.txt" in this folder.
In this file, write "scenes", each ending with a choice, like this:
```
\# Comment
--
<name>

<text1>
<text2>

<option1>
<option2>

<outcome1>
<outcome2>
```
The name can be anything, as long as you have one scene called "start"

You can have as many lines of text as you want.

You can have as many options as you want, as long as the number of outcomes is the same

If there are no options and no outcomes, the scene will automatically be marked as an "end scene," meaning it will be interpreted as an end to the story.

### Step 3
Run the file "main.py" with Python!
To do this, simply open up a terminal in this folder and type `python main.py`