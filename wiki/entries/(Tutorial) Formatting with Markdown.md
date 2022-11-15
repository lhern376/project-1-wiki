# (Tutorial) Formatting with Markdown
***



<!-- =================== Intro ========================  -->
<br>
Markdown is a text-to-HTML conversion tool for web writers. Markdown allows you to write using an easy-to-read, easy-to-write plain text format, then convert it to structurally valid XHTML (or HTML).

[https://www.markdownguide.org/cheat-sheet/](https://www.markdownguide.org/cheat-sheet/)
<br>
[https://github.com/trentm/python-markdown2](https://github.com/trentm/python-markdown2)



<!-- =================== Table of Contents ========================  -->
<br>
## Table of Contents
***
1. [Headings](#headings)
2. [Bold and Italic](#bold-and-italic)
3. [Lists](#lists)
4. [Task List](#task-list)
5. [Code](#code)
6. [Code Blocks](#code-blocks)
7. [Links and Images](#links-and-images)
8. [Tables](#tables)
9. [Additional Elements](#additional-elements)



<!-- =================== Headings ========================  -->
<br>
### Headings
***
Syntax:
```text
# The largest heading
## The second largest heading
###### The smallest heading
```
Output:

# The largest heading
## The second largest heading
###### The smallest heading   



<!-- =================== Bold and Italic ========================  -->
<br>
<br>
### Bold and Italic
***
Syntax:
```text
**This is bold text**
*This text is italicized*	
***All bold and italic***	
```
Output:

**This is bold text** <br>
*This text is italicized*	
***All bold and italic***	



<!-- =================== Lists ========================  -->
<br>
<br>
### Lists
***
##### Ordered Lists
Syntax:
```text
1. First item
2. Second item
3. Third item
    1. Indented item
    2. Indented item
4. Fourth item
```
Output:

1. First item
2. Second item
3. Third item
    1. Indented item
    2. Indented item
4. Fourth item

<br>
##### Unordered Lists 
Syntax:
```text
- First item
- Second item
- Third item
    - Indented item
    - Indented item
- Fourth item
```
<br>
Output:

- First item
- Second item
- Third item
    - Indented item
    - Indented item
- Fourth item



<!-- =================== Task Lists ========================  -->
<br>
<br>
### Task List
***
Syntax:
```text
- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media
```
Output:

- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media



<!-- =================== Code ========================  -->
<br>
<br>
### Code
***
Syntax:
```text
At the command prompt, type `nano`.
```
Output:

At the command prompt, type `nano`.



<!-- =================== Code Blocks ========================  -->
<br>
<br>
### Code Blocks
***
Enclose the code to be displayed between three backticks and the name of the programming language.
<br>
<br>
Syntax:
<br>
` ```html
<html>
  <head>
  </head>
</html>
```  `
<br>
<br>
Output:

```html
<html>
  <head>
  </head>
</html>
```


<!-- =================== Links and Images ========================  -->
<br>
<br>
### Links and Images
***
| Element &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |  Syntax |
| -------- | -------- |
| Link | `[title](https://www.example.com)` |
| Image | `![alt text](image.jpg)` |

<br>

Link Syntax:
```text
[Link to example.com](https://www.example.com)
```
Output:

[Link to example.com](https://www.example.com)

<br>
Image Syntax:
```text
![This is an image](https://myoctocat.com/assets/images/base-octocat.svg)
```
Output:

![This is an image](https://myoctocat.com/assets/images/base-octocat.svg)



<!-- =================== Tables ========================  -->
<br>
<br>
### Tables
***
To add a table, use three or more hyphens (---) to create each column’s header, and use pipes (|) to separate each column. For compatibility, you should also add a pipe on either end of the row.

<br>
Syntax:
```text
| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |
```

<br>
Output:

| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |


<!-- =================== Additional Elements ========================  -->
<br>
<br>
### Additional Elements
***
| Element |  Syntax |
| -------- | :--------: |
| Horizontal Rule | `---` |
| Line break | `<br>` |
| Extra space | `&nbsp;` |